import pandas as pd

# Load the retail dataset
df = pd.read_csv("Indian FMCG Retail Sales  Customer  Inventory (2024).csv")


# Handle missing values
df["Customer_Age"] = df["Customer_Age"].fillna(
    df["Customer_Age"].median()
)

df["Customer_Gender"] = df["Customer_Gender"].fillna("Unknown")


# Convert Invoice_Date to datetime format
df["Invoice_Date"] = pd.to_datetime(
    df["Invoice_Date"],
    errors="coerce"
)


# Check duplicate records
print("Duplicate Records:")
print(df.duplicated().sum())


# Verify Revenue calculation
calculated_revenue = df["Units"] * df["Selling_Price"]

print("Revenue Calculation Check:")
print(
    (df["Revenue"] - calculated_revenue).abs().sum()
)


# Check low stock items
low_stock = df[
    df["Stock_On_Hand"] <= df["Reorder_Level"]
]

print("Low Stock Records:")
print(len(low_stock))


# Check missing values after cleaning
print("Missing Values After Cleaning:")
print(df.isnull().sum())


# Export cleaned dataset
df.to_csv("retail_cleaned.csv", index=False)

print("Cleaned dataset exported successfully!")