import tkinter as tk
from tkinter import ttk
import sqlite3

# Create SQLite database connection
conn = sqlite3.connect('deities.db')
c = conn.cursor()

# Create deities table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS deities (id INTEGER PRIMARY KEY, name TEXT, pantheon TEXT, deity_type TEXT, power_level INTEGER, gender TEXT)''')
conn.commit()

# Function to add deity to database
def add_deity():
    name = name_entry.get()
    pantheon = pantheon_entry.get()
    deity_type = type_entry.get()
    power_level = power_entry.get()
    gender = gender_entry.get()

    # Check if text fields are empty and replace with None
    if not name:
        name = None
    if not pantheon:
        pantheon = None
    if not deity_type:
        deity_type = None
    if not power_level:
        power_level = None
    else:
        power_level = int(power_level)
    if not gender:
        gender = None

    c.execute('''INSERT INTO deities (name, pantheon, deity_type, power_level, gender)
                 VALUES (?, ?, ?, ?, ?)''', (name, pantheon, deity_type, power_level, gender))
    conn.commit()

    # Clear input fields
    name_entry.delete(0, tk.END)
    pantheon_entry.delete(0, tk.END)
    type_entry.delete(0, tk.END)
    power_entry.delete(0, tk.END)
    gender_entry.delete(0, tk.END)

# Create Tkinter GUI
root = tk.Tk()
root.title("Deity Manager")

# GUI elements
name_label = ttk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = ttk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

pantheon_label = ttk.Label(root, text="Pantheon:")
pantheon_label.grid(row=1, column=0, padx=5, pady=5)
pantheon_entry = ttk.Entry(root)
pantheon_entry.grid(row=1, column=1, padx=5, pady=5)

type_label = ttk.Label(root, text="Type:")
type_label.grid(row=2, column=0, padx=5, pady=5)
type_entry = ttk.Entry(root)
type_entry.grid(row=2, column=1, padx=5, pady=5)

power_label = ttk.Label(root, text="Power Level:")
power_label.grid(row=3, column=0, padx=5, pady=5)
power_entry = ttk.Entry(root)
power_entry.grid(row=3, column=1, padx=5, pady=5)

gender_label = ttk.Label(root, text="Gender:")
gender_label.grid(row=4, column=0, padx=5, pady=5)
gender_entry = ttk.Entry(root)
gender_entry.grid(row=4, column=1, padx=5, pady=5)

add_button = ttk.Button(root, text="Add Deity", command=add_deity)
add_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Start Tkinter event loop
root.mainloop()

# Close database connection when done
conn.close()

