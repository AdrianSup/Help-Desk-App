import tkinter
from tkinter import *
from Class import Ticket
# from tkinter import ttk


def clear_window(windows):
    for i in windows.winfo_children()[1:]:
        i.destroy()


# window construct
window = tkinter.Tk()
window.title("Help Desk System")
window.geometry("700x500")
menubar = Menu(window)
window.config(bg="white", menu=menubar)


def complain_window():
    clear_window(window)
    complain_frame = Frame(window).pack()
    data_frame = LabelFrame(complain_frame, text="Information")
    data_frame.pack(padx=10, pady=10)

    staff_id_label = Label(data_frame, text="Staff ID")
    staff_id_label.grid(row=0, column=0, padx=10, pady=10)
    staff_id_entry = Entry(data_frame)
    staff_id_entry.grid(row=0, column=1, padx=10, pady=10)

    name_label = Label(data_frame, text="Name")
    name_label.grid(row=1, column=0, padx=10, pady=10)
    name_entry = Entry(data_frame)
    name_entry.grid(row=1, column=1, padx=10, pady=10)

    date_label = Label(data_frame, text="Date")
    date_label.grid(row=2, column=0, padx=10, pady=10)
    date_entry = Entry(data_frame)
    date_entry.grid(row=2, column=1, padx=10, pady=10)

    email_label = Label(data_frame, text="Email")
    email_label.grid(row=3, column=0, padx=10, pady=10)
    email_entry = Entry(data_frame)
    email_entry.grid(row=3, column=1, padx=10, pady=10)

    content_label = Label(data_frame, text="Description")
    content_label.grid(row=4, column=0, padx=10, pady=10)
    content_entry = Entry(data_frame)
    content_entry.grid(row=5, column=0, padx=10, pady=10)


menubar.add_command(label="Complain", command=complain_window)
window.mainloop()

ticket1 = Ticket("1234", "20240027", "Adrian", "adriansuprapto2004@gmail.com", "this is a test", "open")
