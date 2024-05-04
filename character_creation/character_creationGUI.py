import tkinter as tk
from tkinter import ttk
import mysql.connector

class PantheonRegistryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pantheon Registry")
        self.root.geometry("600x400")

        self.create_database_connection()

        # Create notebook (tab control)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Create pantheon tab
        self.pantheon_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.pantheon_tab, text="Pantheons")
        self.create_pantheon_widgets()

        # Create god tab
        self.god_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.god_tab, text="Gods")
        self.create_god_widgets()

    def create_database_connection(self):
        # Establish connection to MariaDB database
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="ShiverP",
            password="Steppenwolf69!",
            database="pantheon_registry"
        )
        # Create database cursor
        self.db_cursor = self.db_connection.cursor()

    def create_pantheon_widgets(self):
        # Pantheon tab widgets
        self.pantheon_label = ttk.Label(self.pantheon_tab, text="Pantheons")
        self.pantheon_label.pack()

        self.pantheon_listbox = tk.Listbox(self.pantheon_tab, height=10, width=50)
        self.pantheon_listbox.pack()

        self.refresh_pantheon_button = ttk.Button(self.pantheon_tab, text="Refresh", command=self.refresh_pantheons)
        self.refresh_pantheon_button.pack()

        self.add_pantheon_label = ttk.Label(self.pantheon_tab, text="Add Pantheon")
        self.add_pantheon_label.pack()

        self.pantheon_entry = ttk.Entry(self.pantheon_tab, width=50)
        self.pantheon_entry.pack()

        self.add_pantheon_button = ttk.Button(self.pantheon_tab, text="Add Pantheon", command=self.add_pantheon)
        self.add_pantheon_button.pack()

    def create_god_widgets(self):
        # God tab widgets
        self.god_label = ttk.Label(self.god_tab, text="Gods")
        self.god_label.pack()

        self.god_listbox = tk.Listbox(self.god_tab, height=10, width=50)
        self.god_listbox.pack()

        self.refresh_god_button = ttk.Button(self.god_tab, text="Refresh", command=self.refresh_gods)
        self.refresh_god_button.pack()

        self.add_god_label = ttk.Label(self.god_tab, text="Add God")
        self.add_god_label.pack()

        self.god_entry = ttk.Entry(self.god_tab, width=50)
        self.god_entry.pack()

        self.add_god_button = ttk.Button(self.god_tab, text="Add God", command=self.add_god)
        self.add_god_button.pack()

    def refresh_pantheons(self):
        # Refresh list of pantheons
        self.pantheon_listbox.delete(0, tk.END)
        self.db_cursor.execute("SELECT pantheon_name FROM pantheons")
        pantheons = self.db_cursor.fetchall()
        for pantheon in pantheons:
            self.pantheon_listbox.insert(tk.END, pantheon[0])

    def add_pantheon(self):
        # Add new pantheon to database
        pantheon_name = self.pantheon_entry.get()
        if pantheon_name:
            self.db_cursor.execute("INSERT INTO pantheons (pantheon_name) VALUES (%s)", (pantheon_name,))
            self.db_connection.commit()
            self.pantheon_entry.delete(0, tk.END)
            self.refresh_pantheons()

    def refresh_gods(self):
        # Refresh list of gods
        self.god_listbox.delete(0, tk.END)
        self.db_cursor.execute("SELECT god_name FROM gods")
        gods = self.db_cursor.fetchall()
        for god in gods:
            self.god_listbox.insert(tk.END, god[0])

    def add_god(self):
        # Add new god to database
        god_name = self.god_entry.get()
        if god_name:
            self.db_cursor.execute("INSERT INTO gods (god_name) VALUES (%s)", (god_name,))
            self.db_connection.commit()
            self.god_entry.delete(0, tk.END)
            self.refresh_gods()

root = tk.Tk()
app = PantheonRegistryApp(root)
root.mainloop()
