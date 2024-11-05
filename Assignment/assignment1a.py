# Function to collect user details
def collect_user_details():
    name = input("Please enter your name: ")
    designation = input("Please enter your designation: ")
    email = input("Please enter your email address: ")
    phone_number = input("Please enter your phone number: ")

    # Print the collected details
    print("\ngeeCollected Details:")
    print(f"Name: {name}")
    print(f"Designation: {designation}")
    print(f"Email: {email}")
    print(f"Phone Number: {phone_number}")

# Call the function
collect_user_details()