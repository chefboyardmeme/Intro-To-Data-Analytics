import pandas as pd
import numpy as np

# Set option to display all columns
pd.set_option('display.max_columns', None)

# Task 1: Load the CSV file to create a Pandas DataFrame (items)
items = pd.read_csv('items.csv')

# Task 2: Display the first seven items of items DataFrame
print("First seven items:")
print(items.head(7))

# Task 3: Display the last seven items of items DataFrame
print("\nLast seven items:")
print(items.tail(7))

# Task 4: Display description of items DataFrame (use “info” method)
print("\nDescription of items DataFrame:")
print(items.info())

# Task 5: Display the number of rows and columns in items DataFrame
num_rows, num_cols = items.shape
print("\nNumber of rows:", num_rows)
print("Number of columns:", num_cols)

# Task 6: Display descriptive statistics for Bottle_Cost (use “describe” method)
print("\nDescriptive statistics for Bottle_Cost:")
print(items['Bottle_Cost'].describe())

# Task 7: Add a new Column ‘bottle_profit_margin’ to items DataFrame
items['bottle_profit_margin'] = (items['Bottle_Retail_Price'] - items['Bottle_Cost']) / items['Bottle_Retail_Price']

# Task 8: Delete/drop rows 5-15 from items DataFrame
items.drop(range(5, 16), inplace=True)

# Task 9: Display items that have Bottle_Volume_ml > 750 and more than 12 pack and bottle_profit_margin more than 0.3
filtered_items = items[(items['Bottle_Volume_ml'] > 750) & (items['Pack'] > 12) & (items['bottle_profit_margin'] > 0.3)]
print("\nItems with Bottle_Volume_ml > 750, Pack > 12, and bottle_profit_margin > 0.3:")
print(filtered_items)

# Task 10: Display the number of energy drinks ('Category' ='Energy Drink')
num_energy_drinks = items[items['Category'] == 'Energy Drink'].shape[0]
print("\nNumber of energy drinks:", num_energy_drinks)

# Task 11: Create a new DataFrame ‘items2’ that has all rows and 4 attributes from ‘items’ DataFrame
items2 = items[['Item_id', 'Item_Description', 'Bottle_Retail_Price', 'bottle_profit_margin']]

# Task 12: Add a new Column ‘QTY’ to the data frame using numpy.random.randint
items2['QTY'] = np.random.randint(1, 100, size=len(items2))

# Display items2 DataFrame
print("\nitems2 DataFrame:")
print(items2)
