import pandas as pd
import numpy as np
import random

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

# Number of transactions
num_samples = 2000  # More transactions for better data

# Generate random Customer IDs (some customers will repeat)
customer_ids = np.random.choice(np.arange(1000, 5000), num_samples)

# Generate random dates (from 2024-01-01 to 2024-12-31)
date_range = pd.date_range(start="2024-01-01", end="2024-12-31")
dates = np.random.choice(date_range, num_samples)

# Product names and categories
products = {
    "Laptop": "Electronics",
    "Smartphone": "Electronics",
    "Tablet": "Electronics",
    "Headphones": "Accessories",
    "Smartwatch": "Accessories",
    "Keyboard": "Peripherals",
    "Mouse": "Peripherals",
    "Monitor": "Displays",
    "Charger": "Accessories",
    "Gaming Console": "Electronics",
    "Speaker": "Accessories",
    "Graphics Card": "PC Components",
    "Printer": "Peripherals",
    "Router": "Networking"
}

product_choices = np.random.choice(list(products.keys()), num_samples)
categories_list = [products[p] for p in product_choices]

# Generate random purchase amounts (higher for expensive items)
amounts = []
for product in product_choices:
    if product in ["Laptop", "Gaming Console", "Smartphone", "Graphics Card"]:
        amounts.append(np.random.randint(500, 3000))  # Expensive items
    elif product in ["Tablet", "Monitor", "Printer", "Router"]:
        amounts.append(np.random.randint(200, 1500))
    else:
        amounts.append(np.random.randint(10, 500))  # Accessories and small items

# Discounts (5% to 50% for random transactions)
discounts = np.random.choice([0, 5, 10, 15, 20, 25, 30, 50], num_samples, p=[0.4, 0.1, 0.1, 0.1, 0.1, 0.05, 0.05, 0.1])
final_amounts = [max(a - (a * d / 100), 5) for a, d in zip(amounts, discounts)]

# Payment methods
payment_methods = ["Credit Card", "Debit Card", "PayPal", "Cash on Delivery", "Cryptocurrency", "UPI"]
payments = np.random.choice(payment_methods, num_samples)

# Order status
order_status = np.random.choice(["Completed", "Pending", "Cancelled"], num_samples, p=[0.85, 0.1, 0.05])

# Locations (random cities)
locations = ["New York", "Los Angeles", "Chicago", "Houston", "San Francisco", "Miami", "Seattle", "Boston", "Denver", "Atlanta"]
customer_locations = [random.choice(locations) for _ in range(num_samples)]

# Create DataFrame
df = pd.DataFrame({
    "CustomerID": customer_ids,
    "Date": dates,
    "Product": product_choices,
    "Category": categories_list,
    "OriginalAmount": amounts,
    "Discount(%)": discounts,
    "FinalAmount": final_amounts,
    "PaymentMethod": payments,
    "OrderStatus": order_status,
    "Location": customer_locations
})

# Save to CSV
df.to_csv("fake_ecommerce_data.csv", index=False)

print("✅ Fake e-commerce dataset 'fake_ecommerce_data.csv' generated successfully!")
