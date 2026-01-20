import tkinter as tk
from tkinter import ttk

# Conversion function
def convert_temperature():
    try:
        temp = float(entry_temp.get())
        unit = combo.get()

        if unit == "Celsius to Fahrenheit":
            result = (temp * 9/5) + 32
        elif unit == "Fahrenheit to Celsius":
            result = (temp - 32) * 5/9

        label_result.config(text=f"Result: {result:.2f}")
    except:
        label_result.config(text="Invalid input")

# GUI setup
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x200")
root.resizable(False, False)

tk.Label(root, text="Temperature Converter", font=("Arial", 16, "bold")).pack(pady=10)

# Entry for temperature
entry_temp = tk.Entry(root, font=("Arial", 14))
entry_temp.pack(pady=5)

# Dropdown for conversion type
combo = ttk.Combobox(root, values=["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
combo.current(0)
combo.pack(pady=5)

# Convert button
tk.Button(root, text="Convert", font=("Arial", 14), command=convert_temperature).pack(pady=10)

# Result label
label_result = tk.Label(root, text="Result:", font=("Arial", 12))
label_result.pack(pady=5)

root.mainloop()
