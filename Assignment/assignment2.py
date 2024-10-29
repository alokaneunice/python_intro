def calculate_sum():
    # Step 2: Prompt User Input for the first number
    first_number = input("Enter the first number: ")
    
    # Step 3: Handle User Input and convert to numeric type
    first_number = int(first_number)
    
    # Step 4: Prompt User Input for the second number
    second_number = input("Enter the second number: ")
    
    # Step 3: Handle User Input and convert to numeric type
    second_number = int(second_number)
    
    # Step 5: Calculate the Sum
    total_sum = first_number + second_number
    
    # Step 6: Check for Large Sum
    if total_sum > 100:
        print(f"The sum is {total_sum}, which is large!")
    else:
        print(f"The sum is {total_sum}.")
    
# Step 8: Call the Function
calculate_sum()