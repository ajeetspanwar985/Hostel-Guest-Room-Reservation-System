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
| **5** | Check-In / Check-Out System | Marks guests as arrived or departed |
| **8** | User Interface & Integration | Simple menu-based console interface connecting all modules |

---

## 🧩 Modules Planned (Next Phase)

| Module No. | Module Name | Description |
|-------------|--------------|--------------|
| **4** | Policy Enforcement | Apply hostel rules like stay limits and relation checks |
| **6** | Sorting & Reporting | Generate daily/monthly visitor and room usage reports |
| **7** | Notifications & Receipts | Add digital receipts or QR confirmations |
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

