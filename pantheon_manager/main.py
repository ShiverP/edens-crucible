import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Pantheon Manager")
root.geometry("600x400")
root.configure(bg="#f0f0f0")  # Set background color

# Set custom font
font_style = ("Helvetica", 12)

# Create frames
header_frame = tk.Frame(root, bg="#333333", pady=10)
header_frame.pack(fill="x")

content_frame = tk.Frame(root, bg="#f0f0f0")
content_frame.pack(fill="both", expand=True, padx=20, pady=10)

# Create header label
header_label = tk.Label(header_frame, text="Pantheon Manager", fg="white", bg="#333333", font=("Helvetica", 16))
header_label.pack()

# Create buttons
add_button = ttk.Button(content_frame, text="Add Pantheon", style="Main.TButton")
add_button.pack(pady=10)

edit_button = ttk.Button(content_frame, text="Edit Pantheon", style="Main.TButton")
edit_button.pack(pady=10)

remove_button = ttk.Button(content_frame, text="Remove Pantheon", style="Main.TButton")
remove_button.pack(pady=10)

# Create custom style for buttons
style = ttk.Style()
style.configure("Main.TButton", foreground="white", background="#333333", font=font_style, padding=10)

# Run the application
root.mainloop()

