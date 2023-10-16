# Function to simulate a payment process
def make_payment(ticket_price):
    while True:
        try:
            payment_amount = float(input("Enter payment amount: $"))
            if payment_amount < ticket_price:
                print("Insufficient payment. Please enter at least the ticket price.")
            else:
                change = payment_amount - ticket_price
                print("Payment successful.")
                print(f"Change: ${change:.2f}")
                return True
        except ValueError:
            print("Invalid input. Please enter a valid payment amount.")

# Function to simulate a login (replace with actual authentication logic)
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    # Replace with your authentication logic
    if username == "user" and password == "password":
        return True
    else:
        return False

# Function to generate a ticket
def generate_ticket():
    passenger_name = input("Enter passenger name: ")
    source = input("Enter source location: ")
    destination = input("Enter destination location: ")
    departure_time = input("Enter departure time: ")
    return {
        'passenger_name': passenger_name,
        'source': source,
        'destination': destination,
        'departure_time': departure_time
    }

# Main program
if __name__ == "__main__":
    ticket_price = 20.0
    logged_in = False

    while True:
        print("Bus Tracking System")
        print("1. Log In")
        print("2. Generate Ticket")
        print("3. Make Payment")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            if logged_in:
                print("You are already logged in.")
            else:
                if login():
                    print("Login successful.")
                    logged_in = True
                else:
                    print("Login failed. Please try again.")

        elif choice == "2":
            if not logged_in:
                print("Please log in first.")
            else:
                ticket = generate_ticket()
                print("Ticket generated:")
                for key, value in ticket.items():
                    print(f"{key}: {value}")

        elif choice == "3":
            if not logged_in:
                print("Please log in first.")
            else:
                print(f"Ticket Price: ${ticket_price:.2f}")
                if make_payment(ticket_price):
                    print("Thank you for your payment.")
                else:
                    print("Payment failed. Please try again.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select
