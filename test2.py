# system.py
# Hostel Guest Room Reservation System (Full project with Tkinter GUI)
# Student ID used as Booking ID. Beginner-friendly code.

import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

BOOKING_FILE = r"C:\Users\ASUS\OneDrive\Desktop\Python\bookings.txt"

# ---------------------------
# MODULE 1: File Handling & Database
# ---------------------------
def load_bookings():
    bookings = []
    if not os.path.exists(BOOKING_FILE):
        return bookings
    try:
        f = open(BOOKING_FILE, "r")
        for line in f:
            data = line.strip().split(",")
            # Expect: student_id,guest_name,relation,room_no,days,status
            if len(data) == 6:
                bookings.append({
                    "student_id": data[0],
                    "guest_name": data[1],
                    "relation": data[2],
                    "room_no": data[3],
                    "days": data[4],
                    "status": data[5]
                })
        f.close()
    except Exception as e:
        print("Error reading file:", e)
    return bookings

def save_bookings(bookings):
    try:
        f = open(BOOKING_FILE, "w")
        for b in bookings:
            line = ",".join([b["student_id"], b["guest_name"], b["relation"],
                             b["room_no"], b["days"], b["status"]]) + "\n"
            f.write(line)
        f.close()
    except Exception as e:
        print("Error writing file:", e)

# ---------------------------
# MODULE 3: Room Allocation
# ---------------------------
def allocate_room(bookings):
    all_rooms = [str(i) for i in range(101, 121)]
    booked = [b["room_no"] for b in bookings]
    for r in all_rooms:
        if r not in booked:
            return r
    return "-1"

# ---------------------------
# MODULE 4: Policy Enforcement
# ---------------------------
def policy_check(relation, days):
    if relation.lower() not in ["father", "mother", "guardian"]:
        messagebox.showwarning("Policy Check", "Only Father/Mother/Guardian allowed.")
        return False
    if not days.isdigit():
        messagebox.showwarning("Policy Check", "Days must be a number.")
        return False
    if int(days) > 3:
        messagebox.showwarning("Policy Check", "Stay limit exceeded (max 3 days).")
        return False
    return True

# ---------------------------
# MODULE 7: Notifications (simple)
# ---------------------------
def send_notification(action, sid, gname, room):
    # Console print + messagebox simple notification
    print(f"Notification: {action} for {gname} (Student ID {sid}) in Room {room}")
    # You may also show small info dialogs (quietly)
    # messagebox.showinfo(action, f"{action} recorded for {gname} (ID: {sid}) in Room {room}")

# ---------------------------
# MODULE 2: Reservation Management (Add/Update/Cancel/Search)
# ---------------------------
def add_reservation_backend(student_id, guest_name, relation, days):
    bookings = load_bookings()
    # Check duplicate (student_id as booking ID)
    for b in bookings:
        if b["student_id"] == student_id:
            return False, "This student already has an active booking."
    # Policy check
    if not policy_check(relation, days):
        return False, "Policy check failed."

    room = allocate_room(bookings)
    if room == "-1":
        return False, "All rooms are booked."

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
    send_notification("Booking", student_id, guest_name, room)
    return True, f"Booking successful. Room {room} assigned."

def update_reservation_backend(student_id, new_guest_name, new_days):
    bookings = load_bookings()
    for b in bookings:
        if b["student_id"] == student_id:
            if new_guest_name.strip() != "":
                b["guest_name"] = new_guest_name
            if new_days.strip() != "":
                if not new_days.isdigit():
                    return False, "Days must be a number."
                if int(new_days) > 3:
                    return False, "Stay limit exceeded (max 3 days)."
                b["days"] = new_days
            save_bookings(bookings)
            return True, "Reservation updated."
    return False, "Booking not found."

def cancel_reservation_backend(student_id):
    bookings = load_bookings()
    for b in bookings:
        if b["student_id"] == student_id:
            bookings.remove(b)
            save_bookings(bookings)
            send_notification("Cancellation", student_id, b["guest_name"], b["room_no"])
            return True, "Reservation cancelled."
    return False, "Booking not found."

def search_reservation_backend(key):
    bookings = load_bookings()
    result = []
    for b in bookings:
        if b["student_id"] == key or b["guest_name"].lower() == key.lower():
            result.append(b)
    return result

# ---------------------------
# MODULE 5: Check-In / Check-Out
# ---------------------------
def check_in_backend(student_id):
    bookings = load_bookings()
    for b in bookings:
        if b["student_id"] == student_id:
            if b["status"] == "Booked":
                b["status"] = "Checked In"
                save_bookings(bookings)
                send_notification("Check-In", student_id, b["guest_name"], b["room_no"])
                return True, "Checked In successfully."
            else:
                return False, "Guest already checked in or checked out."
    return False, "Booking not found."

def check_out_backend(student_id):
    bookings = load_bookings()
    for b in bookings:
        if b["student_id"] == student_id:
            if b["status"] == "Checked In":
                b["status"] = "Checked Out"
                save_bookings(bookings)
                send_notification("Check-Out", student_id, b["guest_name"], b["room_no"])
                return True, "Checked Out successfully."
            else:
                return False, "Guest is not checked in."
    return False, "Booking not found."

# ---------------------------
# MODULE 6: Sorting & Reporting
# ---------------------------
def generate_report_backend():
    bookings = load_bookings()
    total = len(bookings)
    checked_in = sum(1 for b in bookings if b["status"] == "Checked In")
    checked_out = sum(1 for b in bookings if b["status"] == "Checked Out")
    currently_booked = sum(1 for b in bookings if b["status"] == "Booked")
    return {
        "total": total,
        "checked_in": checked_in,
        "checked_out": checked_out,
        "currently_booked": currently_booked
    }

# ---------------------------
# Helper: clear entries
# ---------------------------
def clear_entries(entries):
    for e in entries:
        e.delete(0, tk.END)

# ---------------------------
# GUI CODE (Module 8)
# ---------------------------
class HostelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hostel Guest Room Reservation System")
        self.root.geometry("900x600")

        # Top frame for form
        form_frame = tk.Frame(root, padx=10, pady=10)
        form_frame.pack(fill=tk.X)

        # Student ID
        tk.Label(form_frame, text="Student ID (Booking ID):").grid(row=0, column=0, sticky=tk.W)
        self.entry_sid = tk.Entry(form_frame)
        self.entry_sid.grid(row=0, column=1, padx=5, pady=3)

        # Guest Name
        tk.Label(form_frame, text="Guest Name:").grid(row=1, column=0, sticky=tk.W)
        self.entry_guest = tk.Entry(form_frame)
        self.entry_guest.grid(row=1, column=1, padx=5, pady=3)

        # Relation
        tk.Label(form_frame, text="Relation:").grid(row=0, column=2, sticky=tk.W)
        self.entry_relation = tk.Entry(form_frame)
        self.entry_relation.grid(row=0, column=3, padx=5, pady=3)

        # Days
        tk.Label(form_frame, text="Days:").grid(row=1, column=2, sticky=tk.W)
        self.entry_days = tk.Entry(form_frame)
        self.entry_days.grid(row=1, column=3, padx=5, pady=3)

        # Buttons frame
        btn_frame = tk.Frame(root, padx=10, pady=5)
        btn_frame.pack(fill=tk.X)

        tk.Button(btn_frame, text="Add Reservation", width=15, command=self.add_reservation).grid(row=0, column=0, padx=4, pady=4)
        tk.Button(btn_frame, text="Update Reservation", width=15, command=self.update_reservation).grid(row=0, column=1, padx=4, pady=4)
        tk.Button(btn_frame, text="Cancel Reservation", width=15, command=self.cancel_reservation).grid(row=0, column=2, padx=4, pady=4)
        tk.Button(btn_frame, text="Search", width=12, command=self.search_reservation).grid(row=0, column=3, padx=4, pady=4)

        tk.Button(btn_frame, text="Check-In", width=12, command=self.check_in).grid(row=1, column=0, padx=4, pady=4)
        tk.Button(btn_frame, text="Check-Out", width=12, command=self.check_out).grid(row=1, column=1, padx=4, pady=4)
        tk.Button(btn_frame, text="Refresh List", width=12, command=self.load_tree).grid(row=1, column=2, padx=4, pady=4)
        tk.Button(btn_frame, text="Daily Report", width=12, command=self.show_report).grid(row=1, column=3, padx=4, pady=4)

        # Treeview frame
        tree_frame = tk.Frame(root, padx=10, pady=10)
        tree_frame.pack(fill=tk.BOTH, expand=True)

        columns = ("student_id", "guest_name", "relation", "room_no", "days", "status")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
        self.tree.heading("student_id", text="Student ID")
        self.tree.heading("guest_name", text="Guest Name")
        self.tree.heading("relation", text="Relation")
        self.tree.heading("room_no", text="Room No")
        self.tree.heading("days", text="Days")
        self.tree.heading("status", text="Status")

        # column widths
        self.tree.column("student_id", width=100)
        self.tree.column("guest_name", width=200)
        self.tree.column("relation", width=100)
        self.tree.column("room_no", width=80)
        self.tree.column("days", width=60)
        self.tree.column("status", width=100)

        # add tree to scrollbar
        vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=vsb.set)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Load initial records
        self.load_tree()

        # Bind double-click to load record into form
        self.tree.bind("<Double-1>", self.on_tree_double)

    # ---------------------------
    # GUI helper functions
    # ---------------------------
    def load_tree(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        bookings = load_bookings()
        # Sort by room number (as number)
        try:
            bookings_sorted = sorted(bookings, key=lambda x: int(x["room_no"]))
        except:
            bookings_sorted = bookings
        for b in bookings_sorted:
            self.tree.insert("", tk.END, values=(b["student_id"], b["guest_name"],
                                                 b["relation"], b["room_no"], b["days"], b["status"]))

    def on_tree_double(self, event):
        item = self.tree.selection()
        if not item:
            return
        values = self.tree.item(item, "values")
        # Fill form fields
        self.entry_sid.delete(0, tk.END)
        self.entry_sid.insert(0, values[0])
        self.entry_guest.delete(0, tk.END)
        self.entry_guest.insert(0, values[1])
        self.entry_relation.delete(0, tk.END)
        self.entry_relation.insert(0, values[2])
        self.entry_days.delete(0, tk.END)
        self.entry_days.insert(0, values[4])

    # ---------------------------
    # GUI actions that call backend
    # ---------------------------
    def add_reservation(self):
        sid = self.entry_sid.get().strip()
        guest = self.entry_guest.get().strip()
        relation = self.entry_relation.get().strip()
        days = self.entry_days.get().strip()
        if sid == "" or guest == "" or relation == "" or days == "":
            messagebox.showwarning("Input Error", "All fields are required.")
            return
        ok, msg = add_reservation_backend(sid, guest, relation, days)
        if ok:
            messagebox.showinfo("Success", msg)
            self.load_tree()
            clear_entries([self.entry_sid, self.entry_guest, self.entry_relation, self.entry_days])
        else:
            messagebox.showerror("Error", msg)

    def update_reservation(self):
        sid = self.entry_sid.get().strip()
        if sid == "":
            messagebox.showwarning("Input Error", "Student ID is required for update.")
            return
        new_guest = self.entry_guest.get().strip()
        new_days = self.entry_days.get().strip()
        ok, msg = update_reservation_backend(sid, new_guest, new_days)
        if ok:
            messagebox.showinfo("Success", msg)
            self.load_tree()
        else:
            messagebox.showerror("Error", msg)

    def cancel_reservation(self):
        sid = self.entry_sid.get().strip()
        if sid == "":
            messagebox.showwarning("Input Error", "Student ID is required to cancel.")
            return
        confirm = messagebox.askyesno("Confirm", f"Are you sure you want to cancel booking for {sid}?")
        if not confirm:
            return
        ok, msg = cancel_reservation_backend(sid)
        if ok:
            messagebox.showinfo("Success", msg)
            self.load_tree()
            clear_entries([self.entry_sid, self.entry_guest, self.entry_relation, self.entry_days])
        else:
            messagebox.showerror("Error", msg)

    def search_reservation(self):
        key = self.entry_sid.get().strip()
        if key == "":
            key = self.entry_guest.get().strip()
        if key == "":
            messagebox.showwarning("Input Error", "Enter Student ID or Guest Name to search.")
            return
        results = search_reservation_backend(key)
        if not results:
            messagebox.showinfo("No Result", "No matching bookings found.")
            return
        # Show results in a simple text box popup
        text = ""
        for b in results:
            text += f"Student ID: {b['student_id']}\nGuest: {b['guest_name']}\nRelation: {b['relation']}\nRoom: {b['room_no']}\nDays: {b['days']}\nStatus: {b['status']}\n\n"
        messagebox.showinfo("Search Results", text)

    def check_in(self):
        sid = self.entry_sid.get().strip()
        if sid == "":
            messagebox.showwarning("Input Error", "Enter Student ID to check-in.")
            return
        ok, msg = check_in_backend(sid)
        if ok:
            messagebox.showinfo("Success", msg)
            self.load_tree()
        else:
            messagebox.showerror("Error", msg)

    def check_out(self):
        sid = self.entry_sid.get().strip()
        if sid == "":
            messagebox.showwarning("Input Error", "Enter Student ID to check-out.")
            return
        ok, msg = check_out_backend(sid)
        if ok:
            messagebox.showinfo("Success", msg)
            self.load_tree()
        else:
            messagebox.showerror("Error", msg)

    def show_report(self):
        r = generate_report_backend()
        text = (f"Total bookings: {r['total']}\n"
                f"Checked In: {r['checked_in']}\n"
                f"Checked Out: {r['checked_out']}\n"
                f"Currently Booked: {r['currently_booked']}")
        messagebox.showinfo("Daily Report", text)

# ---------------------------
# MODULE 9: Testing & Documentation (basic)
# ---------------------------
def test_system():
    # Basic tests: can load and save
    try:
        bookings = load_bookings()
        if isinstance(bookings, list):
            print("Test OK: load_bookings returned list.")
        else:
            print("Test FAIL: load_bookings did not return list.")
    except Exception as e:
        print("Test FAIL:", e)

# ---------------------------
# MAIN
# ---------------------------
if __name__ == "__main__":
    test_system()
    root = tk.Tk()
    app = HostelApp(root)
    root.mainloop()
