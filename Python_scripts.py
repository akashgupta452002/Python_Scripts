# imported Library
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load your dataset into a DataFrame
file_path = 'C:\\Users\\Deepak\\Desktop\\SaleData.xlsx'
df = pd.read_excel(file_path)

# Check the first few rows of the dataset to understand its structure
print(df.head())

# Check the data types of each column
print(df.dtypes)

# Check basic statistics of numerical columns
print(df.describe())

# Create a bar plot of sales by region
plt.figure(figsize=(10,6))
sns.barplot(x = 'Region', y = 'Sale_amt', data=df)
plt.title('Sales by Region')
plt.show()

#Create a scatter plot to visualize the relationship between unit price and sales amount
plt.figure(figsize = (8,6))
sns.scatterplot(x = 'Unit_price',  y = 'Sale_amt', data = df)
plt.title('Unit Price vs. Sales Amount')
plt.show()

#Sales Over time
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# Extract Year and Month as separate columns
df['Year'] = df['OrderDate'].dt.year
df['Month'] = df['OrderDate'].dt.month

# Create a new DataFrame for monthly sales
monthly_sales = df.groupby(['Year', 'Month'])['Sale_amt'].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(x='Month', y='Sale_amt', hue='Year', data=monthly_sales)
plt.title('Monthly Sales Trends')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.legend(title='Year')
plt.show()

#Identify the top-selling items
top_items = df.groupby('Item')['Sale_amt'].sum().sort_values(ascending=False).head(5)
print("Top Selling Items:")
print(top_items)

#Analyze the performance of managers in terms of total sales
manager_sales = df.groupby('Manager')['Sale_amt'].sum().sort_values(ascending=False)
print("Manager Sales Performance:")
print(manager_sales)

#Visualize the distribution of sales amounts
plt.figure(figsize=(10, 6))
sns.histplot(df['Sale_amt'], bins=20, kde=True)
plt.title('Sales Distribution')
plt.xlabel('Sale Amount')
plt.ylabel('Frequency')
plt.show()

#Determine which items have the highest and lowest units sold
item_units_sold = df.groupby('Item')['Units'].sum().sort_values(ascending=False)
print("Units Sold by Item:")
print(item_units_sold)

#Calculate and visualize the average unit price for each item
plt.figure(figsize=(10, 6))
sns.barplot(x='Item', y='Unit_price', data=df, estimator=np.mean)  # Use np.mean as the estimator
plt.title('Average Unit Price by Item')
plt.xticks(rotation=45)
plt.ylabel('Average Unit Price')
plt.show()

#Examine how the sales of specific items have evolved over time
plt.figure(figsize=(12, 6))
sns.lineplot(x='OrderDate', y='Sale_amt', hue='Item', data=df)
plt.title('Item-wise Sales Trends')
plt.xlabel('Order Date')
plt.ylabel('Sales Amount')
plt.xticks(rotation=45)
plt.legend(loc='upper right')
plt.show()


