import tkinter

ticket_list = []
class Ticket:
    # Ticket basic information and constructor
    def __init__(self, ticket_id, staff_id, name, date, email, status, content):
        self.ticket_id = ticket_id
        self.staff_id = staff_id
        self.name = name
        self.date = date
        self.email = email
        self.content = content
        self.status = status

    # Ticket methods
    def submit(self):
        ticket_now = (self.ticket_id, self.staff_id, self.name, self.date, self.email, self.status, self.content)
        ticket_list.append(ticket_now)
        print((ticket_now, ticket_list))

    def respond(self):
        pass

    def resolve(self):
        pass

    def reopen(self):
        pass

    def pass_change(self):
        pass
    