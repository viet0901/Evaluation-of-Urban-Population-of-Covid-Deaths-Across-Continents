'''Final Project
    Author: Viet Nguyen, Minh Nguyen, Long Kim. All right reserved.  
    Date: 19 April 2024
    
'''

import json
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#123456789 123456789 123456789 123456789 123456789 123456789 123456789
######################################################################
def read_json(infilename):
    """ Borrow from Dr. Buell and modified
        Read the owid-covid-data.json using the Python json package 
        into Dataframe 
        Parameters:
            infilename: the JSON file to read 
        Returns:
            thedata: the dataframe
    """
    with open(infilename, encoding='utf-8') as thefile:
        covid = json.load(thefile)
    listofdicts = []
    for code, codesubtree in covid.items():
        for value in codesubtree:
            if value == 'data':
                list_dict = codesubtree['data']
                for items in list_dict:
                    items['code'] = code
                    listofdicts.append(items)
    dataframe = pd.DataFrame(listofdicts)
    dataframe.set_index(['code', 'date'], inplace=True)
    return dataframe

#123456789 123456789 123456789 123456789 123456789 123456789 123456789
######################################################################

def clean_urban_df(input_file):
    """
    Clean and reformat urban population data from a DataFrame.
    This function processes DataFrame columns, renaming them, handling 
    incorrect data types, and setting appropriate indexes.
    Parameters:
        input (pandas.DataFrame): The DataFrame containing urban data.    
    Returns:
        pandas.DataFrame: A cleaned DataFrame with urban population percentage.
    """
    clean_df = input_file[["Country Name", "Country Code", "2022"]]
    clean_df = clean_df.rename(columns={"Country Name": "Country",
                                        "Country Code": "Code",
                                        "2022": "Urban_Percentage_2022"})
    for element in clean_df["Urban_Percentage_2022"]:
        if str(element).count('.') > 1:
            clean_df["Urban_Percentage_2022"].replace(element, np.nan, inplace = True)
        else:
            clean_df["Urban_Percentage_2022"].replace(element, float(element), inplace = True)
    clean_df = clean_df.dropna()
    clean_df.set_index(['Code'], inplace = True)
    return clean_df

#123456789 123456789 123456789 123456789 123456789 123456789 123456789
######################################################################

def clean_poppulation_df(input_file):
    """ 
    Clean and reformat population data from a DataFrame.
    This function processes DataFrame columns, renaming them and 
    setting appropriate indexes.
    Parameters:
        input (pandas.DataFrame): The DataFrame containing population data.
    Returns:
        pandas.DataFrame: A cleaned DataFrame with relevant population data.
    """
    clean_df =  input_file[["CCA3", "Country/Territory", "Continent", "2022 Population"]]
    clean_df = clean_df.rename(columns={"CCA3": "Code",
                                        "Country/Territory": "Country",
                                        "2022 Population": "Population_2022"})
    clean_df.set_index(['Code'], inplace = True)
    return clean_df

#123456789 123456789 123456789 123456789 123456789 123456789 123456789
######################################################################

def clean_death_df(input_file):
    """ 
    Clean and reformat COVID-19 related data from a DataFrame.
    This function extracts year, month, and day from dates, and 
    aggregates data for the year 2022. 
    Parameters:
        input (pandas.DataFrame): The DataFrame containing raw COVID-19 
        data.    
    Returns:
        pandas.DataFrame: A DataFrame with aggregated COVID-19 data for 2022.
    """
    clean_df = input_file.reset_index()
    date = clean_df['date'].str.split(expand = True, pat = "-", n = 2)
    clean_df.insert(loc = 2, column = 'Year', value = date[0])
    clean_df.insert(loc = 3, column = 'Month', value = date[1])
    clean_df.insert(loc = 4, column = 'Day', value = date[2])
    clean_df = clean_df[['code', 'Year', 'Month', 'Day', 'new_cases',
                         'new_deaths', 'new_vaccinations']]
    clean_df = clean_df[clean_df['Year'] == '2022']
    clean_df = clean_df.groupby(['code']).mean(numeric_only=True)
    clean_df = clean_df.reset_index()
    clean_df = clean_df.rename(columns={"code": "Code",
                                        "new_cases": "New_cases_2022",
                                        "new_deaths": "Total_new_deaths_2022",
                                        "new_vaccinations": "New_vaccinations_2022"})
    clean_df.set_index(['Code'], inplace = True)
    return clean_df

#123456789 123456789 123456789 123456789 123456789 123456789 123456789
######################################################################

def urban_create(dataframe, dbfilename):
    """ 
    Create and populate an SQLite table for urban data.
    This function creates (if not exists) an SQLite table and populates
    it with urban data.
    Parameters:
        dataframe (pandas.DataFrame): The DataFrame to insert into the 
        SQLite database.
        dbfilename (str): Path to the SQLite database file.
    Returns:
        none: create table in database
    """
    con = sqlite3.connect(dbfilename)
    cur = con.cursor()
    creation =  """ CREATE TABLE IF NOT EXISTS urban_table (
                Code VARCHAR(3) NOT NULL PRIMARY KEY, 
                Country VARCHAR NULL,
                Urban_Percentage_2022 FLOAT NULL)"""
    cur.execute(creation)
    dataframe.to_sql("urban_table", con, if_exists = "replace", index = True)
    con.commit()

#123456789 123456789 123456789 123456789 123456789 123456789 123456789
######################################################################

def population_create(dataframe, dbfilename):
    """ 
    Create and populate an SQLite table for population data.
    This function creates (if not exists) an SQLite table and 
    populates it with population data.
    Parameters:
        dataframe (pandas.DataFrame): The DataFrame to insert into the 
        SQLite database.
        dbfilename (str): Path to the SQLite database file.
    Returns:
        none: create table in database
    """
    con = sqlite3.connect(dbfilename)
    cur = con.cursor()
    creation =  """ CREATE TABLE IF NOT EXISTS population_table (
                Code VARCHAR(3) NOT NULL PRIMARY KEY, 
                Country VARCHAR NULL,
                Continent VARCHAR NULL,
                Population_2022 FLOAT NULL)"""
    cur.execute(creation)
    dataframe.to_sql("population_table", con, if_exists = "replace", index = True)
    con.commit()

#123456789 123456789 123456789 123456789 123456789 123456789 123456789
######################################################################

def death_create(dataframe, dbfilename):
    """ 
    Create and populate an SQLite table for COVID-19 death data.
    This function creates (if not exists) an SQLite table and populates 
    it with COVID-19 data.
    Parameters:
        dataframe (pandas.DataFrame): The DataFrame to insert into the 
        SQLite database.
        dbfilename (str): Path to the SQLite database file.
    Returns:
        none: create table in database
    """
    con = sqlite3.connect(dbfilename)
    cur = con.cursor()
    creation =  """ CREATE TABLE IF NOT EXISTS death_table (
                Code VARCHAR(3) NOT NULL PRIMARY KEY, 
                New_cases_2022 FLOAT NULL,
                Total_new_death_2022 FLOAT NULL,
                New_vaccinations_20222 FLOAT NULL)"""
    cur.execute(creation)
    dataframe.to_sql("death_table", con, if_exists = "replace", index = True)
    con.commit()

#123456789 123456789 123456789 123456789 123456789 123456789 123456789
######################################################################

def merged_table(dbfilename, continent):
    """ 
    Create a merged table from existing tables and retrieve data for 
    a specific continent.
    This function merges death, population, and urban data into a single 
    table
    and filters the data based on the continent.
    Parameters:
        dbfilename (str): Path to the SQLite database file.
        continent (str): The continent name to filter the data. 
    Returns:
        pandas.DataFrame: A DataFrame containing the merged data for the 
        specified continent.
    """
    con = sqlite3.connect(dbfilename)
    cur = con.cursor()
    merge = """CREATE TABLE IF NOT EXISTS merged_table AS
            SELECT death_table.*, population_table.Population_2022, population_table.Continent, 
                   urban_table.Urban_Percentage_2022
            FROM death_table
            INNER JOIN population_table ON death_table.Code = population_table.Code
            INNER JOIN urban_table ON death_table.Code = urban_table.Code
        """
    cur.execute(merge)
    select_continent = """SELECT * FROM merged_table WHERE Continent = ?"""
    continent_df = pd.read_sql_query(select_continent, con, params=(continent,))
    con.commit()
    return continent_df

#123456789 123456789 123456789 123456789 123456789 123456789 123456789
######################################################################

def make_scatterplot(dataframe, continent):
    """
    Generate a scatter plot showing the relationship between urban 
    population percentage and COVID-19 deaths. This function plots 
    data points representing the urban population percentage and the 
    total new deaths from COVID-19 in 2022 for a specific continent.
    Parameters:
        dataframe (pandas.DataFrame): The DataFrame containing data 
        to plot.
        continent (str): The continent name used for the plot title.
    Returns:
        none: show plot
    """
    x_axis = dataframe[
        'Urban_Percentage_2022']
    y_axis = dataframe['Total_new_deaths_2022']
    plt.scatter(x_axis,y_axis,alpha=0.7)
    plt.xlabel('Urban Population Percentage in 2022')
    plt.ylabel('Total new death in 2022')
    plt.title(f'The relationship between Urban Population and Covid Death in {continent}')
    plt.show()


#123456789 123456789 123456789 123456789 123456789 123456789 123456789
######################################################################
def main():
    """ This fuction calls other functions and prints out what is 
        needed.
        Parameter:
            None
        Return:
            None
    """
    death_path = "./owid-covid-data.json"
    urban_path = "./API_SP.URB.TOTL.IN.ZS_DS2_en_csv_v2_43721.csv"
    population_path = "./world_population.csv"
    db_path = "./final.db"
    death_df  = read_json(death_path)
    urban_df = pd.read_csv(urban_path)
    population_df = pd.read_csv(population_path)
    #death_df = clean_death_df(death_df)
    population_df = clean_poppulation_df(population_df)
    urban_df = clean_urban_df(urban_df)
    population_create(population_df, db_path)
    urban_create(urban_df, db_path)
    death_create(death_df, db_path)
    europe = merged_table(db_path, 'Europe')
    asia = merged_table(db_path, 'Asia')
    oceania = merged_table(db_path, 'Oceania')
    south_america = merged_table(db_path, 'South America')
    north_america = merged_table(db_path, 'North America')
    print(death_df)
    #print(europe)
    #print(asia)
    #print(oceania)
    #print(south_america)
    #print(north_america)
    #make_scatterplot(europe, "Europe")
    #make_scatterplot(asia, "Asia")
    #make_scatterplot(oceania, "Oceania")
    #make_scatterplot(south_america, "South America")
    #make_scatterplot(north_america, "North America")


main()
