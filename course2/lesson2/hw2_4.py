from abc import abstractmethod, ABC


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
