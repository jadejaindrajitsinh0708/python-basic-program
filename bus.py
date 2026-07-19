total_seats = 20
ticket_price = 150

while True:
    print("\n===== BUS TICKET BOOKING SYSTEM =====")
    print("1. Book Ticket")
    print("2. Check Available Seats")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter Passenger Name: ")

        seat = input("How many tickets do you want? ")

        if not seat.isdigit():
            print("❌ Please enter numbers only.")
            continue

        seat = int(seat)

        if seat <= 0:
            print("❌ Invalid number of tickets.")
            continue

        if seat > total_seats:
            print("❌ Sorry! Only", total_seats, "seats are available.")
            continue

        total = seat * ticket_price

        total_seats -= seat

        print("\n===== TICKET CONFIRMED =====")
        print("Passenger :", name)
        print("Tickets   :", seat)
        print("Price     : ₹", ticket_price)
        print("Total Bill: ₹", total)
        print("Seats Left:", total_seats)

    elif choice == "2":
        print("Available Seats :", total_seats)

    elif choice == "3":
        print("Thank You! Visit Again.")
        break

    else:
        print("❌ Invalid Choice")