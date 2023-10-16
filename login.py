# User data dictionary (in-memory storage, replace with a database in a real system)
user_data = {}

# Function for user registration
def register_user(username, password):
    if username in user_data:
        return "User already exists. Please log in."
    user_data[username] = password
    return "Registration successful. You can now log in."

# Function for user login
def login_user(username, password):
    if username in user_data and user_data[username] == password:
        return "Login successful. Welcome, " + username + "!"
    return "Login failed. Please check your credentials."
import re
import datetime

# Function to validate the time format
def is_valid_time(time_str):
    try:
        datetime.datetime.strptime(time_str, '%H:%M')
        return True
    except ValueError:
        return False

# Inside the choice "1" block
departure_time = input("Enter departure time (HH:MM): ")
if not is_valid_time(departure_time):
    print("Invalid time format. Please enter in HH:MM format.")
    continue

# Main program
if __name__ == "__main__":
    while True:
        print("Welcome to the Bus Tracking System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            registration_result = register_user(username, password)
            print(registration_result)

        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            login_result = login_user(username, password)
            print(login_result)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")
