import tkinter as tk
from tkinter import ttk

# Fixed exchange rates (base: USD)
rates = {
    "USD": 1.0,
    "EUR": 0.92,
    "GBP": 0.78,
    "NGN": 1500.0
}

# -------- Conversion Function --------
def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_cur = from_currency.get()
        to_cur = to_currency.get()

        usd_amount = amount / rates[from_cur]
        converted = usd_amount * rates[to_cur]

        label_result.config(
            text=f"{amount} {from_cur} = {converted:.2f} {to_cur}"
        )
    except:
        label_result.config(text="Invalid input")

# -------- GUI Setup --------
root = tk.Tk()
root.title("Currency Converter")
root.geometry("350x300")
root.resizable(False, False)

tk.Label(root, text="Currency Converter", font=("Arial", 16, "bold")).pack(pady=10)

# Amount Entry
entry_amount = tk.Entry(root, font=("Arial", 14))
entry_amount.pack(pady=5)

# Currency Selection
frame = tk.Frame(root)
frame.pack(pady=10)

from_currency = ttk.Combobox(frame, values=list(rates.keys()), width=8)
from_currency.set("USD")
from_currency.grid(row=0, column=0, padx=5)

tk.Label(frame, text="to").grid(row=0, column=1)

to_currency = ttk.Combobox(frame, values=list(rates.keys()), width=8)
to_currency.set("NGN")
to_currency.grid(row=0, column=2, padx=5)

# Convert Button
tk.Button(
    root,
    text="Convert",
    font=("Arial", 14),
    command=convert_currency
).pack(pady=10)

# Result Label
label_result = tk.Label(root, text="Result:", font=("Arial", 12))
label_result.pack(pady=10)

root.mainloop()
