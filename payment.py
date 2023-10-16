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

# Main program
if __name__ == "__main__":
    # Set the ticket price (you can replace this with actual ticket pricing)
    ticket_price = 20.0

    print("Bus Tracking System - Payment Module")
    print(f"Ticket Price: ${ticket_price:.2f}")
    
    if make_payment(ticket_price):
        print("Thank you for your payment.")
    else:
        print("Payment failed. Please try again.")
