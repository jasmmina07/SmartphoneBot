from tinydb import TinyDB, Query

class DB:
    def __init__(self,path):
        self.db = TinyDB(path)

    def get_tables(self):
        """
        To get the list of all the tables in the database
        """
        tables = self.db.tables()
        return tables
        
    def get_phone(self,brand,idx):
        """
        Return phone data by brand
        args:
            brand: str
        return:
            dict
        """
        pass

    def get_phone_list(self,brand):
        """
        Return phone list
        """
        pass

    
if __name__ == "__main__":
    smartphone = DB("data.json")
    print(smartphone.get_tables())