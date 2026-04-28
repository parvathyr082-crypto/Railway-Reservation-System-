seats = 50
bookings = {}

def check_availability():
    print("Available seats:", seats)

def book_ticket():
    global seats
    if seats <= 0:
        print("No seats available!")
        return

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    
    booking_id = len(bookings) + 1
    seat_number = 51 - seats

    bookings[booking_id] = {
        "name": name,
        "age": age,
        "seat": seat_number
    }

    seats -= 1
    print("Ticket booked! Your Booking ID:", booking_id)

def view_ticket():
    bid = int(input("Enter Booking ID: "))
    if bid in bookings:
        print(bookings[bid])
    else:
        print("Booking not found!")

def cancel_ticket():
    global seats
    bid = int(input("Enter Booking ID to cancel: "))
    
    if bid in bookings:
        del bookings[bid]
        seats += 1
        print("Ticket cancelled!")
    else:
        print("Invalid Booking ID!")

while True:
    print("\n1. Check Availability")
    print("2. Book Ticket")
    print("3. View Ticket")
    print("4. Cancel Ticket")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        check_availability()
    elif choice == 2:
        book_ticket()
    elif choice == 3:
        view_ticket()
    elif choice == 4:
        cancel_ticket()
    elif choice == 5:
        break
    else:
        print("Invalid choice!")
