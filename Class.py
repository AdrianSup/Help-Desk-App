class Hash_Ticket:
    def __init__(self, size):
        self.size = size                    ## total of list in the hash map
        self.keys = []                      ## store all keys inputted
        self.ticket_list = []               ## store all key,value in to 2D list for treeview
        self.table = self.create_buckets()  ## hash map table
    
    def create_buckets(self):
        return [[] for _ in range(self.size)] ## create a table of [] in the range of size
    
    def set_val(self, key, value):              ## to input a value to one of the [] in the table
        hashed_key = hash(key) % self.size      ## determine a place of a key in the table from the reminder of hash(key) / size
        self.keys.append(key)                   ## store the key into keys list
        bucket = self.table[hashed_key]         ## direct the focus into determined []

        found_key = False
        for index,record in enumerate(bucket):  ## iterate through all the keys on the table and check if the key provided now match
            record_key, record_val = record
            if record_key == key :
                found_key = True
                break
        
        if found_key:                           ## if the key is already in the table, replace value
            bucket[index] = (key, value)
        else:
            bucket.append((key,value))

    def get_val(self, key):                     ## to get the value by key
        hashed_key = hash(key) % self.size

        bucket = self.table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                found_key = True
                break
        
        if found_key:
            return record_val
        else:
            return "Not Found"
        
    def delete_val(self, key):                  ## to delete a pair of key,value by key
        hashed_key = hash(key) % self.size
        bucket = self.table[hashed_key]

        found_key = False
        for index,record in enumerate(bucket):
            if record == key:
                found_key = True
                break

        if found_key:
            bucket.pop(index)

    def list_all(self):                             ## to change the table into a 2D list
        for keys in self.keys:
            hashed_keys = hash(keys) % self.size
            bucket = self.table[hashed_keys]
            for index,record in enumerate(bucket):  ## record return multiple list on the hash table
                container = []
                for i in record:                    ## i return a the value of 1 list at a time (example: ['2001', (value, value, value,...)])
                    if type(i) is tuple:
                        for j in i:                 ## j return the value inside the tuple
                            container.append(j)
                    else:
                        container.append(i)         ## combine the key with the value into a single list
                self.ticket_list.append(container)
        return self.ticket_list                     ## return a 2D list (example: [['2001', 'value', 'value'], ['2002', 'value', 'value'], ...])

    def __str__(self):                                      ## to show the table when print()
        return "".join(str(item) for item in self.table)


OpenTicketHash = Hash_Ticket(30)
ClosedTicketHash = Hash_Ticket(30)


counter = 2000  ## static counter for Ticket ID

class Ticket:
    # Ticket basic information and constructor
    def __init__(self, staff_id, name, date, email, status, content):
        global counter
        counter += 1
        self.ticket_id = str(counter)
        self.staff_id = staff_id
        self.name = name
        self.date = date
        self.email = email
        self.content = content
        self.status = status
        

    # Ticket methods
    def submit(self):
        OpenTicketHash.set_val(self.ticket_id,(self.staff_id, self.name, self.date, self.email, self.status, self.content))

    def respond(self):
        pass

    def resolve(self):
        pass

    def reopen(self):
        pass

    def pass_change(self):
        pass
