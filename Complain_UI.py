import Class
from tkinter import *
from tkinter import ttk
import Window_update

def complain_window(window):
    Window_update.clear_window(window)

    # Complain window UI
    complain_frame = Frame(window)
    complain_frame.pack()
    data_frame = LabelFrame(complain_frame, text="Information")
    data_frame.pack(padx=10, pady=10, fill=X, expand=True)
    data_frame.columnconfigure(0, weight=1)
    data_frame.columnconfigure(1, weight=3)

    staff_id_label = Label(data_frame, text="Staff ID:")
    staff_id_label.grid(row=0, column=0, padx=10, pady=10)
    staff_id_entry = Entry(data_frame)
    staff_id_entry.grid(row=0, column=1, padx=10, pady=10)

    name_label = Label(data_frame, text="Name:")
    name_label.grid(row=1, column=0, padx=5, pady=5)
    name_entry = Entry(data_frame)
    name_entry.grid(row=1, column=1, padx=5, pady=5)

    date_label = Label(data_frame, text="Date:")
    date_label.grid(row=2, column=0, padx=5, pady=5)
    date_entry = Entry(data_frame)
    date_entry.grid(row=2, column=1, padx=5, pady=5)

    email_label = Label(data_frame, text="Email:")
    email_label.grid(row=3, column=0, padx=5, pady=5)
    email_entry = Entry(data_frame)
    email_entry.grid(row=3, column=1, padx=5, pady=5)

    content_label = Label(data_frame, text="Description:")
    content_label.grid(row=4, column=0, padx=5, pady=5)
    content_text = Text(data_frame, width = 50, height = 10)
    content_text.grid(row=5, column=0, padx=5, columnspan=2)

    # Submit Ticket function to the hash and delete all to make new complain
    def create_ticket(staff_id, name, date, email, content):
        ticket1 = Class.Ticket(staff_id, name, date, email, "Open", content)
        ticket1.submit()
        staff_id_entry.delete(0, END)
        name_entry.delete(0, END)
        date_entry.delete(0, END)
        email_entry.delete(0, END)
        content_text.delete("1.0", "end-1c")

    submit_button = Button(complain_frame, text="Submit", command=lambda: create_ticket(staff_id_entry.get(),
                                                                                        name_entry.get(),
                                                                                        date_entry.get(),
                                                                                        email_entry.get(),
                                                                                        content_text.get("1.0", 'end-1c')))
    submit_button.pack()
