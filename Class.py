import Ticket_list

# Hash map for both open and closed ticket (30 spaces for each)
OpenTicketHash = Ticket_list.Hash_Ticket(30)
ClosedTicketHash = Ticket_list.Hash_Ticket(30)


counter = 2000  ## static counter for Ticket ID

# Parent class for abstract
class Ticket:
    # Ticket basic information and constructor
    def __init__(self, staff_id, name, date, email, status, content):
        self.staff_id = staff_id
        self.name = name
        self.date = date
        self.email = email
        self.content = content
        self.status = status
        
    # Ticket str for print()
    
    def __str__(self):
        return (self.ticket_id, self.staff_id, self.name, self.date, self.email, self.content, self.status, self.respond_text)

# Open Ticket Sub-Class
class Open_Ticket(Ticket):
    def __init__(self, staff_id, name, date, email, status, content):
        super().__init__(staff_id, name, date, email, status, content)
    
    # Submit to create a record on hashmap
    def submit(self, *ticket_id):
        if ticket_id:
            self.ticket_id = "".join(ticket_id)
        else:
            global counter
            counter += 1
            self.ticket_id = str(counter)
        OpenTicketHash.set_val(self.ticket_id,(self.staff_id, self.name, self.date, self.email, self.status, self.content))

    # Respond to a Ticket and update to hashmap
    def respond(self,respond,ticket_id):
        self.respond_text = respond
        self.ticket_id = ticket_id
        self.status = "Responded"           ## mark ticket as responded in status
        OpenTicketHash.set_val(self.ticket_id,(self.staff_id, self.name, self.date, self.email, self.status, self.content, self.respond_text))
        print(OpenTicketHash)

    # Resolve a ticket, close it, and move it to closed ticket hash map
    def resolve(self, ticket_id, respond): 
        self.status = "Closed"
        self.respond_text = respond
        self.ticket_id = ticket_id
        OpenTicketHash.delete_val(ticket_id)    ## move the ticket to closed ticket hashmap as archive
        ClosedTicketHash.set_val(self.ticket_id,(self.staff_id, self.name, self.date, self.email, self.status, self.content, self.respond_text))
        print(ClosedTicketHash)

# Closed Ticket Sub-Class
class Closed_Ticket(Ticket):
    def __init__(self,ticket_id, staff_id, name, date, email, status, content, respond):
        super().__init__(staff_id, name, date, email, status, content)
        self.ticket_id = ticket_id
        self.respond_text = respond
    
    # Move the record to Open hash after reopen the ticket
    def reopen(self):
        ClosedTicketHash.delete_val(self.ticket_id)
        OpenTicketHash.set_val(self.ticket_id, (self.staff_id, self.name, self.date, self.email, self.status, self.content, self.respond_text))

# Password change request ticket Sub-Sub-Class
class Password_Ticket(Open_Ticket):
    def __init__(self, staff_id, name, date, email, status, content):
        super().__init__(staff_id, name, date, email, status, content)

    # Automatically call Respond and Resolve with generated password as responds
    def submit(self, *ticket_id):
        super().submit(*ticket_id)
        respond = str(self.staff_id[:2])+str(self.name[:3])
        super().respond(respond, self.ticket_id)
        super().resolve(self.ticket_id, self.respond_text)

# Function for calling the function inside classes with correct record from hashmap    
def respond_to_ticket(key, respond_text):
    value = OpenTicketHash.get_val(key)     ## Get record from hash
    if value == "Not Found":                ## if record is not found return "Not Found"
        return value
    if len(value) > 6:                      ## if a ticket is Re-Opened, it has a record for past responds.
        value = list(value)                 ## This if statement to check it and remove the old responds
        value.pop(-1)
    ticket = Open_Ticket(*value)            ## create an object based on record
    key = "".join(key)
    ticket.respond(respond_text, key)       ## call respond function inside Open_Ticket Class to update to new responds

def resolve_ticket(key):
    value = OpenTicketHash.get_val(key)     ## Get record from hash
    if value == "Not Found":                ## if record is not found return "Not Found"
        return value
    ticket = Open_Ticket(*value[0:6])       ## Create an object based on record
    key = "".join(key)
    if len(value) > 6:                      ## if statement to check "Responds" availability
        ticket.resolve(key,value[6])        ## Call resolve function in Open_Ticket Class
        return "Ticket closed"              ## return string for notification
    else:
        return "Not responded yet"          ## retrun string for notification
    
    
