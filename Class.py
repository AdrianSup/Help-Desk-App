import Ticket_list

OpenTicketHash = Ticket_list.Hash_Ticket(30)
ClosedTicketHash = Ticket_list.Hash_Ticket(30)


counter = 2000  ## static counter for Ticket ID

class Ticket:
    # Ticket basic information and constructor
    def __init__(self, staff_id, name, date, email, status, content):
        self.staff_id = staff_id
        self.name = name
        self.date = date
        self.email = email
        self.content = content
        self.status = status
        
    # Ticket methods
    

    def pass_change(self):
        pass
    
    def __str__(self):
        return (self.ticket_id, self.staff_id, self.name, self.date, self.email, self.content, self.status, self.respond_text)


class Open_Ticket(Ticket):
    def __init__(self, staff_id, name, date, email, status, content):
        super().__init__(staff_id, name, date, email, status, content)
    
    def submit(self, *ticket_id):
        if ticket_id:
            self.ticket_id = "".join(ticket_id)
        else:
            global counter
            counter += 1
            self.ticket_id = str(counter)
        OpenTicketHash.set_val(self.ticket_id,(self.staff_id, self.name, self.date, self.email, self.status, self.content))

    def respond(self,respond,ticket_id):  ## put a respond into the ticket
        self.respond_text = respond
        self.ticket_id = ticket_id
        self.status = "Responded"           ## mark ticket as responded in status
        OpenTicketHash.set_val(self.ticket_id,(self.staff_id, self.name, self.date, self.email, self.status, self.content, self.respond_text))
        print(OpenTicketHash)

    def resolve(self, ticket_id, respond):  ## to close the case and archive it for a chance to reopen
        self.status = "Closed"
        self.respond_text = respond
        self.ticket_id = ticket_id
        OpenTicketHash.delete_val(ticket_id)    ## move the ticket to closed ticket hashmap as archive
        ClosedTicketHash.set_val(self.ticket_id,(self.staff_id, self.name, self.date, self.email, self.status, self.content, self.respond_text))
        print(ClosedTicketHash)

class Closed_Ticket(Ticket):
    def __init__(self,ticket_id, staff_id, name, date, email, status, content, respond):
        super().__init__(staff_id, name, date, email, status, content)
        self.ticket_id = ticket_id
        self.respond_text = respond
    
    def reopen(self):
        ClosedTicketHash.delete_val(self.ticket_id)
        OpenTicketHash.set_val(self.ticket_id, (self.staff_id, self.name, self.date, self.email, self.status, self.content, self.respond_text))

class Password_Ticket(Open_Ticket):
    def __init__(self, staff_id, name, date, email, status, content):
        super().__init__(staff_id, name, date, email, status, content)

    def submit(self, *ticket_id):
        super().submit(*ticket_id)
        respond = str(self.staff_id[:2])+str(self.name[:3])
        super().respond(respond, self.ticket_id)
        super().resolve(self.ticket_id, self.respond_text)

        
def respond_to_ticket(key, respond_text):
    value = OpenTicketHash.get_val(key)
    if len(value) > 6:
        value = list(value)
        value.pop(-1)
    ticket = Open_Ticket(*value) 
    key = "".join(key)
    ticket.respond(respond_text, key)

def resolve_ticket(key):
    value = OpenTicketHash.get_val(key)
    ticket = Open_Ticket(*value[0:6])
    key = "".join(key)
    if len(value) > 6:
        print("-------------------")
        print(value[6])
        ticket.resolve(key,value[6])
        return "Ticket closed"
    else:
        return "Not responded yet"
    
    
