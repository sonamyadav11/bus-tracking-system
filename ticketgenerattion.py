import random

# Dictionary to store ticket information
tickets = {}

# Function to generate a random ticket number
def generate_ticket_number():
    return ''.join(random.choice('0123456789ABCDEF') for i in range(8))

# Function to create and store a ticket
def generate_ticket(passenger_name, source, destination, departure_time):
    ticket_number = generate_ticket_number()
    ticket = {
        'passenger_name': passenger_name,
        'source': source,
        'destination': destination,
        'departure_time': departure_time
    }
    tickets[ticket_number] = ticket
    return ticket_number

# Function to display a ticket
def display_ticket(ticket_number):
    if ticket_number in tickets:
        ticket = tickets[ticket_number]
        print("Ticket Number:", ticket_number)
        print("Passenger Name:", ticket['passenger_name'])
        print("Source:", ticket['source'])
        print("Destination:", ticket['destination'])
        print("Departure Time:", ticket['departure_time'])
    else:
        print("Ticket not found.")

# Main program
if __name__ == "__main__":
    while True:
        print("Bus Tracking System - Ticket Generation")
        print("1. Generate Ticket")
        print("2. Display Ticket")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            passenger_name = input("Enter passenger name: ")
            source = input("Enter source location: ")
            destination = input("Enter destination location: ")
            departure_time = input("Enter departure time: ")
            ticket_number = generate_ticket(passenger_name, source, destination, departure_time)
            print("Ticket generated. Ticket number:", ticket_number)

        elif choice == "2":
            ticket_number = input("Enter ticket number: ")
            display_ticket(ticket_number)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")
