# 🏠 Hostel Guest Room Reservation System (Python Project)

A modular Python-based project that automates hostel guest room bookings for parents and guardians visiting students.  
Currently implemented as a **console-based system**, this project will later include a **GUI interface** and additional advanced modules.

---

## 📌 Project Overview

Many hostels still maintain guest room records manually using paper registers, leading to confusion, double bookings, and time delays.  
This project aims to digitalize the entire process using **Python** and **file handling**, creating a simple yet efficient system to manage room reservations.

It allows hostel staff to:
- Add, update, or cancel guest bookings  
- Allocate available rooms automatically  
- Track check-ins and check-outs  
- Maintain a digital record of all visitors  

All records are stored in a lightweight **text file (`bookings.txt`)** that functions as the system’s database.

---

## 🧩 Modules Implemented (Current Phase)

| Module No. | Module Name | Description |
|-------------|--------------|--------------|
| **1** | File Handling & Database | Stores and retrieves booking records from a text file |
| **2** | Reservation Management | Add, update, cancel, and search guest bookings |
| **3** | Room Allocation | Automatically assigns available rooms (101–120) |
| **4** | Check-In / Check-Out System | Marks guests as arrived or departed |
| **5** | User Interface & Integration | Simple menu-based console interface connecting all modules |

---

## 🧩 Modules Planned (Next Phase)

| Module No. | Module Name | Description |
|-------------|--------------|--------------|
| **6** | Policy Enforcement | Apply hostel rules like stay limits and relation checks |
| **7** | Sorting & Reporting | Generate daily/monthly visitor and room usage reports |
| **8** | Notifications & Receipts | Add digital receipts or QR confirmations |
| **9** | Testing & Documentation | Detailed testing scripts and user documentation |
| **GUI (Tkinter)** | User Interface Upgrade | Replace console with GUI for real-world usability |

---

## ⚙️ Technologies Used

- **Language:** Python  
- **Concepts:** File Handling, Conditional Statements, Loops, Functions  
- **Data Storage:** Text file (`bookings.txt`)  
- **Planned Extensions:** GUI (Tkinter), Database (MySQL or SQLite)

---

## 🚀 How to Run the Project

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/Hostel-Guest-Room-Reservation-System.git

2. Move into the project folder:
cd Hostel-Guest-Room-Reservation-System


3. Run the program:
python system.py


Follow the menu options to:

Add / Update / Cancel Reservations

Check-In or Check-Out Guests

Search Records or View All Bookings

🧠 Learning Outcomes

Understanding Python file handling and data management

Building modular programs for scalability

Learning how to simulate a database using text files

Foundation for integrating GUI and DBMS

Problem-solving and logical structuring for real-world use cases

🌱 Future Scope

This system will later be upgraded with:

A Tkinter GUI interface for user-friendly booking management

Database connectivity using SQLite or MySQL

Automated reports for visitor tracking and analytics

Email/SMS notifications for booking confirmations

QR code receipts for contactless guest entry

These improvements will make the project suitable for real hostel environments and digital campus initiatives.

Project Structure
Hostel-Guest-Room-Reservation-System/
│
├── test.py # Main program file
├── bookings.txt # Text database
├── README.md # Project description 

Output Sample
===== HOSTEL GUEST ROOM RESERVATION SYSTEM =====
1. Add Reservation
2. Update Reservation
3. Cancel Reservation
4. Search Reservation
5. Check-In Guest
6. Check-Out Guest
7. View All Bookings
8. Exit
Enter your choice: 1

--- Add New Reservation ---
Enter Student ID: 220022
Enter Guest Name: Piyush
Enter Relation (Father/Mother/Guardian): Father
Enter number of stay days: 4

 Booking Successful!
Booking ID (Student ID): 220022
Guest: Piyush
Room Assigned: 101
----------------------------

👨‍💻 Author

Name: Ajeet Singh Panwar 
Email: ajeetspanwar985@gmail.com

🪪 License

This project is open-source under the MIT License
.

