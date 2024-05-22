import sqlite3

# Task 1: Create a connection to the SQLite database
conn = sqlite3.connect('SQL_Lab.db')

cursor = conn.cursor()

# Task 2: Create tables

# Customers table
cursor.execute('''CREATE TABLE IF NOT EXISTS Customers (
                    customer_id INTEGER PRIMARY KEY,
                    customer_name TEXT,
                    customer_age INTEGER
                  )''')

# Orders table
cursor.execute('''CREATE TABLE IF NOT EXISTS Orders (
                    order_id INTEGER PRIMARY KEY,
                    customer_id INTEGER,
                    shippement_id INTEGER,
                    quantity INTEGER,
                    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
                  )''')

# Products table
cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                    product_id INTEGER PRIMARY KEY,
                    product_name TEXT,
                    product_category TEXT
                  )''')

# Sales table
cursor.execute('''CREATE TABLE IF NOT EXISTS Sales (
                    sales_id INTEGER,
                    product_id INTEGER,
                    sales_person_name TEXT,
                    Sales_amount INTEGER,
                    PRIMARY KEY (sales_id, sales_person_name),
                    FOREIGN KEY (product_id) REFERENCES Products(product_id)
                  )''')

# Task 3: Insert data into tables

# Customers data
customers_data = [
    (100, 'John Svendson', 35),
    (200, 'Stephen Adams', 25),
    (300, 'Kari Pettersen', 40),
    (400, 'James McClure', 30)
]
cursor.executemany('INSERT INTO Customers VALUES (?, ?, ?)', customers_data)

# Orders data
orders_data = [
    (1000, 100, 5000, 100),
    (1001, 400, 5050, 30),
    (1002, 100, 5100, 20),
    (1003, 200, 5500, 50),
    (1004, 200, 5350, 10),
    (1005, 300, 5450, 200)
]
cursor.executemany('INSERT INTO Orders VALUES (?, ?, ?, ?)', orders_data)

# Products data
products_data = [
    (12, 'Bike ABC', 'Road Bike'),
    (13, 'Bike DEF', 'Mountain Bike'),
    (14, 'Bike GHI', 'Road Bike'),
    (15, 'Bike JKL', 'Touring Bike')
]
cursor.executemany('INSERT INTO Products VALUES (?, ?, ?)', products_data)

# Sales data
sales_data = [
    (10000, 12, 'Joe Brown', 1000),
    (10001, 12, 'Bill Johnson', 5000),
    (10002, 13, 'Joe Brown', 10000),
    (10003, 15, 'Bill Johnson', 3000)
]
cursor.executemany('INSERT INTO Sales VALUES (?, ?, ?, ?)', sales_data)

conn.commit()

# Task 4: SQL statement to find customers in customers table with age greater than 30
cursor.execute('''SELECT * FROM Customers WHERE customer_age > 30''')
customers_over_30 = cursor.fetchall()
print("Customers with age greater than 30:")
for customer in customers_over_30:
    print(customer)

# Task 5: SQL statement to return customer_name, order_id, quantity from customers and orders tables
cursor.execute('''SELECT Customers.customer_name, Orders.order_id, Orders.quantity 
                  FROM Customers 
                  JOIN Orders ON Customers.customer_id = Orders.customer_id''')
customer_order_info = cursor.fetchall()
print("\nCustomer Name, Order ID, Quantity:")
for info in customer_order_info:
    print(info)

# Task 6: SQL statement to return the distinct list of product categories from the product table
cursor.execute('''SELECT DISTINCT product_category FROM Products''')
distinct_categories = cursor.fetchall()
print("\nDistinct Product Categories:")
for category in distinct_categories:
    print(category[0])

# Task 7: SQL statement to return sales_person_name, product_name, Sales_amount for product with product id equal to 12
cursor.execute('''SELECT Sales.sales_person_name, Products.product_name, Sales.Sales_amount
                  FROM Sales 
                  JOIN Products ON Sales.product_id = Products.product_id
                  WHERE Products.product_id = 12''')
product_12_sales = cursor.fetchall()
print("\nSales for Product ID 12:")
for sale in product_12_sales:
    print(sale)

# Task 8: SQL statement to update the sales_person_name from Joe Brown to Sophie Thomas for sales_id 10000
cursor.execute('''UPDATE Sales 
                  SET sales_person_name = 'Sophie Thomas' 
                  WHERE sales_id = 10000''')

conn.commit()
cursor.close()
conn.close()



# Task 9: Write a function (queryAPI) that takes as input API resource and query parameter and prints status code issued by a server in response
import requests

def queryAPI(api_resource, query_parameter):
    """
    Function to query an API and print the status code, headers, and key-value pairs from the server response.
    
    Parameters:
        api_resource (str): The URL of the API resource.
        query_parameter (dict): Dictionary containing query parameters.
    """
    try:
        # Send a GET request to the API with the query parameters
        response = requests.get(api_resource, params=query_parameter)
        
        # Print status code
        print("\nStatus Code:", response.status_code)
        
        # Print headers
        print("Headers:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")
        
        # Print key-value pairs from server response
        print("\nResponse Data:")
        for key, value in response.json().items():
            print(f"{key}: {value}")
    
    except requests.exceptions.RequestException as e:
        print("Error:", e)

# Example usage of queryAPI function
api_resource = "https://api.datamuse.com/"
query_parameter = {"rel_rhy": "funny"}
queryAPI(api_resource, query_parameter)


# Task 10: Write a Python program that uses BeautifulSoup to go to https://news.google.com and prints out all of the headlines on the page.
from bs4 import BeautifulSoup

def find_headlines(url):
    """
    Function to retrieve headlines from a webpage.
    
    Parameters:
        url (str): The URL of the webpage.
        
    Returns:
        list: List of headlines found on the webpage.
    """
    headlines = []
    try:
        # Send a GET request to the webpage
        response = requests.get(url)
        
        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all <a> tags containing headlines
        headlines_tags = soup.find_all('a')
        
        # Extract text from <a> tags and append to the list of headlines
        for tag in headlines_tags:
            headline = tag.text.strip()
            if headline:
                headlines.append(headline)
    
    except requests.exceptions.RequestException as e:
        print("Error:", e)
    
    return headlines

def find_headline_by_keyword(headlines, *keywords):
    """
    Function to find headlines containing specified keywords.
    
    Parameters:
        headlines (list): List of headlines.
        *keywords (str): Variable number of keywords to search for.
        
    Returns:
        list: List of headlines containing all specified keywords.
    """
    matching_headlines = []
    for headline in headlines:
        if all(keyword.lower() in headline.lower() for keyword in keywords):
            matching_headlines.append(headline)
    return matching_headlines

# Example usage of find_headlines function
url = "https://news.google.com"
all_headlines = find_headlines(url)

# Example usage of find_headline_by_keyword function
matching_headlines = find_headline_by_keyword(all_headlines, "covid", "vaccine")
print("\nHeadlines containing 'covid' and 'vaccine':")
for headline in matching_headlines:
    print(headline)
