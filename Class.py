class Ticket:
    # Ticket basic information and constructor
    def __init__(self, ticket_id, staff_id, name, email, content, status):
        self.ticket_id = ticket_id
        self.staff_id = staff_id
        self.name = name
        self.email = email
        self.content = content
        self.status = status

    # Ticket methods
    def submit(self):
        pass

    def respond(self):
        pass

    def resolve(self):
        pass

    def reopen(self):
        pass

    def pass_change(self):
        pass
