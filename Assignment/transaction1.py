#Mr jide account balance is 100, the bank management has decided to multiply his money by 2 while his account balance is < 10000.
# Write a python function code that will show the transaction details

def transaction_details(initial_balance):
    balance = initial_balance
    transactions = []  # List to hold transaction details

    while balance < 10000:
        transactions.append(f"Current balance: {balance}")
        balance *= 2  # Multiply the balance by 2
        transactions.append(f"New balance after multiplication: {balance}")

    transactions.append("Final balance reached or exceeded 10,000.")
    return transactions

initial_balance = 100
details = transaction_details(initial_balance)

# Print transaction details
for detail in details:
    print(detail)