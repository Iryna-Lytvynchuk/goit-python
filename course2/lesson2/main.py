from collections import UserDict
from datetime import datetime, timedelta
import json


try:
    from helpers import *
except ModuleNotFoundError:
    from .helpers import  *

from abc import abstractmethod, ABC


path = 'data.json'


class Record:
    def __init__(self, name, surname, adress, note, tag, email, phone, birthday):
        self.name = name.value
        self.surname = surname.value
        self.adress = adress.value
        self.note = note.value
        self.tag = tag.value
        self.email = email.value
        self.phone = phone.value
        self.birthday = birthday.value

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


class Adress(Field):
    pass


class Note(Field):
    def __init__(self, note):
        list_note = note.split('.')
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
    def __init__(self, tag):
        list_tag = tag.split(',')
        self.__value = []
        self.value = list_tag

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, list_tag):
        for item in list_tag:
            self.__value.append(item.strip())


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
        list_numbers = str(numbers).split(',')
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
            self.__value = data
        except WrongDateFormat:
            self.flag = False
            print('Please, input birthday date in format "%d %m %Y" ')


classes = {
    'name': Name,
    'surname': Surname,
    'adress': Adress,
    'note': Note,
    'tag': Tag,
    'email': Email,
    'phone': Phone,
    'birthday': Birthday,
}


class AddressBook(UserDict):

    def add_info(self, name):
        data = self.get_data(self)
        if data:
            record = find_item(data, name)
            if record:
                field = input("Enter field: ")
                i = input("Enter new record: ")
                signature_cls = classes[field]
                check_value = signature_cls(i)
                value = check_value.value
                if value:
                    if type(record[name][field]) == list:
                        record[name][field].extend(value)
                        print(f'Note in record {record} changed successfully!')
                        self.save_data(self, data)
                    elif type(record[name][field]) == str:
                        record[name][field] += ',' + ' ' + value
                        print(f'Note in record {record} changed successfully!')
                        self.save_data(self, data)

            else:
                print('Name not found! Please, try again!')
        else:
            print('Database is empty!')

    def add_record(self, record):
        new_record = {record.name: {
            'surname': record.surname,
            'adress': record.adress,
            'note': record.note,
            'tag': record.tag,
            'email': record.email,
            'phone': record.phone,
            'birthday': record.birthday
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
        
        print(f'Record {new_record} added successfully!')


    def get_data(self):
        try:
            with open(path, 'r', encoding='utf8') as file:
                current_data = json.load(file)
            return current_data
        except FileNotFoundError:
            return None
    
    def save_data(self, data):
        with open(path, 'w', encoding='utf8') as file:
            json.dump(data, file, ensure_ascii=False)



class UserInterface(ABC):
    data = AddressBook.get_data(AddressBook)

    @abstractmethod
    def show(self):
        pass

class ShowMain(UserInterface):
    def show(self):
        data = AddressBook.get_data(AddressBook)
        print(show_table(data))


class ShowAll(UserInterface):
    def show(self):
        data = AddressBook.get_data(AddressBook)
        for idx, record in enumerate(data):
            print(idx + 1, '--', record, '\n')


class SortSurname(UserInterface):
    def show(self):
        data = AddressBook.get_data(AddressBook)
        sort_data = sort_surname(data)
        print(show_table(sort_data))


class SortNote(UserInterface):
    def show(self):
        data = AddressBook.get_data(AddressBook)
        sort_data = sort_len_note(data)
        print(show_table(sort_data))


class SortName(UserInterface):
    def show(self):
        data = AddressBook.get_data(AddressBook)
        sort_data = sort_name(data)
        print(show_table(sort_data))


class SortBirthday(UserInterface):
    def show(self):
        data = AddressBook.get_data(AddressBook)
        sort_data = sort_birthday(data)
        print(show_table(sort_data))


class FindTag(UserInterface):
    def __init__(self, tags):
        self.tags = tags

    def show(self):
        data = AddressBook.get_data(AddressBook)
        record = find_unit(data, 'tag', self.tags)
        if record:
            print(show_table(record))
        else:
            print('Tag not found! Please, try again!')


class FindNote(UserInterface):
    
    def __init__(self, words):
        self.words = words

    def show(self):
        data = AddressBook.get_data(AddressBook)
        record = find_unit(data, 'note', self.words)
        if record:
            print(show_table(record))
        else:
            print('Note not found! Please, try again!')


class Find(UserInterface):

    def __init__(self, name):
        self.name = name

    def show(self):
        data = AddressBook.get_data(AddressBook)
        record = find_item(data, self.name)
        if record:
            print(show_record(record))
        else:
            print('Name not found! Please, try again!')


class DeleteNote(UserInterface):

    def __init__(self, name):
        self.name = name
    
    def show(self):
        data = AddressBook.get_data(AddressBook)
        record = find_item(data, self.name)
        if record:
            record[self.name]['note'] = []
            print(f'Note in record {record} deleted successfully!')
            AddressBook.save_data(AddressBook, data)
        else:
            print('Name not found! Please, try again!')


class Delete(UserInterface):

    def __init__(self, name):
        self.name = name

    def show(self):
        data = AddressBook.get_data(AddressBook)
        record = find_item(data, self.name)
        if record:
            data.remove(record)
            print(f'Record {record} deleted successfully!')
            AddressBook.save_data(AddressBook, data)
        else:
            print('Name not found! Please, try again!')


class DaysToBirthday(UserInterface):
    
    def __init__(self, name):
        self.name = name

    birthday = None

    def show(self):
        data = AddressBook.get_data(AddressBook)
        for record in data:
            for key, value in record.items():
                if key == self.name:
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


class ChangeValue(UserInterface):
    def __init__(self, name, field, value):
        self.name = name
        self.field = field
        self.value = value
    
    def show(self):
        data = AddressBook.get_data(AddressBook)
        try:
            signature_cls = classes[self.field.lower()]
        except KeyError:
            print(f'Field {self.field} not found!')
            return
        check_value = signature_cls(self.value)
        value = check_value.value

        if value:
            try:
                record = find_item(data, self.name)
                idx = data.index(record)

                if self.field == 'name':
                    record[value] = record.pop(self.name)
                else:
                    for key in record[self.name]:
                        if key == self.field.lower():
                            record[self.name][key] = value
                data.pop(idx)
                data.append(record)
                AddressBook.save_data(AddressBook, data)

            except TypeError:
                print(f'Name {self.name} not found!')
                return

            print(f'Field {self.field} was changed successfully on {value}!')

'''
    def change(self, name, field, value):
        try:
            signature_cls = classes[field.lower()]
        except KeyError:
            print(f'Field {field} not found!')
            return
        check_value = signature_cls(value)
        value = check_value.value

        if value:
            data = self.get_data(self)
            try:
                record = find_item(data, name)
                idx = data.index(record)

                if field == 'name':
                    record[value] = record.pop(name)
                else:
                    for key in record[name]:
                        if key == field.lower():
                            record[name][key] = value
                data.pop(idx)
                data.append(record)
                self.save_data(self, data)
                    
                
            
            except TypeError:
                print(f'Name {name} not found!')
                return

            print(f'Field {field} was changed successfully on {value}!')

    def days_to_birthday(self, name):
        birthday = None
        data = self.get_data(self)
        if data:
            for record in data:
                for key, value in record.items():
                    if key == name:
                        birthday = datetime.strptime(value['birthday'], '%d %m %Y')
        else:
            print('Database is empty!')
            return

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
        if data:
            record = find_item(data, name)
            if record:
                data.remove(record)
                print(f'Record {record} deleted successfully!')
                self.save_data(self, data)
            else:
                print('Name not found! Please, try again!')
        else:
            print('Database is empty!')

    def delete_note(self, name):
        data = self.get_data(self)
        if data:
            record = find_item(data, name)
            if record:
                record[name]['note'] = []
                print(f'Note in record {record} deleted successfully!')
                self.save_data(self, data)
            else:
                print('Name not found! Please, try again!')
        else:
            print('Database is empty!')

    def find(self, name):
        data = self.get_data(self)
        if data:
            record = find_item(data, name)
            if record:
                print(show_record(record))
            else:
                print('Name not found! Please, try again!')
        else:
            print('Database is empty!')

    def find_note(self, words):
        data = self.get_data(self)
        if data:
            record = find_unit(data, 'note', words)
            if record:
                print(record)
            else:
                print('Note not found! Please, try again!')
        else:
            print('Database is empty!')

    def find_tag(self, tags):
        data = self.get_data(self)
        if data:
            record = find_unit(data, 'tag', tags)
            if record:
                print(record)
            else:
                print('Tag not found! Please, try again!')               
        else:
            print('Database is empty!')

    def get_sort_birthday(self):
        data = self.get_data(self)
        if data:
            sort_data = sort_birthday(data)
            print(show_table(sort_data))
        else:
            print('Database is empty!')

    def get_sort_name(self):
        data = self.get_data(self)
        if data:
            sort_data = sort_name(data)
            print(show_table(sort_data))
        else:
            print('Database is empty!')

    def get_sort_note(self):
        data = self.get_data(self)
        if data:
            sort_data = sort_len_note(data)
            print(sort_data)
        else:
            print('Database is empty!')

    def get_sort_surname(self):
        data = self.get_data(self)
        if data:
            sort_data = sort_surname(data)
            print(show_table(sort_data))
        else:
            print('Database is empty!')

    def show_all(self):
        if self.get_data(self):
            data = self.get_data(self)
            for idx, record in enumerate(data):
                print(idx + 1, record)
        else:
            print('Data not found!')

    def show_main(self):
        if self.get_data(self):
            data = self.get_data(self)
            print(show_table(data))
        else:
            print('Data not found!')
'''

def main():

    while True:
        action = input('Choose action: ')

        if action not in comands:
            print('Wrong action. Try again!')

        if action == 'add':

            name = input("Name:   ")
            name = Name(name)

            surname = input("Surname:   ")
            surname = Surname(surname)

            adress = input("Adress:   ")
            adress_cls = Adress(adress)

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
                    data = AddressBook.get_data(AddressBook)
                    if data:
                        if check_double(data, 'email', email):
                            break
                        else:
                            print(f'Email {email} used already!')
                    else:
                        break

            while True:
                phone = input("Phone format 380......... :   ")
                phone_cls = Phone(phone)
                if phone_cls.flag:
                    data = AddressBook.get_data(AddressBook)
                    if data:
                        if check_double(data, 'phone', phone):
                            break
                        else:
                            print(f'Phone {phone} used already!')
                    else:
                        break

            record = Record(name, surname, adress_cls, note, tag, email_cls, phone_cls, birthday_cls)
            AddressBook.add_record(AddressBook, record)

        elif action == 'add info':
            name = input('Enter the name of the contact where you want to add the note:   ')
            AddressBook.add_info(AddressBook, name)

        elif action == 'hello':
            print('Hello! Can I help you?')

        elif action == 'change':
            name = input("Name:    ")
            field = input("Field:   ")
            new_record = input("Enter new record:   ")
            ChangeValue.show(ChangeValue, name, field, new_record)

        elif action == 'show all':
            ShowAll.show(ShowAll)

        elif action == 'show':
            ShowMain.show(ShowMain)

        elif action == 'days':
            name = input("Enter the name:   ")
            DaysToBirthday.show(DaysToBirthday, name)

        elif action == 'delete':
            name = input('Enter the name of the contact you want to remove:   ')
            Delete.show(Delete, name)

        elif action == 'find':
            name = input('Enter the name of the contact you want to find:   ')
            Find.show(Find, name)

        elif action == 'delete note':
            name = input('Enter the name of the contact where you want to delete the note:   ')
            DeleteNote.show(DeleteNote, name)

        elif action == 'change note':
            name = input('Enter the name of the contact where you want to edit the note:   ')
            ChangeValue.show(ChangeValue, name)

        elif action == 'find note':
            words = input("Enter any word you want to find in the note:   ")
            FindNote.show(FindNote, words)    

        elif action == 'find tag':
            tags = input("Enter any word you want to find in the tag:   ")
            FindTag.show(FindTag, tags)

        elif action == 'sort name':
            SortName.show(SortName)

        elif action == 'sort surname':
            SortSurname.show(SortSurname)

        elif action == 'sort note':
            SortNote.show(SortNote)

        elif action == 'sort birthday':
            SortBirthday.show(SortBirthday)
    
        elif action == 'good bye' or action == 'close' or action == 'exit':
            print('Bye!')
            break


if __name__ == "__main__":
    print_comands()
    main() 