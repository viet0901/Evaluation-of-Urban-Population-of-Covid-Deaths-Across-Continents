# Final Project: Evaluation of Urban Population Percentage on COVID-19 Deaths Across Continents

**Authors**: Minh Nguyen, Long Kim, Viet Nguyen  
**Date**: April 20, 2024

---

## **Project Overview**  
This project investigates the relationship between urban population percentages and COVID-19 deaths across different continents. Specifically, it aims to understand whether higher urbanization contributes to increased COVID-19 mortality rates and how access to healthcare in urban areas affects pandemic outcomes. The study also explores whether proximity to the origin of COVID-19 (China) impacts the number of COVID-19 cases in a country. The project combines data from three key sources to examine the spread and fatality of the virus in urban settings across the globe.

---

## **Research Question**  
How does the percentage of urban population correlate with COVID-19 deaths across different continents? Does urbanization affect the spread of the virus and its fatality rate, and does proximity to China influence these outcomes?

---

## **Datasets**

1. **COVID-19 Data (Our World in Data)**  
   - Link: [COVID-19 Dataset](https://ourworldindata.org/covid-cases)  
   - This dataset provides comprehensive COVID-19 statistics including total cases and deaths by country and date. It is used to analyze the impact of the pandemic on different countries.

2. **Urban Population Data (World Bank)**  
   - Link: [Urban Population Dataset](https://data.worldbank.org/indicator/SP.URB.TOTL)  
   - This dataset provides urban population metrics, which are used to assess the level of urbanization in each country.

3. **World Population Data (Kaggle)**  
   - Link: [World Population Dataset](https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset)  
   - This dataset offers detailed population data by country, useful for calculating urban population percentages and demographic context.

---

## **Methodology**  

To explore the relationship between COVID-19 deaths and urban population percentage, we will utilize the pandas and matplotlib libraries in Python for data manipulation and visualization. The process involves the following steps:

1. **Reading and Cleaning the Data**:  
   We will load the datasets and clean them to ensure consistency. Missing values will be handled, duplicates will be removed, and the data will be transformed for analysis.

2. **Merging Datasets**:  
   The three datasets will be merged based on the common attribute: country name. This will allow for an integrated analysis of COVID-19 deaths, urban population, and overall population data.

3. **Group by Continent**:  
   The dataset will be grouped by continent to explore regional differences in COVID-19 deaths and urbanization.

4. **Exploratory Data Analysis (EDA)**:  
   We will explore the correlation between urban population percentages and COVID-19 deaths, identifying trends and patterns.

5. **Visualization**:  
   Scatter plots will be created to visualize the relationship between urbanization and COVID-19 mortality rates across continents.

---

## **Functions Overview**

Here is a list of functions we will use in our analysis:

- **read_data()**: Reads the datasets from the database and returns pandas DataFrame objects.
- **clean_data(df)**: Cleans the data by handling missing values, removing duplicates, and ensuring consistency within each DataFrame.
- **merge_datasets(df1, df2, df3)**: Merges the three cleaned DataFrames based on a common attribute (country name).
- **group_by_continent(df)**: Groups the data by continent for continent-specific analysis.
- **calculate_urban_percentage(df)**: Calculates the urban population percentage for each country based on the total population and urban population columns.
- **explore_relationship(df)**: Conducts exploratory data analysis (EDA) to identify trends and correlations between urban population percentage and COVID-19 deaths.
- **visualize_findings(df)**: Creates visualizations, such as scatter plots, to illustrate the relationship between urban population percentage and COVID-19 deaths across continents.
- **save_results(df, filename)**: Saves the analyzed and visualized data to a file for further reference or sharing.

---

## **Implementation**

The project utilizes Python with the **pandas** and **matplotlib** libraries for data analysis and visualization. The datasets are cleaned, merged, and analyzed to explore the relationship between urbanization and COVID-19 mortality rates. Visualizations are created to provide insights into the effects of urbanization on the spread of the virus.

---

## **Conclusion**

This project will help us understand how urbanization influences COVID-19 deaths across different continents and whether urban population density plays a significant role in the spread and fatality of the virus. The findings will contribute to public health strategies and urban planning, offering insights into pandemic preparedness.

---

## **How to Run the Code**

1. Clone the repository:
   ```bash
   git clone https://github.com/viet0901/Evaluation-of-Urban-Population-of-Covid-Deaths-Across-Continents.git
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the main script:
   ```bash
   python main.py
   ```

---

## **Disclaimer**

This project is for academic purposes only. The authors are not responsible for the accuracy of the data or any conclusions drawn from it. All rights are reserved by the original data providers.

---

## **Acknowledgments**

Special thanks to Dr. Buell for the initial JSON reading function, which was adapted for this project.

---

## **Note**

- Ensure that the SQLite database file (`final.db`) is writable and the necessary permissions are granted to avoid execution errors.
- If the SQLite database file already exists, running the script may result in an error. Please ensure the file does not already exist or specify a new name for the database file in the script.
