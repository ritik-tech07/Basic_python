import tkinter as tk
from time import strftime

# Function to update time
def time():
    string = strftime('%H:%M:%S %p')  # 24-hour format with AM/PM
    label.config(text=string)
    label.after(1000, time)  # update every 1 second

# Create window
root = tk.Tk()
root.title("Digital Clock")

# Styling the label
label = tk.Label(root, font=("Arial", 50, "bold"), background="black", foreground="cyan")
label.pack(anchor="center")

# Run the time function
time()

# Run the window
root.mainloop()