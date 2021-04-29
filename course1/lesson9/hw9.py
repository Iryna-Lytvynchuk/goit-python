from datetime import datetime


contact_save = {}

def log(action):

    current_time = datetime.strftime(datetime.now(), '%H:%M:%S')
    message = f'[{current_time}] {action}'
    print(message)

    with open('logs.txt', 'a') as file:
        file.write(f'{message}\n')

def save_contact(name, phone):

    log('Saving contact...')

    contact_save[name] = phone
    with open('save.txt','a') as i:
        for name,phone in contact_save.items():
            i.write('{}:{}\n'.format(name,phone))

    log('Contact has been saved')

def load_contact():

    log('Loading contact...')

    with open('save.txt') as file:
        for i in file.readlines():
            name,phone = i.strip().split(':')
            contact_save[name] = phone

    log('Contact has been loaded')
    
    return contact_save

def input_error(func):

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print(f"{func.__name__} got KeyError")
        except ValueError:
            print(f"{func.__name__} got KeyError")
        except IndexError:
            print(f"{func.__name__} got IndexError")
        except KeyboardInterrupt:
            print(f"{func.__name__} got KeyboardInterrupt")
        except TypeError:
            print(f"{func.__name__} got TypeError")
        except Exception as log:
            print(f"{func.__name__} got {log}")
    return inner

@input_error
def add(action):
    log("Give me name and phone please")
    name, phone = input('...').split()
    save_contact(name, phone)
    
@input_error
def hello(action):
    return 'How can I help you?'

@input_error
def change(action):
    log("Give me name and phone please")
    contact_save = load_contact()
    name, phone = input('...').split()
    for key, value in contact_save.items():
        if key == name:
            value = phone
            save_contact(name, phone)    

@input_error
def phone(action):
    log("Give me name please")
    contact_save = load_contact()
    name = input('...')
    for key, value in contact_save.items():
        if key == name:
            return value
        else:
            return "There is no such cotact, choose another"
@input_error
def show_all(action):
    contact_save = load_contact()
    for key, value in contact_save.items():
        print(key, value)

@input_error
def bye(action):
    return 'Good bye!'

def main():

    while True:
        action = input('Choose action: ')

        if action not in ('hello', 'add', 'change', 'phone', 'show all', 'good bye', 'close', 'exit'):
            log('Wrong action. Try again!')
            continue

        if action == 'add':
            add(action)
            continue
        elif action == 'hello':
            print(hello(action))
            continue
        elif action == 'change':
            change(action)
            continue
        elif action == 'phone':
            print(phone(action))
            continue
        elif action == 'show all':
            show_all(action)
            continue
        elif action == 'good bye' or action == 'close' or action == 'exit':
            print(bye(action))
            break


if __name__ == "__main__":
    main() 