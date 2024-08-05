# Formula1-Racing-Data-Analysis
Built a scalable data pipeline and conducted in-depth analysis using Azure Databricks, Delta Lake, Azure Data Factory and Power BI. 



# 🚀 Formula 1 Data Analysis with Azure Databricks 🏎️

Welcome to my GitHub repository where I showcase a comprehensive data analysis project using Azure Databricks! This project dives into Formula 1 racing data, leveraging powerful tools and techniques to extract insights and create impactful visualizations.

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [The Process](#the-process)
- [Key Features](#key-features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview
This project involves analyzing Formula 1 racing data using various Azure services. The data is ingested, transformed, and analyzed to create insightful reports and visualizations. While the Unity Catalog part is not included, this repository contains all Databricks notebooks I used throughout the course.

## Technologies Used
- **Azure Databricks**
- **PySpark**
- **Spark SQL**
- **Delta Lake**
- **Azure Data Lake Storage Gen2**
- **Azure Data Factory**
- **Power BI**

## Getting Started
To get started with the notebooks in this repository, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/f1-data-analysis.git
   cd f1-data-analysis
   ```

2. **Set Up Azure Databricks**
   - Create an Azure Databricks workspace.
   - Configure clusters and import the notebooks from this repository.

3. **Run the Notebooks**
   - Open the notebooks in your Databricks workspace.
   - Follow the step-by-step instructions provided in the notebooks.

## Project Structure
The repository is organized as follows:

```plaintext
f1-data-analysis/
├── data/
│   └── (Data files used in the project)
├── notebooks/
│   ├── 01_Data_Ingestion.ipynb
│   ├── 02_Data_Transformation.ipynb
│   ├── 03_Data_Analysis.ipynb
│   └── 04_Data_Visualization.ipynb
├── README.md
└── LICENSE
```

## The Process
1. **Data Ingestion**: Data is ingested from the Ergast API, which provides a rich dataset on Formula 1 races, drivers, circuits, and more. This data is stored in Azure Data Lake Storage Gen2.
2. **Data Transformation**: Using PySpark and Spark SQL, the raw data is cleaned, transformed, and prepared for analysis. This includes handling missing values, transforming data types, and creating new features.
3. **Data Analysis**: Various analyses are conducted to uncover trends, patterns, and insights. This includes examining race results, driver performance, team statistics, and other interesting metrics.
4. **Data Visualization**: The transformed data is visualized using Power BI, creating interactive and dynamic dashboards that allow users to explore the data and insights effectively.

## Key Features
- **Data Ingestion**: Ingesting data from the Ergast API into Azure Data Lake Storage.
- **Data Transformation**: Using PySpark and Spark SQL to clean and transform raw data.
- **Data Analysis**: Conducting various analyses to uncover trends and patterns in the racing data.
- **Data Visualization**: Creating compelling visualizations using Power BI to present the analysis results.



