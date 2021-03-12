from collections import UserDict


class AddressBook(UserDict):
    pass

class Record:

    book = {}

    def add(self, name, phone):
        self.book[name] = phone
        self.name = Name(name)
        self.phones = Phone(phone)

    def hello(self):
        return 'How can I help you?'

    def change(self, name, phone):
        for key, value in self.book.items():
            if key == name:
                value = phone
        self.book[name] = phone
        self.name = Name(name)
        self.phones = Phone(phone)
        print(self.book)
  
     
    def show_all(self):
        for key, value in self.book.items():
            print(key, value)

    def bye(self):
        return 'Good bye!'    

class Field:
    pass

class Name(Field):
    def __init__(self, name):
        self.name = name



class Phone(Field):
    phones = list()

    def __init__(self, phone):
        if type(phone) == 'str':
            self.phones.append(phone)
        elif type(phone) == 'list':
            self.phones = phone


def main():
    c = Record()
    while True:
        action = input('Choose action: ')

        if action not in ('hello', 'add', 'change', 'show all', 'good bye', 'close', 'exit'):
            print('Wrong action. Try again!')
            continue

        if action == 'add':
            name = input("Name:   ")
            phone = input("Phone:   ")
            c.add(name, phone)
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
            c.show_all()
            continue
        elif action == 'good bye' or action == 'close' or action == 'exit':
            print(c.bye())
            break
        
if __name__ == "__main__":
    main() 


