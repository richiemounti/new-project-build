import json

offices = {}
officeTypes = ['federal', 'legislative', 'state', 'local government']

class Office():
    def __init__(self, name, type, id=0):
        self.name = name
        self.type = type
        self.id = self.create_id()

    def serialize(self):
        return {
            'id' : self.id,
            'name': self.name, 
            'type': self.type,
        }

    def create_id(self, id=0):
        if id == 0:
            id = len(offices)+1
        
        if id in offices:
            id = id+1
            return self.create_id(id)
        return id

    def office_list(self):
        return dict(id=self.id, name=self.name, type=self.type)

    def office_dict(self):
        return dict(id=self.id)
    
    def save_office(self):
        offices[self.id] = self

    def update_name(self, name, type):
        self.name = name
        self.type = type

    def check_name(self, name=None):
        if name == None:
            name = self.name
        for x in offices:
            if offices[x].name == name:
                return x
        return False
