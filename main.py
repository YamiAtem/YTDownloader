from tkinter import *
from tkinter.ttk import Notebook, Style
from screens import download_screen

import menu_bar

# root of app
root = Tk()

# title of app
root.title("YT Downloader")

# icon of app
root.iconbitmap("icons/favicon.ico")

# geometry of app
x, y = round(root.winfo_screenwidth() / 5), round(root.winfo_screenheight() / 15)
root.geometry("800x600+{}+{}".format(x, y))

# icons
menu_icon = PhotoImage(file="icons/menu.png")
home_icon = PhotoImage(file="icons/home.png")
download_icon = PhotoImage(file="icons/download.png")
app_icon = PhotoImage(file="images/yt_downloader.png")
github_icon = PhotoImage(file="icons/github.png")
website_icon = PhotoImage(file="icons/website.png")
update_icon = PhotoImage(file="icons/update.png")

# icons array
icons = [menu_icon, home_icon, download_icon, github_icon, website_icon, update_icon]

# dicts of widgets
menu_buttons_style: dict = dict(compound=LEFT, bd=0, bg="#21252B", fg="#fff", font=("Times New Roman", 20),
                                activebackground="#BD93F9", anchor="w", padx=20, width=300)

# Style
style = Style()

# Style for Notebook Tabs
style.layout('TNotebook.Tab', [])

# Style for Notebook
style.layout("TNotebook", [])
style.configure("TNotebook", tabmargins=0)

# main frame of app
main = Frame(root, bg="#282C34")
main.pack(expand=1, fill="both")

# Notebook
tabs = Notebook(main)
tabs.pack(expand=1, fill="both", side="right")

# create screens
screen = Frame(tabs, bg="#282C34")
screen.pack(expand=1, fill="both")

screen_2 = Frame(tabs, bg="#282C34")
screen_2.pack(expand=1, fill="both")

screen_3 = Frame(tabs, bg="#282C34")
screen_3.pack(expand=1, fill="both")

# add screens
tabs.add(screen)
tabs.add(screen_2)
tabs.add(screen_3)

# load screens
icon_label = Label(screen, bg="#282C34", image=app_icon)
icon_label.pack(anchor='center')

download_screen.load(screen_2, root)

# load menu
menu_bar.load(main, icons, menu_buttons_style, tabs, root)

root.mainloop()
