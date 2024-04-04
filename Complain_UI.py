import Class
from tkinter import *
from tkinter import ttk
import Window_update
import time

# Complain_UI, receive window and ticket details for Re-Open feature
def complain_window(window, *ticket):
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
    date = time.strftime("%d-%B-%Y")
    date_entry = Label(data_frame, text=date)
    date_entry.grid(row=2, column=1, padx=5, pady=5)

    email_label = Label(data_frame, text="Email:")
    email_label.grid(row=3, column=0, padx=5, pady=5)
    email_entry = Entry(data_frame)
    email_entry.grid(row=3, column=1, padx=5, pady=5)

    content_label = Label(data_frame, text="Description:")
    content_label.grid(row=4, column=0, padx=5, pady=5)
    content_text = Text(data_frame, width = 50, height = 10)
    content_text.grid(row=5, column=0, padx=5, columnspan=2)

    notif = StringVar()
    notif_label = Label(complain_frame, textvariable=notif)
    notif_label.pack()

    # Submit Ticket function to the hash and delete all entrybox
    def create_ticket(staff_id, name, date, email, content):
        # Check all entries if any is blank --> set reminder to fill in the entry
        value_dict = {"Staff ID":staff_id, "Name":name, "Date":date, "Email":email, "Content":content}
        for key, value in value_dict.items():
            if value == "":
                notif.set(f"Please fill in {key}")
                return
        
        # Check if content is a Password Change request and create an object on class based on it
        if "password" in content.lower() and "change" in content.lower():
            ticket1 = Class.Password_Ticket(staff_id, name, date, email, "Open", content)
            password = True
        else:
            ticket1 = Class.Open_Ticket(staff_id, name, date, email, "Open", content)
            password = False
        
        ticket1.submit()            ## Submit the ticket

        # Delete all entry boxes
        staff_id_entry.delete(0, END)
        name_entry.delete(0, END)
        email_entry.delete(0, END)
        content_text.delete("1.0", "end-1c")

        # Give notification about Ticket ID number and or with password generated
        if password:
            notif.set(f"Your ticket number is {ticket1.ticket_id}, Your new Password is {ticket1.respond_text}")
        else:
            notif.set(f"Your ticket number is {ticket1.ticket_id}")
        

    submit_button = Button(complain_frame, text="Submit", command=lambda: create_ticket(staff_id_entry.get(),
                                                                                        name_entry.get(),
                                                                                        date,
                                                                                        email_entry.get(),
                                                                                        content_text.get("1.0", 'end-1c')))
    submit_button.pack()

    # Resubmit Reopen ticket, delete all entrybox, and give notification of the ticket Re-Opened
    def resubmit(ticket_id ,staff_id, name, date, email, content):
        ticket2 = Class.Closed_Ticket(ticket_id=ticket_id, staff_id=staff_id, name=name, date=date, email=email, status="Re-Open", content=content, respond=value[-1])
        ticket2.reopen()
        staff_id_entry.delete(0, END)
        name_entry.delete(0, END)
        email_entry.delete(0, END)
        content_text.delete("1.0", "end-1c")
        notif.set(f"Your ticket {ticket2.ticket_id} is Re-Opened")

    # Check if its Reopen request
    if ticket:
        key, value = ticket        ## Unpack the ticket details; key == ticket_id, value == all other detail in array
        
        # Create multiple stringvar for Entries
        staff_id_str = StringVar()
        name_str = StringVar()
        date_str = StringVar()
        email_str = StringVar()
        
        # Set the stringvar to each respective value
        staff_id_str.set(value[0])
        name_str.set(value[1])
        date_str.set(value[2])
        email_str.set(value[3])

        # Configure all entry with respective stringvar and disable the entry function (Read Only)
        staff_id_entry.config(textvariable=staff_id_str, state=DISABLED)
        name_entry.config(textvariable=name_str, state=DISABLED)
        date_entry.config(textvariable=date_str, state=DISABLED)
        email_entry.config(textvariable=email_str, state=DISABLED)

        # Insert textbox with the old content value
        content_text.insert("1.0", value[5])

        # Configure submit button to Re-Submit
        submit_button.config(text="Re-Submit", command=lambda: resubmit(key,
                                                                        staff_id_entry.get(),
                                                                        name_entry.get(),
                                                                        date,
                                                                        email_entry.get(),
                                                                        content_text.get("1.0", 'end-1c')))
