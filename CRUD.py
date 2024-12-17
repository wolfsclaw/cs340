from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps # TO convert pymongo Cursor object to

class CRUD(object):
    
    def __init__(self, USER, PASS):
        #USER = 'aacuser'
        #PASS = 'password1'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 34951
        DB = 'AAC'
        COL = 'animals'
        
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
        print("Connection Successful")
    
    def create(self, data):
        if data is not None:
            inserted = self.database.animals.insert_one(data)
            
            if inserted != 0:
                return True
            return False
        else:
            raise Exception("Nothing to save, data parameter is empty")
            
    def read(self, dataS):
        if dataS is not None:
            read = self.database.animals.find(dataS, {"_id": False})
        else:
            raise Exception("Nothing to read, dataS parameter is empty.")
        return read
    
    def update(self, dataS, dataU):
        if dataS and dataU is not None:
            updated = self.database.animals.update_many(dataS, {"$set": dataU})
        else:
            raise Exception("Nothing to udpate, dataS or dataU parameters are empty.")
            return updated.modified_count
            
    def delete(self, dataD):
        if dataD is not None:
            deleted = self.database.animals.delete_many(dataD)
        else:
            raise Exception("Nothing to delete, dataD parameter is empty.")
        return deleted.deleted_count
