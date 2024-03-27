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
   
        
    def resolve(self):
        pass

    def reopen(self):
        pass

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

    def respond(self,respond):
        self.respond_text = respond
        OpenTicketHash.set_val(self.ticket_id,(self.staff_id, self.name, self.date, self.email, self.status, self.content, self.respond_text))
        print(OpenTicketHash)



def respond_to_ticket(key, respond_text):
    value = OpenTicketHash.get_val(key)
    value_string = " ".join(j for j in value[0:6])
    staff_id, name, date, email, status, content = value_string.split()
    key = "".join(key)
    object_name_list = [value]
    for i in object_name_list[0]:
        i = Open_Ticket(staff_id, name, date, email, status, content, respond_text, key)
    i.respond()