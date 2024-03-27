import tkinter
from tkinter import *
import Review_UI, Complain_UI

def window_construct():
    # window construct
    window = tkinter.Tk()
    window.title("Help Desk System")
    window.geometry("700x500")

    menubar = Menu(window)
    window.config(bg="white", menu=menubar)
    menubar.add_command(label="Complain", command=lambda: Complain_UI.complain_window(window))
    menubar.add_command(label="Review TIcket", command=lambda: Review_UI.review_window(window))
    window.mainloop()

if __name__ == "__main__":
    window_construct()
