from pymongo import MongoClient

class mongoConnect2:
    db_url = "mongodb://esupport:esu#&p@ausdlesmgdb01.us.dell.com:27100/admin?connect=replicaSet"
    db_name = "esupport"
    collection_name = "log"

    def __init__(self):
        try:
            self.Client = MongoClient(self.db_url, maxPoolSize=100)
            print('Connection established!')
        except Exception as e:
            print('Connection failed due to an error! Error: ',e)

    def push_to_db(self, list_of_items):
        collection = self.Client[self.db_name][self.collection_name]
        try:
            collection.insert_many(list_of_items)
            print('Successfully pushed the documents!')
        except:
            print('Connection Error')
