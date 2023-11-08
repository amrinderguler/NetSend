import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk, ImageOps
import socket
import os
import threading
import recv_file
import send_file

root = tk.Tk()
root.title("NetSend")

# Set the window size
root.geometry("800x600")

# Set the window background color
root.configure(bg='#fed7b8')

# Open the image file
img = Image.open("D:/Coding/Python/netshare/logo.jpg")

# Crop the image to remove the border
img = ImageOps.crop(img, border=10) 

# Resize the image
img = img.resize((200, 200), Image.LANCZOS)

# Convert the image to a Tkinter-compatible photo image
logo = ImageTk.PhotoImage(img)

# Display the logo
logo_label = tk.Label(root, image=logo, borderwidth=0,bg='#fed7b8')
logo_label.grid(row=0, column=0, columnspan=2)

welcome_label = tk.Label(root, text="Welcome to NetSend", font=("Arial", 24), bg='#fed7b8')
welcome_label.grid(row=1, column=0, columnspan=2, pady=10, sticky='nsew')

send_button = tk.Button(root, text="Send File", command=lambda: threading.Thread(target=send_file.send_file).start(), font=("Arial", 14), bg='light green')
send_button.grid(row=2, column=0, padx=20, pady=10)

receive_button = tk.Button(root, text="Receive File", command=lambda: threading.Thread(target=recv_file.receive_file).start(), font=("Arial", 14), bg='light blue')
receive_button.grid(row=2, column=1, padx=20, pady=10)

# Configure the grid to expand properly when the window is resized
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)

root.mainloop()
