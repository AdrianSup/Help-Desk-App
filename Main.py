import tkinter
from tkinter import *
from Class import Ticket
import Class
from tkinter import ttk


def clear_window(windows):
    for i in windows.winfo_children()[1:]:
        i.destroy()

def refresh_ticket(list, tree):
    tree.delete(*tree.get_children())
    global count
    count = 0

    for value in list[0:]:
        count += 1
        if count % 2 == 0:
            tree.insert('', index='end', iid=count, values=value, tags=('evenrow',))
        else:
            tree.insert('', index='end', iid=count, values=value, tags=('oddrow',))

    tree.tag_configure("oddrow", background="white")
    tree.tag_configure("evenrow", background="lightblue")

def submit(staff_id, name, date, email, content):
    ticket1 = Ticket("1234", staff_id, name, date, email, "Open", content)
    ticket1.submit()


# window construct
window = tkinter.Tk()
window.title("Help Desk System")
window.geometry("700x500")
menubar = Menu(window)
window.config(bg="white", menu=menubar)


def complain_window():
    clear_window(window)
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
    content_entry = Entry(data_frame)
    content_entry.grid(row=5, column=0, padx=5, columnspan=2)

    submit_button = Button(complain_frame, text="Submit", command=lambda: submit(staff_id_entry.get(),
                                                                                 name_entry.get(),
                                                                                 date_entry.get(),
                                                                                 email_entry.get(),
                                                                                 content_entry.get()))
    submit_button.pack()

def review_window():
    clear_window(window)
    info_frame = LabelFrame(window, text="Ticket Info")
    info_frame.pack(padx=10, pady=10, fill=X, expand=True)

    ticket_id_label = Label(info_frame, text="Ticket ID:")
    ticket_id_label.grid(row=0, column=0, padx=10, pady=10)
    ticket_id_entry = Entry(info_frame)
    ticket_id_entry.grid(row=0, column=1, padx=10, pady=10)

    staff_id_label = Label(info_frame, text="Staff ID:")
    staff_id_label.grid(row=1, column=0, padx=10, pady=10)
    staff_id_entry = Entry(info_frame)
    staff_id_entry.grid(row=1, column=1, padx=10, pady=10)

    name_label = Label(info_frame, text="Name:")
    name_label.grid(row=2, column=0, padx=5, pady=5)
    name_entry = Entry(info_frame)
    name_entry.grid(row=2, column=1, padx=5, pady=5)

    date_label = Label(info_frame, text="Date:")
    date_label.grid(row=0, column=2, padx=5, pady=5)
    date_entry = Entry(info_frame)
    date_entry.grid(row=0, column=3, padx=5, pady=5)

    email_label = Label(info_frame, text="Email:")
    email_label.grid(row=1, column=2, padx=5, pady=5)
    email_entry = Entry(info_frame)
    email_entry.grid(row=1, column=3, padx=5, pady=5)

    status_label = Label(info_frame, text="Status:")
    status_label.grid(row=0, column=4, padx=5, pady=5)
    status_entry = Entry(info_frame)
    status_entry.grid(row=0, column=5, padx=5, pady=5)


    cols = ["Ticket ID","Staff ID","Name","Date","Email","Status"]
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", background="#D3D3D3", rowheight=25, foreground="black",
                    fieldbackground="#D3D3D3")
    style.map("Treeview", background=[("selected", "#347083")])
    table_frame = Frame(window)
    table_frame.pack(side=TOP, pady=20, padx=30)
    table_scroll = Scrollbar(table_frame)
    table_scroll.pack(side=RIGHT, fill=Y)
    ticket_tree = ttk.Treeview(table_frame, columns= cols, show="headings", yscrollcommand=table_scroll.set,
                                  height="15")
    ticket_tree.pack()
    table_scroll.config(command=ticket_tree.yview)

    ticket_tree.column(cols[0], anchor=W, width=140)
    ticket_tree.column(cols[1], anchor=W, width=140)
    ticket_tree.column(cols[2], anchor=W, width=140)
    ticket_tree.column(cols[3], anchor=W, width=100)
    ticket_tree.column(cols[4], anchor=W, width=100)
    ticket_tree.column(cols[5], anchor=W, width=100)

    for i in cols:
        ticket_tree.heading(i, text=i)

    refresh_ticket(Class.ticket_list, ticket_tree)

    #Feature
    def select_record(e):

        ticket_id_entry.delete(0, END)
        staff_id_entry.delete(0, END)
        name_entry.delete(0, END)
        date_entry.delete(0, END)
        email_entry.delete(0, END)
        status_entry.delete(0, END)

        selected = ticket_tree.focus()
        value = ticket_tree.item(selected, 'value')

        try:
            ticket_id_entry.insert(0, value[0])
            staff_id_entry.insert(0, value[1])
            name_entry.insert(0, value[2])
            date_entry.insert(0, value[3])
            email_entry.insert(0, value[4])
            status_entry.insert(0, value[5])
        except IndexError:
            pass
        
    def search(e):
        ticket_id_record = ticket_id_entry.get().lower()
        staff_id_record = staff_id_entry.get().lower()
        name_record = name_entry.get().lower()
        date_record = date_entry.get().lower()
        email_record = email_entry.get().lower()
        status_record = status_entry.get().lower()

        list_record = ((ticket_id_record, staff_id_record, name_record, date_record, email_record, status_record))

        ticket_tree.delete(*ticket_tree.get_children())
        if list_record[0] == "" and list_record[1] == "" and list_record[2] == "" and list_record[3] == "" and list_record[4] == "":
            refresh_ticket(Class.ticket_list, ticket_tree)  
        else:
            for i in Class.ticket_list:
                if list_record[0] in str(i[0]).lower():
                    ticket_tree.insert('', index='end', values=i, tags=('evenrow',))
                elif list_record[1] in str(i[1]).lower():
                    ticket_tree.insert('', index='end', values=i, tags=('evenrow',))
                elif list_record[2] in str(i[2]).lower():
                    ticket_tree.insert('', index='end', values=i, tags=('evenrow',))
                elif list_record[3] in str(i[3]).lower():
                    ticket_tree.insert('', index='end', values=i, tags=('evenrow',))
                elif list_record[4] in str(i[4]).lower():
                    ticket_tree.insert('', index='end', values=i, tags=('evenrow',))
                elif list_record[5] in str(i[5]).lower():
                    ticket_tree.insert('', index='end', values=i, tags=('evenrow',))
    
    #Bind
    ticket_id_entry.bind("<KeyRelease>", search)
    staff_id_entry.bind("<KeyRelease>", search)
    name_entry.bind("<KeyRelease>", search)
    date_entry.bind("<KeyRelease>", search)
    email_entry.bind("<KeyRelease>", search)
    ticket_tree.bind("<ButtonRelease-1>", select_record)



menubar.add_command(label="Complain", command=complain_window)
menubar.add_command(label="Review TIcket", command=review_window)
window.mainloop()
