🏠 Hostel Guest Room Reservation System (Python | Tkinter | File Handling)

A complete Python-based project designed to manage guest room reservations in a hostel using a clean Tkinter GUI and simple file-storage system.
The system supports booking, updating, cancelling, room allocation, check-in/out, reporting, CSV export, and login authentication.

🚀 Project Features
✔ 1. File Handling & Database
Uses a text file (bookings.txt) as the database
Loads/saves all booking details
Ensures data persistence

✔ 2. Reservation Management
Add new reservations
Update and cancel bookings
Search using Student ID or Guest Name
Student ID acts as Booking ID

✔ 3. Room Allocation
Automatically assigns rooms from 101–120
Prevents duplicate room assignments

✔ 4. Policy Enforcement
Only Father/Mother/Guardian allowed
Maximum stay: 3 days
Validates input to maintain hostel rules

✔ 5. Check-In / Check-Out Module
Updates status: Booked → Checked In → Checked Out
Real-time updates in GUI table

✔ 6. Reporting & CSV Export
Displays total booked, checked-in, checked-out
Exports complete records to report.csv

✔ 7. Tkinter-Based GUI
Header, footer, menu bar
Buttons for all operations
Treeview table for data display
User-friendly and easy to navigate

✔ 8. Login Authentication
Simple login screen for security
Username: admin
Password: 1234

📁 Project Structure
Hostel-Guest-Room-System/
│── test2.py
│── bookings.txt   (auto-generated)
│── report.csv     (exported)
│── README.md

🛠️ Technologies & Libraries
This project uses only Python standard libraries, no installation required:
tkinter – GUI development
os – file path and existence checks
csv – exporting reports
ttk – Treeview data table
messagebox – user notifications

📸 Screenshots (Optional)

You can add screenshots here:
Login Screen
<img width="583" height="441" alt="image" src="https://github.com/user-attachments/assets/aa716165-3a50-4a01-8476-42ae6d1d4dec" />

Main Interface
<img width="940" height="641" alt="image" src="https://github.com/user-attachments/assets/8ab7795e-017d-4ae7-9ffb-2a63193e0c05" />

Data Table
<img width="940" height="643" alt="image" src="https://github.com/user-attachments/assets/59cd61f4-96bd-4dc3-b69f-5e18ca0d7442" />

Report

<img width="341" height="333" alt="image" src="https://github.com/user-attachments/assets/772cd5c1-8484-4185-979b-a62f2eea3d32" />

🔧 How to Run
Install Python 3.x
Download or clone the repository

Run:
python test2.py

Login using:
Username: admin
Password: 1234

🧪 Testing & Validation
All modules have been tested:
Test	Status
File handling	✔ Pass
Reservation add/update/cancel	✔ Pass
Room allocation	✔ Pass
Check-in/check-out	✔ Pass
Validation	✔ Pass
CSV export	✔ Pass
GUI operations	✔ Pass
Login authentication	✔ Pass
📦 Project Deliverables
Fully working GUI-based reservation system
File-handling backend
Room allocation logic
Visitor policy enforcement
Check-in/check-out workflow
Exportable reports
Complete documentation

📄 Key Outcomes
Fully functional hostel guest management system
Real-time status updates
Clean and accessible user interface
Secure login-based access
Complete module integration

🔮 Future Scope
Add SQL or SQLite database
Multi-user roles (warden/admin/security)
SMS or email notifications
Detailed analytics dashboard
Multi-day booking history
Cloud-based deployment

👨‍💻 Developer

Ajeet Singh Panwar
📧 Email: ajeetspanwar985@gmail.com

🛠 Developed using Python 3 & Tkinter
