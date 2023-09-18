from tinydb import TinyDB, Query
from telegram import update, InlineKeyboardButton, InlineKeyboardMarkup
class DB:
    def __init__(self,path):
        self.db = TinyDB(path)

    def phone_photo(self,brand,idx):
        table=self.db.table(brand)
        phone=table.get(doc_id=idx)
        text=f"name: {phone['name']}\nprice: {phone['price']} $\ncolor: {phone['color']} "
        return phone["img_url"],text



    def products(self,brand,query):
        data=list(self.db.table(brand))
        a=[]
        buttons=[]
        for i in range(0,10):
            button=InlineKeyboardButton(text=data[i]['name'],callback_data=i+1)
            a.append(button)
            buttons.append(a)
            a=[]
        back=InlineKeyboardButton(text="⬅️ back",callback_data="back_brands")
        a.append(back)
        buttons.append(a)
        keyboard=InlineKeyboardMarkup(buttons)
        query.edit_message_text(text=brand,reply_markup=keyboard)
    
    def data_back_shop(self,query):
        Shop=InlineKeyboardButton(text="🛍 Shop",callback_data="Shop")
        Cart=InlineKeyboardButton(text="📦 Cart",callback_data="Cart")
        Contact=InlineKeyboardButton(text="📞 Contact",callback_data="Contact")
        About=InlineKeyboardButton(text="📝 About",callback_data="About")

        keyboard=InlineKeyboardMarkup([[Shop,Cart],[Contact,About]])
        query.edit_message_text(text="Smartphone shop",reply_markup=keyboard)
        return keyboard
    
    def data_shop(self,query):
        Apple=InlineKeyboardButton(text="Apple",callback_data="Apple")
        Huawei=InlineKeyboardButton(text="Huawei",callback_data="Huawei")
        Nokia=InlineKeyboardButton(text="Nokia",callback_data="Nokia")
        Oppo=InlineKeyboardButton(text="Oppo",callback_data="Oppo")
        Redmi=InlineKeyboardButton(text="Redmi",callback_data="Redmi")
        Samsung=InlineKeyboardButton(text="Samsung",callback_data="Samsung")
        Vivo=InlineKeyboardButton(text="Vivo",callback_data="Vivo")
        back=InlineKeyboardButton(text="⬅️ back",callback_data="back")
        keyboard=InlineKeyboardMarkup([[Apple],[Huawei],[Nokia],[Oppo],[Redmi],[Samsung],[Vivo],[back]])
        query.edit_message_text(text="Choose a brand",reply_markup=keyboard)
        return keyboard

    def get_tables(self):
        """
        To get the list of all the tables in the database
        """
        tables = self.db.tables()
        return list(tables)
        
    def get_phone(self):
        """
        Return phone data by brand
        args:
            brand: str
        return:
            dict
        """

        # phone=self.db.table(brand)
        # return phone.get(doc_id=idx)
        phone=["Apple","Huawei","Nokia","Oppo","Redmi","Samsung","Vivo"]
        return phone

    def get_phone_list(self,brand):
        """
        Return phone list
        """

        phone = self.db.table(brand)
        return phone.all()


    
if __name__ == "__main__":
    smartphone = DB("data.json")

    tables = smartphone.get_tables()
    brand = tables[0]
    phones = smartphone.get_phone_list(brand)

    phone = phones[4]
    doc_id = phone.doc_id
    print(smartphone.get_phone(brand, doc_id))
