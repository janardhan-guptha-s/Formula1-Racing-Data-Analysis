# 🚀 Formula 1 Data Analysis with Azure Databricks 🏎️

Welcome to my GitHub repository where I showcase a comprehensive data analysis project using Azure Databricks! This project dives into Formula 1 racing data, leveraging powerful tools and techniques to extract insights and create impactful visualizations.

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
   - Generate a GitHub token.
   - Link the token with your Databricks account.
   - Create a GitHub folder in Databricks and commit directly from Databricks.

2. **Set Up Azure Databricks**
   - Create an Azure Databricks workspace.
   - Configure clusters and import the notebooks from this repository.

3. **Run the Notebooks**
   - Open the notebooks in your Databricks workspace.
   - Follow the step-by-step instructions provided in the notebooks.
 
## Setting Up Azure Services

### Azure Data Lake Storage Gen2
1. **Create a Storage Account**
   - Sign in to the [Azure portal](https://portal.azure.com/).
   - In the left-hand menu, select **Storage accounts** and then **Create**.
   - Select the subscription and resource group.
   - Enter a name for the storage account.
   - Select **Review + create** and then **Create**.

2. **Enable Hierarchical Namespace**
   - After the storage account is created, go to the **Data Lake Storage** section.
   - Enable **Hierarchical namespace**.

3. **Create a Container**
   - Navigate to the storage account and select **Containers**.
   - Click **+ Container** and create a new container for your data.

### Azure Data Factory
1. **Create a Data Factory**
   - In the Azure portal, select **Create a resource** and search for **Data Factory**.
   - Select **Data Factory** and click **Create**.
   - Choose the subscription, resource group, and region.
   - Enter a name for the data factory.
   - Click **Review + create** and then **Create**.

2. **Set Up Linked Services**
   - In the Data Factory, go to the **Manage** tab and select **Linked services**.
   - Click **+ New** and choose **Azure Data Lake Storage Gen2**.
   - Configure the linked service with the storage account details.

3. **Create Pipelines**
   - In the **Author** tab, create pipelines to ingest and transform data.
   - Use activities such as **Copy Data** to move data from source to destination.

### Linking Azure Data Lake Storage Gen2 and Azure Data Factory with Databricks
1. **Generate Access Keys**
   - In the Azure portal, navigate to your storage account.
   - Under **Security + networking**, select **Access keys**.
   - Copy the access keys.

2. **Configure Databricks to Access Storage**
   - In your Databricks workspace, go to **Clusters** and select your cluster.
   - Click on **Configuration** and add the following Spark configurations:
     ```plaintext
     spark.hadoop.fs.azure.account.key.<storage-account-name>.dfs.core.windows.net <storage-account-key>
     ```

3. **Use Data Factory to Trigger Databricks Notebooks**
   - In the Data Factory pipeline, add a **Databricks Notebook** activity.
   - Configure it to run specific notebooks in your Databricks workspace.


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

## Dominant Drivers Dashboard
![Dominant_Drivers_Dashboard](https://github.com/user-attachments/assets/b0df9c66-7198-4533-9b58-82fd95eb4a52)

## Dominant Teams Dashboard
![Dominant_Teams_Dashboard](https://github.com/user-attachments/assets/ed3292e7-1c3b-4b93-80a9-bd1878ea7a32)
