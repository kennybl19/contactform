import tkinter as tk

def press(key):
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# GUI setup
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.pack(fill="x", padx=10, pady=10)

frame = tk.Frame(root)
frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = col = 0
for btn in buttons:
    action = calculate if btn == "=" else lambda x=btn: press(x)
    tk.Button(
        frame,
        text=btn,
        width=5,
        height=2,
        font=("Arial", 14),
        command=action
    ).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text="Clear", font=("Arial", 14), command=clear).pack(pady=10)

root.mainloop()
