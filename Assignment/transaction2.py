# Mrs banjo account balance in GTB is 100,000, the bank decided to be removing 2000 from her account every day this action should continue while her balance is > 5000.
#Write a python function code that will show the transaction details

def transaction_details(initial_balance, daily_deduction):
    balance = initial_balance
    transactions = []  # List to hold transaction details
    day = 0  # To keep track of the number of days

    while balance > 5000:
        transactions.append(f"Day {day}: Current balance: {balance}")
        balance -= daily_deduction  # Deduct the daily amount
        transactions.append(f"Day {day}: New balance after deduction: {balance}")
        day += 1

    transactions.append("Final balance reached or dropped below 5,000.")
    return transactions

initial_balance = 100000
daily_deduction = 2000
details = transaction_details(initial_balance, daily_deduction)

# Print transaction details
for detail in details:
    print(detail)