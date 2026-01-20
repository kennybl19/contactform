import tkinter as tk
from tkinter import ttk, messagebox
import random

# Function to generate ticket
def generate_ticket():
    name = entry_name.get()
    age = entry_age.get()
    source = combo_source.get()
    destination = combo_destination.get()

    if not name or not age or not source or not destination:
        messagebox.showerror("Error", "Please fill all fields!")
        return

    try:
        age = int(age)
    except:
        messagebox.showerror("Error", "Age must be a number!")
        return

    if source == destination:
        messagebox.showerror("Error", "Source and destination cannot be the same!")
        return

    # Simple pricing logic
    price = random.randint(1000, 5000)  # Random ticket price
    seat_no = f"{random.randint(1, 30)}{random.choice('ABCD')}"  # Random seat number

    ticket_text = f"""
    --- Train Ticket ---
    Passenger: {name}
    Age: {age}
    From: {source}
    To: {destination}
    Seat No: {seat_no}
    Price: ${price}
    -------------------
    """
    text_ticket.config(state='normal')
    text_ticket.delete(1.0, tk.END)
    text_ticket.insert(tk.END, ticket_text)
    text_ticket.config(state='disabled')

# GUI setup
root = tk.Tk()
root.title("Train Ticket Generator")
root.geometry("400x500")
root.resizable(False, False)

tk.Label(root, text="Train Ticket Generator", font=("Arial", 16, "bold")).pack(pady=10)

# Passenger Name
tk.Label(root, text="Passenger Name").pack()
entry_name = tk.Entry(root, font=("Arial", 12))
entry_name.pack(pady=5)

# Age
tk.Label(root, text="Age").pack()
entry_age = tk.Entry(root, font=("Arial", 12))
entry_age.pack(pady=5)

# Source & Destination
tk.Label(root, text="Source").pack()
combo_source = ttk.Combobox(root, values=["Lagos", "Abuja", "Kano", "Port Harcourt"])
combo_source.pack(pady=5)

tk.Label(root, text="Destination").pack()
combo_destination = ttk.Combobox(root, values=["Lagos", "Abuja", "Kano", "Port Harcourt"])
combo_destination.pack(pady=5)

# Generate Ticket Button
tk.Button(root, text="Generate Ticket", font=("Arial", 14), command=generate_ticket).pack(pady=10)

# Ticket Display
text_ticket = tk.Text(root, height=10, width=40, state='disabled', font=("Courier", 12))
text_ticket.pack(pady=10)

root.mainloop()
