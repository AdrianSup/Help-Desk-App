class Hash_Ticket:
    def __init__(self, size):
        self.size = size                    ## total of list in the hash map
        self.keys = []                      ## store all keys inputted              
        self.table = self.create_buckets()  ## hash map table
    
    def create_buckets(self):
        return [[] for _ in range(self.size)] ## create a table of [] in the range of size
    
    def set_val(self, key, value):              ## to input a value to one of the [] in the table
        hashed_key = hash(key) % self.size      ## determine a place of a key in the table from the reminder of hash(key) / size
        if key not in self.keys:
            self.keys.append(key)               ## store the key into keys list if it's a new key
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
        self.keys.remove(key)
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
        self.ticket_list = []                       ## store all key,value in to 2D list for treeview
        for keys in self.keys:
            hashed_keys = hash(keys) % self.size
            bucket = self.table[hashed_keys]
            for index,record in enumerate(bucket):  ## record return multiple list on the hash table
                record_key, record_val = record
                if record_key == keys:                  ## finding the right vakue to the key
                    container = []
                    for i in record:                    ## i return a the value of 1 list at a time (example: ['2001', (value, value, value,...)])
                        if type(i) is tuple:
                            for j in i:                 ## j return the value inside the tuple
                                container.append(j)
                        else:
                            container.append(i)         ## combine the key with the value into a single list
                    self.ticket_list.append(container)
        print(self.ticket_list)
        return self.ticket_list                     ## return a 2D list (example: [['2001', 'value', 'value'], ['2002', 'value', 'value'], ...])

    def __str__(self):                                      ## to show the table when print()
        return "".join(str(item) for item in self.table)
