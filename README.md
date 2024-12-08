# CS-181 Final Project: Evaluation of Urban Population Percentage on COVID-19 Deaths Across Continents

**Authors**: Viet Nguyen, Minh Nguyen, Long Kim  
**Date**: April 20, 2024

---

## **Project Overview**

This project investigates the impact of urbanization on the COVID-19 pandemic's health outcomes. Specifically, we aim to understand how urban population percentages correlate with COVID-19 death rates across various continents. By analyzing data from trusted sources like the OWID COVID-19 dataset, we examine trends and patterns in the 2022 calendar year. This project focuses on data cleaning, database creation, and preliminary data visualization.

---

## **Datasets Used**

1. **owid-covid-data.json**  
   Contains detailed COVID-19 statistics by country and date. The data is loaded, cleaned, and transformed into a structured pandas DataFrame.

2. **API_SP.URB.TOTL.IN.ZS_DS2_en_csv_v2_43721.csv**  
   Provides urban population data, which is processed and merged with the COVID-19 data for insightful analysis.

3. **world_population.csv**  
   Includes global population figures, merged to provide demographic context for the analysis.

---

## **Functions Overview**

1. **read_json(infilename)**  
   Reads the OWID COVID-19 dataset into a pandas DataFrame for further processing.

2. **clean_urban_df(input_file)**  
   Cleans and standardizes the urban population data, preparing it for merging with the COVID-19 data.

3. **clean_population_df(input_file)**  
   Processes the world population data, aligning it with the necessary structure for database integration.

4. **clean_death_df(input_file)**  
   Aggregates the COVID-19 data on a yearly basis and reformats it for consistent database insertion.

5. **urban_create(dataframe, dbfilename)**  
   Creates and populates an SQLite database table with the cleaned urban population data.

6. **population_create(dataframe, dbfilename)**  
   Establishes a table in the SQLite database for global population statistics.

7. **death_create(dataframe, dbfilename)**  
   Creates a table for COVID-19 death data in the SQLite database.

8. **merged_table(dbfilename, continent)**  
   Merges various datasets into a single table, allowing for continent-specific queries and analyses.

9. **make_scatterplot(dataframe, continent)**  
   Generates scatter plots to visualize the relationship between urban population percentages and COVID-19 deaths.

10. **main()**  
    Orchestrates the entire data flow, from loading datasets to generating visualizations, demonstrating the complete data processing pipeline.

---

## **Implementation Details**

The project is implemented using Python functions that handle specific aspects of data manipulation:

### **1. Data Parsing and Cleaning**  
- **read_json** loads the OWID COVID-19 data, transforming it into a format that's ready for analysis and database insertion.  
- **clean_urban_df**, **clean_population_df**, and **clean_death_df** refine their respective datasets, ensuring data integrity and consistency across the merged database.

### **2. Database Creation and Integration**  
- **urban_create**, **population_create**, and **death_create** set up the SQLite database structure, populating it with cleaned data.  
- **merged_table** consolidates the different data streams into a unified table, enabling continent-specific analysis.

### **3. Data Visualization**  
- **make_scatterplot** generates scatter plots that visually represent the relationship between urbanization and COVID-19 mortality rates.

By leveraging this suite of functions, we aim to uncover significant correlations that may inform public health strategies and urban planning, particularly in the context of pandemic preparedness.

---

## **Results and Analysis**

The analysis showed the following:
- **Europe**: Most countries had an urban population percentage between 50% and 85%, with most having fewer than 20,000 new deaths from COVID-19 in 2022. However, a few outliers displayed significantly higher fatality rates, including one country with over 80,000 deaths.
- **Asia & Oceania**: While urbanization showed some correlation with COVID-19 deaths, countries geographically closer to China (the initial epicenter) displayed higher early death rates, despite varying levels of urbanization.

This analysis underscores that urbanization alone does not fully explain the spread and impact of COVID-19. Factors such as healthcare accessibility, government response, and proximity to initial outbreak locations also played a significant role.

---

## **How to Run the Code**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/viet0901/CS-181-Final-Project.git
   ```

2. **Install required libraries**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the main script**:
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

- Ensure the SQLite database file (**final.db**) is writable and the necessary permissions are granted to avoid execution errors.
- If the SQLite database file specified already exists, running the script will result in an error. To avoid this, ensure the file does not already exist or specify a new name in the script.
```
