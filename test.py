BOOKING_FILE = "bookings.txt"   
def load_bookings():
    """Read all bookings from file"""
    bookings = []
    try:
        f = open(BOOKING_FILE, "r")
        for line in f:
            data = line.strip().split(",")
            if len(data) == 6:
                record = {
                    "student_id": data[0],      
                    "guest_name": data[1],
                    "relation": data[2],
                    "room_no": data[3],
                    "days": data[4],
                    "status": data[5]
                }
                bookings.append(record)
        f.close()
    except FileNotFoundError:
        bookings = []
    return bookings

def save_bookings(bookings):
    """Save all bookings back to file"""
    f = open(BOOKING_FILE, "w")
    for b in bookings:
        line = b["student_id"] + "," + b["guest_name"] + "," + b["relation"] + "," + b["room_no"] + "," + b["days"] + "," + b["status"] + "\n"
        f.write(line)
    f.close()

def add_reservation(bookings):
    print("\n--- Add New Reservation ---")
    student_id = input("Enter Student ID: ")
    for b in bookings:
        if b["student_id"] == student_id:
            print("This student already has an active booking.\n")
            return

    guest_name = input("Enter Guest Name: ")
    relation = input("Enter Relation (Father/Mother/Guardian): ")
    days = input("Enter number of stay days: ")

    room_no = allocate_room(bookings)
    if room_no == "-1":
        print("Sorry, all rooms are booked.\n")
        return

    record = {
        "student_id": student_id,
        "guest_name": guest_name,
        "relation": relation,
        "room_no": room_no,
        "days": days,
        "status": "Booked"
    }

    bookings.append(record)
    save_bookings(bookings)
    print("\n Booking Successful!")
    print("Booking ID (Student ID):", student_id)
    print("Guest:", guest_name)
    print("Room Assigned:", room_no)
    print("----------------------------\n")


def update_reservation(bookings):
    print("\n--- Update Reservation ---")
    student_id = input("Enter Student ID (Booking ID): ")
    found = False
    for b in bookings:
        if b["student_id"] == student_id:
            print("Current Guest Name:", b["guest_name"])
            new_name = input("Enter new Guest Name (press Enter to skip): ")
            if new_name != "":
                b["guest_name"] = new_name
            new_days = input("Enter new number of stay days (press Enter to skip): ")
            if new_days != "":
                b["days"] = new_days
            found = True
            break
    if found:
        save_bookings(bookings)
        print("Reservation updated.\n")
    else:
        print("Booking not found.\n")


def cancel_reservation(bookings):
    print("\n--- Cancel Reservation ---")
    student_id = input("Enter Student ID (Booking ID) to cancel: ")
    found = False
    for b in bookings:
        if b["student_id"] == student_id:
            bookings.remove(b)
            found = True
            break
    if found:
        save_bookings(bookings)
        print("Reservation cancelled successfully.\n")
    else:
        print("Booking not found.\n")


def search_reservation(bookings):
    print("\n--- Search Reservation ---")
    key = input("Enter Student ID or Guest Name: ")
    found = False
    for b in bookings:
        if b["student_id"] == key or b["guest_name"].lower() == key.lower():
            print("\nBooking ID (Student ID):", b["student_id"])
            print("Guest:", b["guest_name"])
            print("Relation:", b["relation"])
            print("Room:", b["room_no"])
            print("Days:", b["days"])
            print("Status:", b["status"])
            print("--------------------------")
            found = True
    if found == False:
        print(" No record found.\n")

def allocate_room(bookings):
    """Assign the first available room between 101–120"""
    all_rooms = []
    for i in range(101, 121):
        all_rooms.append(str(i))

    booked_rooms = []
    for b in bookings:
        booked_rooms.append(b["room_no"])

    for r in all_rooms:
        if r not in booked_rooms:
            return r
    return "-1"  

def check_in(bookings):
    print("\n--- Check-In Guest ---")
    student_id = input("Enter Student ID (Booking ID): ")
    found = False
    for b in bookings:
        if b["student_id"] == student_id:
            if b["status"] == "Booked":
                b["status"] = "Checked In"
                found = True
                print("Guest checked in successfully!\n")
            else:
                print(" Already checked in or checked out.\n")
            break
    if found:
        save_bookings(bookings)
    else:
        print("Booking not found.\n")


def check_out(bookings):
    print("\n--- Check-Out Guest ---")
    student_id = input("Enter Student ID (Booking ID): ")
    found = False
    for b in bookings:
        if b["student_id"] == student_id:
            if b["status"] == "Checked In":
                b["status"] = "Checked Out"
                found = True
                print("Guest checked out successfully!\n")
            else:
                print("Cannot check out. Guest not currently checked in.\n")
            break
    if found:
        save_bookings(bookings)
    else:
        print("Booking not found.\n")

def view_all(bookings):
    """Show all bookings"""
    print("\n--- All Current Bookings ---")
    if len(bookings) == 0:
        print("No bookings yet.\n")
    else:
        for b in bookings:
            print("Booking ID (Student ID):", b["student_id"])
            print("Guest:", b["guest_name"])
            print("Relation:", b["relation"])
            print("Room:", b["room_no"])
            print("Days:", b["days"])
            print("Status:", b["status"])
            print("-----------------------------")
    print()


def main_menu():
    """Main text-based interface (GUI can connect later)"""
    while True:
        print("===== HOSTEL GUEST ROOM RESERVATION SYSTEM =====")
        print("1. Add Reservation")
        print("2. Update Reservation")
        print("3. Cancel Reservation")
        print("4. Search Reservation")
        print("5. Check-In Guest")
        print("6. Check-Out Guest")
        print("7. View All Bookings")
        print("8. Exit")

        choice = input("Enter your choice: ")
        bookings = load_bookings()

        if choice == "1":
            add_reservation(bookings)
        elif choice == "2":
            update_reservation(bookings)
        elif choice == "3":
            cancel_reservation(bookings)
        elif choice == "4":
            search_reservation(bookings)
        elif choice == "5":
            check_in(bookings)
        elif choice == "6":
            check_out(bookings)
        elif choice == "7":
            view_all(bookings)
        elif choice == "8":
            print("Exiting system. Thank you!")
            break
        else:
            print("Invalid choice. Try again.\n")
print("Starting Hostel Guest Room Reservation System...\n")
main_menu()
