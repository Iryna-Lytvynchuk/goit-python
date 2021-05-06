from datetime import datetime
import re

comands = ('hello', 'add', 'add info', 'change', 'close', 'days', 'delete', 'delete note', 'exit', 'find', 'find note', 'find tag', 'good bye', 'show', 'show all', 'sort birthday', 'sort name', 'sort note', 'sort surname')

class WrongDateFormat(Exception):
    pass


class WrongPhoneNumberFormat(Exception):
    pass


class WrongEmailFormat(Exception):
    pass

def check_birthday_date(date):
    BIRTH_REG = re.compile(r"(\d{2})\s(\d{2})\s(\d{4})")

    if BIRTH_REG.match(date):
        return True
    else:
        raise WrongDateFormat


def check_phone_number(number):
    PHONE_REGEX = re.compile(r"^380\d{2}\d{7}$")

    if PHONE_REGEX.match(str(number)):
        return True
    else:
        raise WrongPhoneNumberFormat


def check_valid_email(email):
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

    if EMAIL_REGEX.match(str(email)):
        return True
    else:
        raise WrongEmailFormat


def find_item(data, item):
    for record in data:
        for key, value in record.items():
            if key == item:
                return record

def find_unit(data, unit, item):
    found_records_list = []
    for record in data:
        for key, value in record.items():
            for i in value[unit]:
                if i.lower().find(item.lower()) != -1:
                    found_records_list.append(record)      

    return found_records_list           

def show_table(data):
    width = 15
    width_isx = 3
    width_email = 30
    string_files = ''
    for idx, record in enumerate(data):
        for name, value in record.items():
            string_files += '| {:^{width_isx}} | {:^{width}} | {:^{width}} | {:^{width_email}} | {:^{width}} | {:^{width}} | \n'.format(idx + 1, name, value['surname'], value['email'][0], value['phone'][0], value['birthday'], width_isx=width_isx, width=width, width_email=width_email)
    title = '| {:^{width_isx}} | {:^{width}} | {:^{width}} | {:^{width_email}} | {:^{width}} | {:^{width}} |'.format('ID', 'Name', 'Surname', 'Email', 'Phone', 'Birthday', width_isx=width_isx, width=width, width_email=width_email)
    line = '=' * len(title)
    header = line + '\n' + title + '\n' + line + '\n'
    end = '{:=^{width}}'.format('END', width=len(title))
    table = header + string_files + end
    return table

def show_record(record):
    width = 15
    width_idx = 3
    width_email = 30
    string_files = ''
    for name, value in record.items():
        string_files += '| {:^{width}} | {:^{width}} | {:^{width_email}} | {:^{width}} | {:^{width}} | \n'.format(name, value['surname'], value['email'][0], value['phone'][0], value['birthday'], width_idx=width_idx, width=width, width_email=width_email)
    title = '| {:^{width}} | {:^{width}} | {:^{width_email}} | {:^{width}} | {:^{width}} |'.format('Name', 'Surname', 'Email', 'Phone', 'Birthday', width=width, width_email=width_email)
    line = '=' * len(title)
    header = line + '\n' + title + '\n' + line + '\n'
    end = '{:=^{width}}'.format('END', width=len(title))
    table = header + string_files + end
    return table

def sort_name(data):
    name_list = []
    if data:
        for record in data:
            for key in record:
                name_list.append(key)
        
        sort_name_list = sorted(name_list)
        sort_list = sorted(data, key=lambda d: [k in d for k in sort_name_list], reverse=True)
        return sort_list
    else:
        return 'Database is empty!'

def sort_surname(data):
    dict_ = []
    sort_dict = []
    if data:
        for record in data:
            for value in record.values():
                dict_.append(value)
        dict_ = sorted(dict_, key=lambda k: k['surname'])

        for item in dict_:
            for record in data:
                for value in record.values():
                    if item == value:
                        sort_dict.append(record)
        
        return sort_dict
    else:
        return 'Database is empty!'

def sort_len_note(data):
    dict_ = []
    sort_dict = []
    if data:
        for record in data:
            for value in record.values():
                dict_.append(value)
        dict_ = sorted(dict_, key=lambda k: len(k['note']), reverse=True)

        for item in dict_:
            for record in data:
                for value in record.values():
                    if item == value:
                        sort_dict.append(record)
            
        return sort_dict
    else:
        return 'Database is empty!'

def sort_birthday(data):
    dict_ = []
    sort_dict = []
    if data:
        for record in data:
            for value in record.values():
                dict_.append(value)
        dict_ = sorted(dict_, key=lambda k: datetime.strptime(k['birthday'], '%d %m %Y'), reverse=True)

        for item in dict_:
            for record in data:
                for value in record.values():
                    if item == value:
                        sort_dict.append(record)
            
        return sort_dict
    else:
        return 'Database is empty!'

def check_double(data, field, value):
    for record in data:
        for item in record.values():
            if str(value) in item[field]:
                return False
    return True

def print_comands():
    print('Available commands:')
    for idx, comand in enumerate(comands):
        print(idx + 1, '-', comand, sep='-')