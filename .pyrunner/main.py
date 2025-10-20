# This code is generated using PyUIbuilder: https://pyuibuilder.com

import os
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from pandastable import Table

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

main = tk.Tk()
main.title("Curse-Forge mods analytics showcase")
main.config(bg="#3d3d3d")
main.geometry("1284x618")
main_img = Image.open(os.path.join(BASE_DIR, "assets", "images", "pandas_logo.png"))
main_img = ImageTk.PhotoImage(main_img)
main.iconphoto(False, main_img)


style = ttk.Style(main)
style.theme_use("clam")



frame = tk.Frame(master=main)
frame.config(bg="#2d2754")
frame.place(x=13, y=173, width=752, height=317)

style.configure("option_menu.TCombobox", fieldbackground="#d442e4", foreground="#000", cursor="exchange")
option_menu_options = ["min","max","mean","median"]
option_menu_var = tk.StringVar(value="Select filter")
option_menu = ttk.Combobox(frame, textvariable=option_menu_var, values=option_menu_options, style="option_menu.TCombobox")
option_menu.place(x=197, y=12, width=175, height=61)

style.configure("option_menu1.TCombobox", fieldbackground="#d442e4", foreground="#000", cursor="exchange")
option_menu1_options = ["Downloads","By year"]
option_menu1_var = tk.StringVar(value="Downloads")
option_menu1 = ttk.Combobox(frame, textvariable=option_menu1_var, values=option_menu1_options, style="option_menu1.TCombobox")
option_menu1.place(x=8, y=13, width=175, height=61)

style.configure("button.TButton", background="#2ee134", foreground="#000", relief=tk.FLAT, font=("", 20), cursor="target")
style.map("button.TButton", background=[("active", "#30802e")], foreground=[("active", "#000")])

button = ttk.Button(master=frame, text="Apply filters", style="button.TButton")
button.place(x=481, y=85, width=160, height=52)

style.configure("label.TLabel", background="#8e8dff", foreground="#000", font=("", 25), anchor="center")
label = ttk.Label(master=frame, text="None", style="label.TLabel")
label.configure(anchor="center")
label.place(x=390, y=11, width=343, height=62)

pandas_table_table_frame = tk.Frame(master=main)
pandas_table_table_frame.place(x=10, y=9, width=756, height=157)
pandas_table = Table(parent=pandas_table_table_frame)
pandas_table.editable = False
pandas_table.importCSV(os.path.join(BASE_DIR, "assets", "others", "top_authors.csv"))
pandas_table.show()

style.configure("label1.TLabel", background="#E4E2E2", foreground="#000", font=("", 30), anchor="center")
label1 = ttk.Label(master=main, text="Analysis Scr. here", style="label1.TLabel")
label1.configure(anchor="center")
label1.place(x=771, y=9, width=500, height=350)


main.mainloop()