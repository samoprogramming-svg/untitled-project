import os
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from pandastable import Table
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from playsound import playsound
import pygame
pygame.mixer.init()
import time

multipliers = {"K": 1_000, "M": 1_000_000, "B": 1_000_000_000}
months = {"Jan":1, "Feb": 2, "Mar": 3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}

class introduction():
    def __init__(self):
        pass

    def introUI(self):
        self.introapp = tk.Tk()
        self.introapp.title("Welcome to Curse-Forge Mods Analytics")
        self.introapp.config(bg="#4b3a8c")
        self.introapp.geometry("800x500")  
        self.introapp.resizable(False, False)
 
        introlabel = tk.Label(master=self.introapp, text="Welcome to Curse-Forge Mods Analytics\nIn this app you can explore Curse-forge mods analytics for 2021\n\nClick 'Continue' to proceed.\n\n\n\nby Samuel Kukučka\n\n Copyright laws are not applied \n But its not pretty to steal.\n\n :)", font=("", 16), bg="#4b3a8c", fg="#fff", justify="center")
        introlabel.pack(pady=50)
        continue_button = tk.Button(master=self.introapp, text="Continue", font=("", 14), bg="#349429", fg="#000", command=self.startmainapp)
        continue_button.pack(pady=20)

        pygame.mixer.music.load("untitled-project-main/sounds/echo3b.mp3")
        pygame.mixer.music.play()
        self.introapp.mainloop()

    def startmainapp(self):
        self.introapp.destroy()
        app = App()
        app.MakeUIloop()

class App():

    def __init__(self):
        self.dataframe = pd.read_csv("untitled-project-main/DataFrames/finalfile.csv")

    def check_last_updated_type(self, file_path):
        df = pd.read_csv(file_path)

        invalid_indexes = []
        for i, val in enumerate(df["last_updated"]):
            try:
                float(val)
            except (ValueError, TypeError):
                invalid_indexes.append(i)

        if not invalid_indexes:
            print("All values can be and were converted to float data-type")
        else:
            print("Non-float-compatible values found at indexes:", invalid_indexes)

        return invalid_indexes

    def ApplyAnalytics(self):
        filter = self.option_menu_var.get()
        what_to_filter = self.option_menu1_var.get()

        if str(what_to_filter) == "Downloads":
            what_to_filter2 = "downloads"
        elif str(what_to_filter) == "By year":
            what_to_filter2 = "last_updated"
        if filter == "Select filter":
            self.label.config(text="Select filter please")
            pygame.mixer.music.load("sounds/errorsound.mp3")
            pygame.mixer.music.play()
            return 

        if what_to_filter == "Downloads":

            if str(filter) == "min":
                result = self.dataframe[what_to_filter2].min()
            if str(filter) == "max":
                result = self.dataframe[what_to_filter2].max()
            if str(filter) == "mean":
                result = self.dataframe[what_to_filter2].mean()
            if str(filter) == "median":
                result = self.dataframe[what_to_filter2].median()

            pygame.mixer.music.load("untitled-project-main/sounds/duck-toy-sound.mp3")
            pygame.mixer.music.play()

            self.label.config(text=result)
        
        elif what_to_filter == "By year":

            if str(filter) == "min":
                result_year = self.dataframe["last_updated"].min()
            if str(filter) == "max":
                result_year = self.dataframe["last_updated"].max()
            if str(filter) == "mean":
                result_year = self.dataframe["last_updated"].mean()
            if str(filter) == "median":
                result_year = self.dataframe["last_updated"].median()

            if result_year:
                self.label.config(text=result_year)

                pygame.mixer.music.load("untitled-project-main/sounds/duck-toy-sound.mp3")
                pygame.mixer.music.play()
            else:
                pygame.mixer.music.load("untitled-project-main/sounds/errorsound.mp3")
                pygame.mixer.music.play()
                print("No mean year returned, ERROR 404")
        else:
            pygame.mixer.music.load("untitled-project-main/sounds/errorsound.mp3")
            pygame.mixer.music.play()
            print("what_to_filter is wrong, ERROR 1")

    def clean_downloads(self, path):
        
        counter = 0
        df = pd.read_csv(path)
        df_local = df.copy()

        for counter in range(len(df_local)):

            old_value = df_local.at[counter, "downloads"]

            if old_value != "":
                try:
                    number, _ = old_value.split()

                    suffix = number[-1]

                    if suffix.isalpha():
                        final_number_p1 = number[:-1]

                        multiplier_value = multipliers.get(suffix, 1)

                        final_number_p2 = float(final_number_p1) * int(multiplier_value)

                        final_number_p2 = float(final_number_p2)

                        df_local.at[counter, "downloads"] = final_number_p2
                    else:
                        df_local.at[counter, "downloads"] = float(number)
                except:
                    try:
                        df_local.at[counter, "downloads"] = float(old_value)
                    except:
                        try:
                            x, _ = df_local.at[counter, "downloads"].split()

                            if x == "-":
                                df_local.at[counter, "downloads"] = 0.0
                        except:
                            continue

        df_local.to_csv("untitled-project-main/DataFrames/cleaned_downloads_only.csv", index=False)
        return df_local

    def clean_dates(self, path = "untitled-project-main/DataFrames/cleaned_downloads_finals.csv"):
        # code changed a lot of times depending on the data converting process (thats why I have like 6 csv files of the same dataframe)

        counter2 = 0
        df = pd.read_csv(path)
        df_local2 = df.copy()

        for counter2 in range(len(df_local2)):

            old_value2 = df_local2.at[counter2, "last_updated"]

            print("Old value: ", old_value2)

            if old_value2 != "":
                try:
                    _, year = str(old_value2).split()

                    df_local2.at[counter2, "last_updated"] = float(year)

                    counter2 += 1
                except:
                    continue

        df_local2.to_csv("untitled-project-main/DataFrames/finalfile2.csv", index=False)

    def chart1(self):
        img = Image.open("untitled-project-main/images/analysis_scr2.png")
        img.thumbnail((1200, 1000)) 
        self.tk_img = ImageTk.PhotoImage(img)
        self.label1.config(image=self.tk_img)
        pygame.mixer.music.load("untitled-project-main/sounds/fart-with-reverb.mp3")
        pygame.mixer.music.play()

    def chart2(self):
        img = Image.open("untitled-project-main/images/averagedownloadspermodanalysis.png")
        img.thumbnail((1200, 1000)) 
        self.tk_img = ImageTk.PhotoImage(img)
        self.label1.config(image=self.tk_img)
        pygame.mixer.music.load("untitled-project-main/sounds/fart-with-reverb.mp3")
        pygame.mixer.music.play()

    def chart3(self):
        img = Image.open("untitled-project-main/images/downloadsperkeyword.png")
        img.thumbnail((1200, 1000)) 
        self.tk_img = ImageTk.PhotoImage(img)
        self.label1.config(image=self.tk_img)
        pygame.mixer.music.load("untitled-project-main/sounds/fart-with-reverb.mp3")
        pygame.mixer.music.play()

    def chart4(self):
        img = Image.open("untitled-project-main/images/pieanalysis.png")
        img.thumbnail((1200, 1000)) 
        self.tk_img = ImageTk.PhotoImage(img)
        self.label1.config(image=self.tk_img)
        pygame.mixer.music.load("untitled-project-main/sounds/fart-with-reverb.mp3")
        pygame.mixer.music.play()

    def popup_image(self):
        top = tk.Toplevel()
        top.title("Image Popup")

        img = Image.open("untitled-project-main/images/romanians.png")
        img = img.resize((1200, 800))
        self.popup_photo = ImageTk.PhotoImage(img) 

        label = tk.Label(top, image=self.popup_photo)
        label.pack()


    def exitapp(self):
        self.popup_image()
        pygame.mixer.music.load("untitled-project-main/sounds/roblox-bye.mp3")
        pygame.mixer.music.play()
        pygame.mixer.music.queue("untitled-project-main/sounds/drum_bun.mp3")
        self.main.after(10000, self.main.destroy)

    def MakeUIloop(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        self.main = tk.Tk()
        self.main.title("Curse-Forge mods analytics showcase for 2021")
        self.main.config(bg="#3d3d3d")
        self.main.geometry("2345x900")  
        self.main.resizable(False, False)

        main_img = Image.open(os.path.join(BASE_DIR, "assets", "images", "pandas_logo.png"))
        main_img = ImageTk.PhotoImage(main_img)
        self.main.iconphoto(False, main_img)

        style = ttk.Style(self.main)
        style.theme_use("clam")

        frame = tk.Frame(master=self.main)
        frame.config(bg="#2d2754")
        frame.place(x=20, y=280, width=1200, height=500) 

        self.option_menu_var = tk.StringVar(value="Select filter")
        option_menu_options = ["min", "max", "mean", "median"]
        self.option_menu = tk.OptionMenu(frame, self.option_menu_var, *option_menu_options)
        self.option_menu.config(font=("Arial", 25), bg="#d442e4", fg="#000", activebackground="#4400ff") 
        self.option_menu["menu"].config(font=("Arial", 25), bg="#4b3a8c", fg="#fff",
                                activebackground="#3d2a70", activeforeground="#000")
        self.option_menu.place(x=300, y=20, width=250, height=80)

        self.option_menu1_var = tk.StringVar(value="Downloads")
        option_menu1_options = ["Downloads", "By year"]
        self.option_menu1 = tk.OptionMenu(frame, self.option_menu1_var, *option_menu1_options)
        self.option_menu1.config(font=("Arial", 25), bg="#d442e4", fg="#000", activebackground="#4400ff")
        self.option_menu1["menu"].config(font=("Arial", 25), bg="#4b3a8c", fg="#fff",
                                activebackground="#3d2a70", activeforeground="#000")
        self.option_menu1.place(x=20, y=20, width=250, height=80)

        
        style.configure("button.TButton", background="#2ee134", foreground="#000", relief=tk.FLAT, font=("", 30), cursor="target")
        style.map("button.TButton", background=[("active", "#30802e")], foreground=[("active", "#000")])

        button = ttk.Button(master=frame, text="Apply filters", style="button.TButton", command=self.ApplyAnalytics)
        button.place(x=750, y=120, width=250, height=80)

        style.configure("button.TButton", background="#f628ef", foreground="#000", relief=tk.FLAT, font=("", 30), cursor="target")
        style.map("button.TButton", background=[("active", "#30802e")], foreground=[("active", "#000")])

        self.buttonimage1 = ttk.Button(master=self.main, text="chart 1", style="button.TButton", command=self.chart1)
        self.buttonimage1.place(x=20, y=800, width=250, height=80)

        self.buttonimage2 = ttk.Button(master=self.main, text="chart 2", style="button.TButton", command=self.chart2)
        self.buttonimage2.place(x=320, y=800, width=250, height=80)

        self.buttonimage3 = ttk.Button(master=self.main, text="chart 3", style="button.TButton", command=self.chart3)
        self.buttonimage3.place(x=620, y=800, width=250, height=80)

        self.buttonimage4 = ttk.Button(master=self.main, text="chart 4", style="button.TButton", command=self.chart4)
        self.buttonimage4.place(x=920, y=800, width=250, height=80)

        self.exitbutton = tk.Button(master=self.main, text="Exit", command=self.exitapp, bg = "red", fg = "white", font=("Arial", 20))
        self.exitbutton.place(x=2250, y=800, width=80, height=80)

        style.configure("label.TLabel", background="#8e8dff", foreground="#000", font=("", 35), anchor="center")
        self.label = ttk.Label(master=frame, text="None", style="label.TLabel")
        self.label.configure(anchor="center")
        self.label.place(x=600, y=20, width=550, height=80)

        pandas_table_table_frame = tk.Frame(master=self.main)
        pandas_table_table_frame.place(x=20, y=20, width=1200, height=250)
        pandas_table = Table(parent=pandas_table_table_frame)
        pandas_table.editable = False
        pandas_table.importCSV(os.path.join(BASE_DIR, "assets", "others", "top_authors.csv"))
        pandas_table.rowheight = 40         
        pandas_table.colwidth = 150         
        pandas_table.fontsize = 16           
        pandas_table.show()

        style.configure("label1.TLabel", background="#E4E2E2", foreground="#000", font=("", 40), anchor="center")
        img = Image.open("untitled-project-main/images/defaultanalysis.png")
        img.thumbnail((1200, 1000)) 
        tk_img_default = ImageTk.PhotoImage(img)
        self.label1 = ttk.Label(master=self.main, image=tk_img_default, style="label1.TLabel")
        self.label1.configure(anchor="center")
        self.label1.place(x=1230, y=20, width=1100, height=760)

        pygame.mixer.music.load("untitled-project-main/sounds/old-tractor.mp3")
        pygame.mixer.music.play()
        time.sleep(12)
        pygame.mixer.music.load("untitled-project-main/sounds/windows-xp-startup.mp3")
        pygame.mixer.music.play()
        
        self.main.mainloop()

intro = introduction()
intro.introUI()
