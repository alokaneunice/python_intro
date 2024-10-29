# Initialize an empty dictionary to store items and their prices
items = {}

# Collect items and their prices
items['Yam'] = float(input("Enter the price of Yam: "))
items['Cassava'] = float(input("Enter the price of Cassava: "))
items['Groundnut oil'] = float(input("Enter the price of Groundnut oil: "))
items['Meat'] = float(input("Enter the price of Meat: "))
items['Maize'] = float(input("Enter the price of Maize: "))

# Calculate the total amount
total_amount = sum(items.values())

# Print the total amount
print("\nTotal amount spent:", total_amount)

# Print the final items with details
print("\nItems purchased:")
for item, price in items.items():
    print(f"{item}: {price}")