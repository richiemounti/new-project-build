import json

parties = {}

class Party():
    def __init__(self, name, hqAddress, logoUrl, id=0):
        self.name = name
        self.hqAddress = hqAddress
        self.logoUrl = logoUrl
        self.id = self.create_id()

    def serialize(self):
        return {
            'id' : self.id,
            'name': self.name, 
            'hqAddress': self.hqAddress,
            'logoUrl': self.logoUrl,
        }

    def create_id(self, id=0):
        if id == 0:
            id = len(parties)+1
        
        if id in parties:
            id = id+1
            return self.create_id(id)
        return id

    def party_dict(self):
        return dict(id=self.id)

    def detail_list(self):
        return dict(id=self.id, name=self.name, hqAddress=self.hqAddress , logoUrl=self.logoUrl)
    
    def get_parties(self):
        return dict(id=self.id, name=self.name, logoUrl=self.logoUrl)
    
    def save_party(self):
        parties[self.id] = self

    def update_name(self, name, hqAddress):
        self.name = name
        self.hqAddress = hqAddress

    def delete_party(self):
        del parties[self.id]
    
    def delete_parties(self):
        parties.clear()

    def check_name(self, name=None):
        if name == None:
            name = self.name
        for x in parties:
            if parties[x].name == name:
                return x
        return False

