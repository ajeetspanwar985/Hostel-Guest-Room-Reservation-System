# Hostel Guest Room Reservation System
# Developed by team: CodeBlooded

import os
import csv
import tkinter as tk
from tkinter import ttk, messagebox

# Set custom destination for booking file
BOOKING_FILE = r"C:\Users\ASUS\OneDrive\Desktop\Python\PBL pyhton\bookings.txt"

# MODULE 1: File Handling & Database
def load_bookings():
    bookings = []
    if not os.path.exists(BOOKING_FILE):
        return bookings
    try:
        with open(BOOKING_FILE, "r") as f:
            for line in f:
                data = line.strip().split(",")
                if len(data) == 6:
                    bookings.append({
                        "student_id": data[0],
                        "guest_name": data[1],
                        "relation": data[2],
                        "room_no": data[3],
                        "days": data[4],
                        "status": data[5]
                    })
    except Exception as e:
        print("Error loading file:", e)
    return bookings
def save_bookings(bookings):
    try:
        with open(BOOKING_FILE, "w") as f:
            for b in bookings:
                f.write(",".join([
                    b["student_id"], b["guest_name"], b["relation"],
                    b["room_no"], b["days"], b["status"]
                ]) + "\n")
    except Exception as e:
        print("Error saving file:", e)

# MODULE 3: Room Allocation
def allocate_room(bookings):
    all_rooms = [str(i) for i in range(101, 121)]
    booked = [b["room_no"] for b in bookings]
    for r in all_rooms:
        if r not in booked:
            return r
    return "-1"

# MODULE 4: Policy Enforcement
def policy_check(relation, days):
    if relation.lower() not in ["father", "mother", "guardian"]:
        messagebox.showwarning("Policy Check", "Only Father, Mother, or Guardian allowed.")
        return False
    if not days.isdigit():
        messagebox.showwarning("Policy Check", "Days must be a number.")
        return False
    if int(days) > 3:
        messagebox.showwarning("Policy Check", "Stay limit exceeded (max 3 days).")
        return False
    return True

# MODULE 2: Reservation Management
def add_reservation_backend(student_id, guest_name, relation, days):
    bookings = load_bookings()
    for b in bookings:
        if b["student_id"] == student_id:
            return False, "This student already has a booking."

    if not policy_check(relation, days):
        return False, "Policy check failed."

    room = allocate_room(bookings)
    if room == "-1":
        return False, "No rooms available."

    record = {
        "student_id": student_id,
        "guest_name": guest_name,
        "relation": relation,
        "room_no": room,
        "days": days,
        "status": "Booked"
    }
    bookings.append(record)
    save_bookings(bookings)
    return True, f"Booking successful! Room {room} assigned."
def cancel_reservation_backend(student_id):
    bookings = load_bookings()
    for b in bookings:
        if b["student_id"] == student_id:
            bookings.remove(b)
            save_bookings(bookings)
            return True, "Booking cancelled."
    return False, "Booking not found."
def update_reservation_backend(student_id, new_guest_name, new_days):
    bookings = load_bookings()
    for b in bookings:
        if b["student_id"] == student_id:
            if new_guest_name:
                b["guest_name"] = new_guest_name
            if new_days:
                if not new_days.isdigit() or int(new_days) > 3:
                    return False, "Invalid stay duration."
                b["days"] = new_days
            save_bookings(bookings)
            return True, "Booking updated successfully."
    return False, "Booking not found."

# MODULE 5: Check-In / Check-Out
def check_in_backend(student_id):
    bookings = load_bookings()
    for b in bookings:
        if b["student_id"] == student_id:
            if b["status"] == "Booked":
                b["status"] = "Checked In"
                save_bookings(bookings)
                return True, "Checked in successfully."
            else:
                return False, "Already checked in or out."
    return False, "Booking not found."
def check_out_backend(student_id):
    bookings = load_bookings()
    for b in bookings:
        if b["student_id"] == student_id:
            if b["status"] == "Checked In":
                b["status"] = "Checked Out"
                save_bookings(bookings)
                return True, "Checked out successfully."
            else:
                return False, "Not currently checked in."
    return False, "Booking not found."

# MODULE 6: Reporting
def generate_report_backend():
    bookings = load_bookings()
    return {
        "total": len(bookings),
        "checked_in": sum(1 for b in bookings if b["status"] == "Checked In"),
        "checked_out": sum(1 for b in bookings if b["status"] == "Checked Out"),
        "booked": sum(1 for b in bookings if b["status"] == "Booked")
    }
def export_report_csv():
    bookings = load_bookings()
    if not bookings:
        messagebox.showinfo("Export", "No data to export.")
        return
    with open(r"C:\Users\ASUS\OneDrive\Desktop\Python\PBL python\report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Student ID", "Guest Name", "Relation", "Room No", "Days", "Status"])
        for b in bookings:
            writer.writerow([b["student_id"], b["guest_name"], b["relation"], b["room_no"], b["days"], b["status"]])
    messagebox.showinfo("Export", "Report saved to report.csv")

# MODULE 8: GUI Interface
class HostelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hostel Guest Room Reservation System")
        self.root.geometry("950x600")
        self.root.configure(bg="#F5F5F5")

        # Header
        header = tk.Label(root, text="🏠 Hostel Guest Room Reservation System", 
                          font=("Arial", 18, "bold"), bg="#2F4F4F", fg="white", pady=10)
        header.pack(fill=tk.X)

        # Menu Bar
        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Export CSV", command=export_report_csv)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About Project", command=lambda: messagebox.showinfo("About", 
                "Hostel Guest Room Reservation System\nDeveloped by Ajeet S. Panwar\nEmail: ajeetspanwar985@gmail.com"))
        menu_bar.add_cascade(label="Help", menu=help_menu)

        # Form Frame
        form = tk.Frame(root, bg="#F5F5F5")
        form.pack(pady=10)

        tk.Label(form, text="Student ID:", bg="#F5F5F5").grid(row=0, column=0, padx=5, pady=5)
        self.sid = tk.Entry(form); self.sid.grid(row=0, column=1)

        tk.Label(form, text="Guest Name:", bg="#F5F5F5").grid(row=0, column=2, padx=5, pady=5)
        self.gname = tk.Entry(form); self.gname.grid(row=0, column=3)

        tk.Label(form, text="Relation:", bg="#F5F5F5").grid(row=1, column=0, padx=5, pady=5)
        self.relation = tk.Entry(form); self.relation.grid(row=1, column=1)

        tk.Label(form, text="Days:", bg="#F5F5F5").grid(row=1, column=2, padx=5, pady=5)
        self.days = tk.Entry(form); self.days.grid(row=1, column=3)

        # Buttons
        btn_frame = tk.Frame(root, bg="#F5F5F5")
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="Add", width=10, bg="#4CAF50", fg="white", command=self.add).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Update", width=10, bg="#2196F3", fg="white", command=self.update).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Cancel", width=10, bg="#f44336", fg="white", command=self.cancel).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Check-In", width=10, bg="#008CBA", fg="white", command=self.check_in).grid(row=0, column=3, padx=5)
        tk.Button(btn_frame, text="Check-Out", width=10, bg="#FFA500", fg="white", command=self.check_out).grid(row=0, column=4, padx=5)
        tk.Button(btn_frame, text="Report", width=10, command=self.report).grid(row=0, column=5, padx=5)

        # Treeview Table
        cols = ("Student ID", "Guest Name", "Relation", "Room", "Days", "Status")
        self.tree = ttk.Treeview(root, columns=cols, show="headings")
        for c in cols:
            self.tree.heading(c, text=c)
            self.tree.column(c, anchor="center", width=120)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.load_data()

        # Footer
        footer = tk.Label(root, text="Developed by CodeBlooded | Python Project", 
                          bg="#F5F5F5", fg="#555", font=("Arial", 9))
        footer.pack(side=tk.BOTTOM, fill=tk.X)

    # GUI Functions
    def load_data(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for b in load_bookings():
            self.tree.insert("", tk.END, values=(b["student_id"], b["guest_name"], b["relation"], b["room_no"], b["days"], b["status"]))

    def add(self):
        ok, msg = add_reservation_backend(self.sid.get(), self.gname.get(), self.relation.get(), self.days.get())
        messagebox.showinfo("Info" if ok else "Error", msg)
        self.load_data()

    def cancel(self):
        ok, msg = cancel_reservation_backend(self.sid.get())
        messagebox.showinfo("Info" if ok else "Error", msg)
        self.load_data()

    def update(self):
        ok, msg = update_reservation_backend(self.sid.get(), self.gname.get(), self.days.get())
        messagebox.showinfo("Info" if ok else "Error", msg)
        self.load_data()

    def check_in(self):
        ok, msg = check_in_backend(self.sid.get())
        messagebox.showinfo("Info" if ok else "Error", msg)
        self.load_data()

    def check_out(self):
        ok, msg = check_out_backend(self.sid.get())
        messagebox.showinfo("Info" if ok else "Error", msg)
        self.load_data()

    def report(self):
        r = generate_report_backend()
        msg = f"Total: {r['total']}\nBooked: {r['booked']}\nChecked In: {r['checked_in']}\nChecked Out: {r['checked_out']}"
        messagebox.showinfo("Report", msg)


# MODULE 9: Login + Main
def login_window():
    login = tk.Tk()
    login.title("Login")
    login.geometry("300x200")

    tk.Label(login, text="Username:").pack(pady=5)
    user = tk.Entry(login); user.pack()
    tk.Label(login, text="Password:").pack(pady=5)
    pwd = tk.Entry(login, show="*"); pwd.pack()

    def check_login():
        if user.get() == "admin" and pwd.get() == "1234":
            login.destroy()
            root = tk.Tk()
            HostelApp(root)
            root.mainloop()
        else:
            messagebox.showerror("Error", "Invalid credentials.")

    tk.Button(login, text="Login", command=check_login, bg="#4CAF50", fg="white").pack(pady=10)
    login.mainloop()

# Run Program
if __name__ == "__main__":
    login_window()
