from collections import UserDict
from datetime import datetime, timedelta
import json
import pickle

from helpers import check_birthday_date, WrongDateFormat, check_phone_number, WrongPhoneNumberFormat, check_valid_email, WrongEmailFormat, comands

path = 'data.json'


class AddressBook(UserDict):
    def get_data(self):
        try:
            with open(path, 'r', encoding='utf8') as file:
                current_data = json.load(file)
            return current_data
        except FileNotFoundError:
            return None

    def add_record(self, record):
        new_record = {record.name: {
            'surname': record.surname,
            'note': record.note,
            'tag': record.tag,
            'email': record.email,
            'phone': record.phone,
            'birthday': record.birthday.strftime('%d %m %Y')
        }}

        if self.get_data(self):
            current_data = self.get_data(self)
            current_data.append(new_record)
            with open(path, 'w', encoding='utf8') as file:
                json.dump(current_data, file, ensure_ascii=False)
        else:
            # First save
            with open(path, 'w', encoding='utf8') as file:
                json.dump([new_record], file, ensure_ascii=False)
        
    def iterator(self, record_count):
        result = ''

        if record_count > len(self.data):
            print(f'Max count item {len(self.data)}')
        elif record_count == len(self.data):
            print(self.__str__())
        else:
            for key, value in self.data.items():
                if record_count:
                    result += f'{key}: {value} \n'
                    record_count -= 1
                else:
                    print(result)
                    break

    def save_data(self, path):
        with open(path, 'wb') as file:
            pickle.dump(self.data, file)

    def load_data(self, path):
        with open(path, 'rb') as file:
            self.data = pickle.load(file)

    def get_user_list(self, input_data=None):
        user_list = []
        input_data = str(input_data).lower()
        for name, value in self.data.items():
            try:
                if str(name).lower().find(input_data) >= 0:
                    user_list.append([name, str(value)])
                for phone in value.phones:
                    if input_data in str(phone):
                        user_list.append([name, str(value)])
            except AttributeError:
                continue

        if user_list:
            print(user_list)
        else:
            print('User was not found')

    def __str__(self):
        result = ''
        for key, value in self.data.items():
            result += f'{key}: {value} \n'
        return result


    def show_all(self):
        if self.get_data(self):
            data = self.get_data(self)
            for idx, record in enumerate(data):
                print(idx + 1, record)
        else:
            print('Data not found!')

    def days_to_birthday(self, name):
        birthday = None
        data = self.get_data(self)
        for record in data:
            for key, value in record.items():
                if key == name:
                    birthday = datetime.strptime(value['birthday'], '%d %m %Y')  
        if birthday:
            date_with_current_year = birthday.replace(year=datetime.now().year)
            if date_with_current_year > datetime.now():
                dif = date_with_current_year - datetime.now()
                print(f'{dif.days} days')
            else:
                year_delta = timedelta(days=365)
                dif = (date_with_current_year + year_delta) - datetime.now()
                print(f'{dif.days} days')
        else:
            print('Name not found! Please, try again!')


    def delete(self, name):
        data = self.get_data(self)
        for record in data:
            for key, value in record.items():
                if key == name:
                    del record[name]
                    print(data)
                else:
                    print('Name not found! Please, try again!')#выводит кол.раз сколько контактов (нужна правка) и сохр.в файл
    
    def find(self, name):
        data = self.get_data(self)
        for record in data:
            for key, value in record.items():
                if key == name:
                    print(record)
                else:
                    print('Name not found! Please, try again!')#выводит кол.раз сколько контактов (нужна правка)

    def delete_note(self, name):
        data = self.get_data(self)
        for record in data:
            for key, value in record.items():
                if key == name:
                    print(record)
                    del record[name]["note"]
                    print(record)#сделать сохр.в файл

    def change_note(self, name):
        data = self.get_data(self)
        for record in data:
            for key, value in record.items():
                if key == name:
                    print(record)
                    for i in value["note"]:
                        value["note"].clear()
                        i = input("Enter new note: ")
                        value["note"].append(i)
                        print(record)#сделать сохр.в файл

    def find_note(self, words):
        data = self.get_data(self)
        for record in data:
            for key, value in record.items():
                for i in value["note"]:
                    if i.find(words) != -1:
                        print(record)

    def add_note(self, name):
        data = self.get_data(self)
        for record in data:
            for key, value in record.items():
                if key == name:
                    print(record)
                    for i in value["note"]:
                        note_new = input("Enter note: ")
                        value["note"].append(note_new)
                        print(record)
                        break#сделать сохр.в файл
                            
          
class Record:
    def __init__(self, name, surname, note, tag, email, phone, birthday):
        self.name = name.value
        self.surname = surname.value
        self.note = note.value
        self.tag = tag.value
        self.email = email.value
        self.phone = phone.value
        self.birthday = birthday.value

    def add_data(self, field, *data):
        if field == 'birthday':
            b = Birthday(str(*data))
            self.birthday = b.value
        else:
            p = Phone(data)
            p.value = data
            if len(p.value) == 1:
                self.phone.append(p.value[0])
            else:
                for item in p.value:
                    self.phone.append(item)

    def delete_data_in_field(self, field):
        if field == 'birthday':
            self.birthday = None
        else:
            self.phones.clear()

    def days_to_birthday(self):
        date_with_current_year = self.birthday.replace(year=datetime.now().year)
        if date_with_current_year > datetime.now():
            dif = date_with_current_year - datetime.now()
            print(f'{dif.days} days')
        else:
            year_delta = timedelta(days=365)
            dif = (date_with_current_year + year_delta) - datetime.now()
            print(f'{dif.days} days')

    def __str__(self):
        return f'surname: {self.surname}, note: {self.note}, tag: {self.tag}, email: {self.email}, phone: {self.phone}, birthday: {self.birthday}'


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Surname(Field):
    pass


class Note(Field):
    
    def __init__(self, note):
        list_note = note.split(',')
        self.__value = []
        self.value = list_note

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, list_note):
        for item in list_note:
            self.__value.append(item.strip())


class Tag(Field):
    pass


class Email(Field):
    flag = True
    def __init__(self, email):
        list_email = email.split(',')
        self.__value = []
        self.value = list_email

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, list_email):
        for item in list_email:
            try:    
                check_valid_email(item.strip())
                self.__value.append(item.strip())
            except WrongEmailFormat: 
                self.flag = False
                print(f'Email "{item}" not valid!')

class Phone(Field):
    flag = True
    def __init__(self, numbers):
        list_numbers = numbers.split(',')
        self.__value = []
        self.value = list_numbers

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, list_numbers):

        for item in list_numbers:
            try:
                check_phone_number(item.strip())
                if item not in self.__value:
                    self.__value.append(item.strip())
            except WrongPhoneNumberFormat:
                self.flag = False
                print(f'Number {item} is not valid! Please, enter number in format 380_________')


    def __str__(self):
        return f'Phone: {self.__value}'


class Birthday(Field):
    flag = True
    def __init__(self, value):
        self.__value = None
        self.value = value

    def __getitem__(self, key=None):
        return self.__value

    def __setitem__(self, key, value):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, data):
        try:
            check_birthday_date(data)
            self.__value = (datetime.strptime(data, '%d %m %Y'))
        except WrongDateFormat:
            self.flag = False
            print('Please, input birthday date in format "%d %m %Y" ')

    # def __str__(self):
    #     return f'Birthday: {self.__value}'


while True:
    action = input('Choose action: ')

    if action not in comands:
        print('Wrong action. Try again!')

    if action == 'add':

        name = input("Name:   ")
        name = Name(name)

        surname = input("Surname:   ")
        surname = Surname(surname)

        note = input("Note/s:   ")
        note = Note(note)

        tag = input("Tag/s:   ")
        tag = Tag(tag)

        while True:
            birthday = input("Birthday:  ")
            birthday_cls = Birthday(birthday)
            if birthday_cls.flag:
                break
            
        while True:
            email = input("Email:   ")  
            email_cls = Email(email)
            if email_cls.flag:
                break

        while True:
            phone = input("Phone format 380......... :   ")
            phone_cls = Phone(phone)
            if phone_cls.flag:
                break

        record = Record(name, surname, note, tag, email_cls, phone_cls, birthday_cls)
        AddressBook.add_record(AddressBook, record)


    elif action == 'hello':
        print('Hello! Can I help you?')


    elif action == 'change':
        field = input("Field:   ")
        new_record = input("New record:   ")
        AddressBook.change(field, new_record)

    elif action == 'show all':
        AddressBook.show_all(AddressBook)

    elif action == 'days':
        name = input("Name:   ")
        AddressBook.days_to_birthday(AddressBook, name)

#добавить новые команды в список
    elif action == 'delete':
        name = input('Введите имя контакта, которое нужно удалить: ')
        AddressBook.delete(AddressBook, name)

    elif action == 'find':
        name = input('Введите имя контакта, которое нужно найти: ')
        AddressBook.find(AddressBook, name)

    elif action == 'delete note':
        name = input('Введите имя контакта, в котором нужно удалить запись: ')
        AddressBook.delete_note(AddressBook, name)

    elif action == 'change note':
        name = input('Введите имя контакта, в котором нужно изменить запись: ')
        AddressBook.change_note(AddressBook, name)

    elif action == 'find note':
        words = input("Some words:  ")
        AddressBook.find_note(AddressBook, words)    
        
    elif action == 'add note':
        name = input('Введите имя контакта, в котором нужно изменить запись: ')
        AddressBook.add_note(AddressBook, name)


    # elif action == 'choose':
    #     words = input("Some words:  ")
    #     for i in a.data:
    #         for key, value in i.items():
    #             if value.find(words) != -1:
    #                 print(c.book) 

    #elif action == 'good bye' or action == 'close' or action == 'exit':
     #   print('Bye!')
      #  break


