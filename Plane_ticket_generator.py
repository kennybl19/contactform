import tkinter as tk
from tkinter import ttk, messagebox
import random

# ---------------- Function to generate ticket ----------------
def generate_ticket():
    passenger = entry_name.get().strip()
    age = entry_age.get().strip()
    source = combo_source.get()
    destination = combo_destination.get()

    # Validate input
    if not passenger or not age or not source or not destination:
        messagebox.showerror("Error", "Please fill all fields!")
        return

    try:
        age = int(age)
        if age <= 0:
            raise ValueError
    except:
        messagebox.showerror("Error", "Age must be a positive number!")
        return

    if source == destination:
        messagebox.showerror("Error", "Source and destination cannot be the same!")
        return

    # Generate random seat and price
    seat_no = f"{random.randint(1, 50)}{random.choice('ABCDEF')}"
    price = random.randint(15000, 50000)  # price in local currency

    # Create ticket text
    ticket_text = f"""
    🛫 Plane Ticket
    ----------------------------
    Passenger: {passenger}
    Age: {age} years
    From: {source}
    To: {destination}
    Seat No: {seat_no}
    Price: ${price}
    ----------------------------
    Have a safe flight!
    """

    # Display ticket
    text_ticket.config(state='normal')
    text_ticket.delete(1.0, tk.END)
    text_ticket.insert(tk.END, ticket_text)
    text_ticket.config(state='disabled')

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("Plane Ticket Generator")
root.geometry("450x500")
root.resizable(False, False)

tk.Label(root, text="Plane Ticket Generator", font=("Arial", 16, "bold")).pack(pady=10)

# Passenger Name
tk.Label(root, text="Passenger Name:").pack()
entry_name = tk.Entry(root, font=("Arial", 12))
entry_name.pack(pady=5)

# Passenger Age
tk.Label(root, text="Age:").pack()
entry_age = tk.Entry(root, font=("Arial", 12))
entry_age.pack(pady=5)

# Source & Destination
tk.Label(root, text="Source:").pack()
combo_source = ttk.Combobox(root, values=["Lagos", "Abuja", "Kano", "Port Harcourt"])
combo_source.current(0)
combo_source.pack(pady=5)

tk.Label(root, text="Destination:").pack()
combo_destination = ttk.Combobox(root, values=["Lagos", "Abuja", "Kano", "Port Harcourt"])
combo_destination.current(1)
combo_destination.pack(pady=5)

# Generate Ticket Button
tk.Button(root, text="Generate Ticket", font=("Arial", 14), command=generate_ticket).pack(pady=10)

# Ticket Display
text_ticket = tk.Text(root, height=12, width=50, font=("Courier", 12), state='disabled')
text_ticket.pack(pady=10)

root.mainloop()
