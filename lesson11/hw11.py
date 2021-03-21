from datetime import datetime
from collections import UserDict
import re


class Field:
    pass

class Name(Field):
    def __init__(self, name):
        
        self.name = name

    def __str__(self):
        return self.name    


class Phone(Field):
    
    def __init__(self, phone):
        self.__phone = None
        self.phone = phone

    def __str__(self):
        return self.phone

    @property
    def phone(self):
        return self.__phone   

    @phone.setter
    def phone(self, value):
        if len(value) != 10:
            raise Exception('Entered incorrectly')
        self.__phone = value

class Birthday:

    def __init__(self, birthday):
        self.__birthday = None
        self.birthday = birthday
    
    def __str__(self):
        return self.birthday
    
    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, value):
        if not (re.match(r'\d{4}/\d{2}/\d{2}', value)):
            raise Exception('Entered incorrectly')
        self.__birthday = value

class AddressBook(UserDict):
    data = list()
    MAX_VALUE = 3

    def __init__(self, Record, book):
        self.record = Record
        self.book = self.record.book
        self.index = 0

    def add_record(self):
        self.data.append(self.book)
        return self.data

    def __next__(self):
        if self.index < self.MAX_VALUE:
            self.index += 1
            return self.index
        raise StopIteration
        
    def __iter__(self):
        return self     


class Record():

    book = {}

    def add(self, name, phone, birthday):
        self.name = str(Name(name))
        self.phone = str(Phone(phone))
        self.birthday = str(Birthday(birthday))     
        self.book["name"] = self.name
        self.book["phone"] = self.phone
        self.book["birthday"] = self.birthday
        
        print(self.book)
        return self.book
        

    def hello(self):
        return 'How can I help you?'

    def change(self, name, phone):
        for value in self.book.values():
            if value == name:
                self.book["phone"] = phone
        
        print(self.book)

    def days_to_birthday(self, name, birthday):
        for value in self.book.values():
            if value == name:
                self.book["birthday"]  = birthday
            a = birthday.split("/")
            date_new = datetime(int(a[0]), int(a[1]), int(a[2]))
            current_data = datetime.now()
            b_day = datetime(current_data.year, date_new.month, date_new.day)
            count_date = (b_day - current_data.today()).days + 1
        print(f'Left until the birthday:  {count_date}')
     
    def show_all(self):
        for key, value in self.book.items():
            print(key, value)

    def bye(self):
        return 'Good bye!'    

def main():
    c = Record() 
    a = AddressBook(c, c.book)

    while True:
        action = input('Choose action: ')

        if action not in ('hello', 'add', 'change', 'show all', 'days', 'good bye', 'close', 'exit'):
            print('Wrong action. Try again!')
            continue
        if action == 'add':
            name = input("Name:   ")
            phone = input("Phone:   ")
            birthday = input("Birthday:  ")
            c.add(name, phone, birthday)
            continue
        elif action == 'hello':
            print(c.hello())
            continue
        elif action == 'change':
            name = input("Name:   ")
            phone = input("Phone:   ")
            c.change(name, phone)
            continue
        elif action == 'show all':
            show = a.add_record()
            print(show)
            continue
        elif action == 'days':
            name = input("Name:   ")
            c.days_to_birthday(name, birthday)
            continue
        elif action == 'good bye' or action == 'close' or action == 'exit':
            print(c.bye())
            break
        
if __name__ == "__main__":
    main() 


