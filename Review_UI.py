import Class
from tkinter import *
from tkinter import ttk
import Window_update


def review_window(window):
    Window_update.clear_window(window)

    def open():
        # get value from hash map for selected in treeview
        key = ticket_id_entry.get()
        record = Class.OpenTicketHash.get_val(key)

        # Top level UI
        ticket_detail_window = Toplevel()
        data_frame = LabelFrame(ticket_detail_window, text="Information")
        data_frame.pack(padx=10, pady=10, fill=X, expand=True)
        data_frame.columnconfigure(0, weight=1)
        data_frame.columnconfigure(1, weight=3)

        ticket_id_label = Label(data_frame, text="Ticket ID:")
        ticket_id_label.grid(row=0, column=0, padx=10, pady=10)
        ticket_id_entry2 = Entry(data_frame)
        ticket_id_entry2.grid(row=0, column=1, padx=10, pady=10)

        name_label = Label(data_frame, text="Name:")
        name_label.grid(row=0, column=2, padx=5, pady=5)
        name_entry = Entry(data_frame)  
        name_entry.grid(row=0, column=3, padx=5, pady=5)

        content_label = Label(data_frame, text="Description:")
        content_label.grid(row=1, column=0, padx=5, pady=5)
        content_text = Text(data_frame, width=50,height=10)
        content_text.grid(row=2, column=0, padx=5, columnspan=4)

        ticket_id_entry2.insert(END, key)
        name_entry.insert(END, record[1])
        content_text.insert("end-1c", record[5])
        ticket_id_entry2.config(state=DISABLED)
        name_entry.config(state=DISABLED)
        content_text.config(state=DISABLED)

        # Respond button
        def respond_ui():
            def respond_submit():
                Class.respond_to_ticket(key, respond_text.get("1.0", 'end-1c'))
                ticket_detail_window.destroy()
                ttk_list = Class.OpenTicketHash.list_all()
                Window_update.refresh_ticket(ttk_list, ticket_tree)
            respond_button.config(text="Submit", command=respond_submit)
            ticket_detail_window.config(height= 50)
            respond_label = Label(data_frame, text="Respond:")
            respond_label.grid(row=3, column=0, padx=5, pady=5)
            respond_text = Text(data_frame, width = 50, height = 10)
            respond_text.grid(row=4, column=0, padx=5, columnspan=4)
        
        respond_button = Button(ticket_detail_window,text= "Respond", command=respond_ui)
        respond_button.pack()

    def resolve():
        notification.set(Class.resolve_ticket(ticket_id_entry.get()))
        ttk_list = Class.OpenTicketHash.list_all()
        Window_update.refresh_ticket(ttk_list, ticket_tree)      
        
    # Review UI
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
    status_label.grid(row=2, column=2, padx=5, pady=5)
    status_entry = Entry(info_frame)
    status_entry.grid(row=2, column=3, padx=5, pady=5)

    open_button = Button(info_frame, text="Open", command=open)
    open_button.grid(row=0, column=4, padx=10, pady=10)

    resolve_button = Button(info_frame, text="Close Ticket",command=resolve)
    resolve_button.grid(row=1, column=4, padx=10, pady=10)

    notification = StringVar()
    notif_label = Label(info_frame, textvariable=notification)
    notif_label.grid(row=2, column=4, padx=10, pady=10)

    # Treeview
    cols = ["Ticket ID", "Staff ID", "Name", "Date", "Email", "Status"]
    style = ttk.Style()
    style.theme_use("default")  
    style.configure("Treeview", background="#D3D3D3", rowheight=25, foreground="black",
                    fieldbackground="#D3D3D3")
    style.map("Treeview", background=[("selected", "#347083")])
    table_frame = Frame(window)
    table_frame.pack(side=TOP, pady=20, padx=30)
    table_scroll = Scrollbar(table_frame)
    table_scroll.pack(side=RIGHT, fill=Y)
    ticket_tree = ttk.Treeview(table_frame, columns=cols, show="headings", yscrollcommand=table_scroll.set, height=15)
    ticket_tree.pack()
    table_scroll.config(command=ticket_tree.yview)

    ticket_tree.column(cols[0], anchor=W, width=80)
    ticket_tree.column(cols[1], anchor=W, width=80)
    ticket_tree.column(cols[2], anchor=W, width=100)
    ticket_tree.column(cols[3], anchor=W, width=100)
    ticket_tree.column(cols[4], anchor=W, width=200)
    ticket_tree.column(cols[5], anchor=W, width=70)

    for i in cols:
        ticket_tree.heading(i, text=i)

    ttk_list = Class.OpenTicketHash.list_all()
    Window_update.refresh_ticket(ttk_list, ticket_tree)

    # Feature
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

        list_record = (ticket_id_record, staff_id_record, name_record, date_record, email_record, status_record)

        ticket_tree.delete(*ticket_tree.get_children())
        if list_record[0] == "" and list_record[1] == "" and list_record[2] == "" and list_record[3] == "" \
                and list_record[4] == "":
            Window_update.refresh_ticket(Class.ticket_list, ticket_tree)  
        else:
            for ticket in Class.ticket_list:
                if list_record[0] in str(ticket[0]).lower():
                    ticket_tree.insert('', index='end', values=ticket, tags=('evenrow',))
                elif list_record[1] in str(ticket[1]).lower():
                    ticket_tree.insert('', index='end', values=ticket, tags=('evenrow',))
                elif list_record[2] in str(ticket[2]).lower():
                    ticket_tree.insert('', index='end', values=ticket, tags=('evenrow',))
                elif list_record[3] in str(ticket[3]).lower():
                    ticket_tree.insert('', index='end', values=ticket, tags=('evenrow',))
                elif list_record[4] in str(ticket[4]).lower():
                    ticket_tree.insert('', index='end', values=ticket, tags=('evenrow',))
                elif list_record[5] in str(ticket[5]).lower():
                    ticket_tree.insert('', index='end', values=ticket, tags=('evenrow',))
    
    # Bind
    ticket_id_entry.bind("<KeyRelease>", search)            ## to refresh the treeview every single charcater inputted
    staff_id_entry.bind("<KeyRelease>", search)
    name_entry.bind("<KeyRelease>", search)
    date_entry.bind("<KeyRelease>", search)
    email_entry.bind("<KeyRelease>", search)
    status_entry.bind("<KeyRelease>", search)
    ticket_tree.bind("<ButtonRelease-1>", select_record)    ## to select record
