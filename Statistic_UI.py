import Window_update
import Class
from tkinter import *

# To display total ticket submitted, open ticket, and closed ticket
def statistic_window(window):
    statistic_window = Toplevel()
    statistic_window.geometry("300x200")
    ticket_submitted = IntVar()
    closed_ticket = IntVar()
    open_ticket = IntVar()

    open_ticket.set(len(Class.OpenTicketHash.list_all()))
    closed_ticket.set(len(Class.ClosedTicketHash.list_all()))
    ticket_submitted.set(len(Class.OpenTicketHash.list_all())+len(Class.ClosedTicketHash.list_all()))


    Label(statistic_window, text="Tickets Submitted: ", padx=5, pady=5).pack()
    Label(statistic_window, textvariable=ticket_submitted, padx=5, pady=5).pack()
    Label(statistic_window, text="Open Ticket: ", padx=5, pady=5).pack()
    Label(statistic_window, textvariable=open_ticket, padx=5, pady=5).pack()
    Label(statistic_window, text="Closed Ticket: ", padx=5, pady=5).pack()
    Label(statistic_window, textvariable=closed_ticket, padx=5, pady=5).pack()