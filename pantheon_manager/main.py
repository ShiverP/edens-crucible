import tkinter as tk
from tkinter import ttk
import sqlite3

# Function to create database and tables if not exists
def create_database():
    conn = sqlite3.connect('deities.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS pantheons (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                 )''')

    c.execute('''CREATE TABLE IF NOT EXISTS deities (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    pantheon_id INTEGER,
                    deity_type TEXT,
                    power_level INTEGER,
                    gender TEXT,
                    FOREIGN KEY(pantheon_id) REFERENCES pantheons(id)
                 )''')

    conn.commit()
    conn.close()

# Function to add pantheon to database
def add_pantheon():
    name = pantheon_entry.get()

    conn = sqlite3.connect('deities.db')
    c = conn.cursor()

    c.execute('''INSERT INTO pantheons (name) VALUES (?)''', (name,))
    conn.commit()
    conn.close()

    pantheon_entry.delete(0, tk.END)

# Function to add deity to database
def add_deity():
    name = name_entry.get()
    pantheon_id = pantheon_id_var.get()
    deity_type = type_entry.get()
    power_level = power_entry.get()
    gender = gender_entry.get()

    conn = sqlite3.connect('deities.db')
    c = conn.cursor()

    c.execute('''INSERT INTO deities (name, pantheon_id, deity_type, power_level, gender)
                 VALUES (?, ?, ?, ?, ?)''', (name, pantheon_id, deity_type, power_level, gender))
    conn.commit()
    conn.close()

    name_entry.delete(0, tk.END)
    type_entry.delete(0, tk.END)
    power_entry.delete(0, tk.END)
    gender_entry.delete(0, tk.END)

# Function to populate pantheon combobox
def populate_pantheon_combobox():
    conn = sqlite3.connect('deities.db')
    c = conn.cursor()

    c.execute('''SELECT * FROM pantheons''')
    pantheons = c.fetchall()

    pantheon_combobox['values'] = [pantheon[1] for pantheon in pantheons]

    conn.close()

# Function to retrieve pantheon ID based on name
def get_pantheon_id(pantheon_name):
    conn = sqlite3.connect('deities.db')
    c = conn.cursor()

    c.execute('''SELECT id FROM pantheons WHERE name = ?''', (pantheon_name,))
    pantheon_id = c.fetchone()[0]

    conn.close()
    return pantheon_id

# Create database if not exists
create_database()

# Create main window
root = tk.Tk()
root.title("Deity Manager")

# Create style
style = ttk.Style()
style.theme_use('clam')

# Create dark theme
style.configure('.', background='#333333', foreground='white')
style.map('.', background=[('selected', '#777777')])

# Pantheon Manager
pantheon_frame = ttk.LabelFrame(root, text="Pantheon Manager", padding=(10, 10))
pantheon_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

pantheon_label = ttk.Label(pantheon_frame, text="Pantheon:")
pantheon_label.grid(row=0, column=0, padx=5, pady=5)

pantheon_entry = ttk.Entry(pantheon_frame)
pantheon_entry.grid(row=0, column=1, padx=5, pady=5)

add_pantheon_button = ttk.Button(pantheon_frame, text="Add Pantheon", command=add_pantheon)
add_pantheon_button.grid(row=0, column=2, padx=5, pady=5)

# God Manager
god_frame = ttk.LabelFrame(root, text="God Manager", padding=(10, 10))
god_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

name_label = ttk.Label(god_frame, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)

name_entry = ttk.Entry(god_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

pantheon_label = ttk.Label(god_frame, text="Pantheon:")
pantheon_label.grid(row=1, column=0, padx=5, pady=5)

pantheon_id_var = tk.StringVar()
pantheon_combobox = ttk.Combobox(god_frame, textvariable=pantheon_id_var, state="readonly")
pantheon_combobox.grid(row=1, column=1, padx=5, pady=5)
populate_pantheon_combobox()

type_label = ttk.Label(god_frame, text="Type:")
type_label.grid(row=2, column=0, padx=5, pady=5)

type_entry = ttk.Entry(god_frame)
type_entry.grid(row=2, column=1, padx=5, pady=5)

power_label = ttk.Label(god_frame, text="Power Level:")
power_label.grid(row=3, column=0, padx=5, pady=5)

power_entry = ttk.Entry(god_frame)
power_entry.grid(row=3, column=1, padx=5, pady=5)

gender_label = ttk.Label(god_frame, text="Gender:")
gender_label.grid(row=4, column=0, padx=5, pady=5)

gender_entry = ttk.Entry(god_frame)
gender_entry.grid(row=4, column=1, padx=5, pady=5)

add_deity_button = ttk.Button(god_frame, text="Add Deity", command=add_deity)
add_deity_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Start Tkinter event loop
root.mainloop()

