# Retail Data Integration 

## Project Overview

This project demonstrates the integration and analysis of retail sales data using Excel, SQL, and Python.

The dataset contains 100,000 retail records covering sales, revenue, costs, margins, inventory, customer information, brands, categories, cities, payment modes, and sales channels.

## Tools Used

- Python – Data cleaning and validation
- PostgreSQL / SQL – Data storage and analysis
- Microsoft Excel – PivotTables and data visualization

## Python Data Cleaning

Python with Pandas was used to:

- Handle missing customer age values using the median.
- Replace missing customer gender values with "Unknown".
- Convert Invoice_Date into datetime format.
- Check duplicate records.
- Validate Revenue using Units × Selling Price.
- Identify low-stock records.
- Export the cleaned dataset.

### Python Results

- Duplicate Records: 0
- Missing Values After Cleaning: 0
- Low Stock Records: 1,729

## SQL Analysis

PostgreSQL was used to import the dataset into the `retail_sales` table and perform analytical queries.

The analysis included:

- Total records
- Total revenue
- Total margin
- Category-wise revenue
- City-wise revenue
- Channel-wise revenue
- Top brands by revenue
- Payment mode analysis
- Low-stock analysis
- Average customer age

### SQL Results

- Total Records: 100,000
- Total Revenue: ₹39,335,134.98
- Low Stock Records: 1,729

## Excel Analysis

Microsoft Excel was used to create PivotTables and charts for:

- Category-wise Revenue
- City-wise Revenue
- Channel-wise Revenue
- Brand-wise Revenue

### Key Insights

- Fruits generated the highest revenue among categories.
- Kolkata generated the highest revenue among cities.
- Omnichannel was the highest-revenue sales channel.
- ITC was the top-performing brand by revenue.

## Project Files

- `retail_cleaning.py` – Python data cleaning script
- `retail_cleaned.csv` – Cleaned dataset
- `retail_sql_export.csv` – SQL exported dataset
- `Retail_Data_Integration_Report.pdf` – Final project report

## Conclusion

This project demonstrates how Excel, SQL, and Python can be combined for an end-to-end retail data analysis workflow. SQL was used for database analysis, Excel for visualization, and Python for data cleaning and validation.
