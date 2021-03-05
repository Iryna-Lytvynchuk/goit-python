from datetime import datetime, timedelta

monday = []
tuesday = []
wednesday = []
thursday = []
friday = []

def congratulate(users):

    for i in users:
        
        name = str(i.get('name'))
        date = i.get('birthday')
        a = date.split("/")
        date_new = datetime(int(a[0]), int(a[1]), int(a[2]))
        i.update({'birthday':date_new})
        current_data = datetime.now()
        date_new_d = date_new.replace(current_data.year)
        count_date = date_new_d - current_data

        if current_data.weekday() == 6:
            if timedelta(-2) < count_date < timedelta(1):
                d = current_data + count_date
                monday.append(name)
            elif timedelta(1) < count_date < timedelta(2):
                d = current_data + count_date
                tuesday.append(name)
            elif timedelta(2) < count_date < timedelta(3):
                d = current_data + count_date
                wednesday.append(name)
            elif timedelta(3) < count_date < timedelta(4):
                d = current_data + count_date
                thursday.append(name)
            elif timedelta(4) < count_date < timedelta(5):
                d = current_data + count_date
                friday.append(name)
        
        if current_data.weekday() == 0:
            if timedelta(4) < count_date < timedelta(7):
                d = current_data + count_date
                monday.append(name)
            elif timedelta(7) < count_date < timedelta(8):
                d = current_data + count_date
                tuesday.append(name)
            elif timedelta(8) < count_date < timedelta(9):
                d = current_data + count_date
                wednesday.append(name)
            elif timedelta(9) < count_date < timedelta(10):
                d = current_data + count_date
                thursday.append(name)
            elif timedelta(10) < count_date < timedelta(11):
                d = current_data + count_date
                friday.append(name)


        if current_data.weekday() == 1:
            if timedelta(3) < count_date < timedelta(6):
                d = current_data + count_date
                monday.append(name)
            elif timedelta(6) < count_date < timedelta(7):
                d = current_data + count_date
                tuesday.append(name)
            elif timedelta(7) < count_date < timedelta(8):
                d = current_data + count_date
                wednesday.append(name)
            elif timedelta(8) < count_date < timedelta(9):
                d = current_data + count_date
                thursday.append(name)
            elif timedelta(9) < count_date < timedelta(10):
                d = current_data + count_date
                friday.append(name)        

        if current_data.weekday() == 2:
            if timedelta(2) < count_date < timedelta(5):
                d = current_data + count_date
                monday.append(name)
            elif timedelta(5) < count_date < timedelta(6):
                d = current_data + count_date
                tuesday.append(name)
            elif timedelta(6) < count_date < timedelta(7):
                d = current_data + count_date
                wednesday.append(name)
            elif timedelta(7) < count_date < timedelta(8):
                d = current_data + count_date
                thursday.append(name)
            elif timedelta(8) < count_date < timedelta(9):
                d = current_data + count_date
                friday.append(name)

        if current_data.weekday() == 3:
            if timedelta(1) < count_date < timedelta(4):
                d = current_data + count_date
                monday.append(name)
            elif timedelta(4) < count_date < timedelta(5):
                d = current_data + count_date
                tuesday.append(name)
            elif timedelta(5) < count_date < timedelta(6):
                d = current_data + count_date
                wednesday.append(name)
            elif timedelta(6) < count_date < timedelta(7):
                d = current_data + count_date
                thursday.append(name)
            elif timedelta(7) < count_date < timedelta(8):
                d = current_data + count_date
                friday.append(name)

        if current_data.weekday() == 4:
            if timedelta(0) < count_date < timedelta(3):
                d = current_data + count_date
                monday.append(name)
            elif timedelta(3) < count_date < timedelta(4):
                d = current_data + count_date
                tuesday.append(name)
            elif timedelta(4) < count_date < timedelta(5):
                d = current_data + count_date
                wednesday.append(name)
            elif timedelta(5) < count_date < timedelta(6):
                d = current_data + count_date
                thursday.append(name)
            elif timedelta(6) < count_date < timedelta(7):
                d = current_data + count_date
                friday.append(name)

        if current_data.weekday() == 5:
            if timedelta(-1) < count_date < timedelta(2):
                d = current_data + count_date
                monday.append(name)
            elif timedelta(2) < count_date < timedelta(3):
                d = current_data + count_date
                tuesday.append(name)
            elif timedelta(3) < count_date < timedelta(4):
                d = current_data + count_date
                wednesday.append(name)
            elif timedelta(4) < count_date < timedelta(5):
                d = current_data + count_date
                thursday.append(name)
            elif timedelta(5) < count_date < timedelta(6):
                d = current_data + count_date
                friday.append(name)    

    monday_str = ', '.join(monday)
    tuesday_str = ', '.join(tuesday)
    wednesday_str = ', '.join(wednesday)
    thursday_str = ', '.join(thursday)
    friday_str = ', '.join(friday)
    if not monday_str == '':
        print(f'Monday: {monday_str}')
    if not tuesday_str == '':
        print(f'Tuesday: {tuesday_str}')
    if not wednesday_str == '':   
        print(f'Wednesday: {wednesday_str}')
    if not thursday_str == '': 
        print(f'Thursday: {thursday_str}')
    if not friday_str == '': 
        print(f'Friday: {friday_str}')


bd_1 = {'name': 'SatAnn', 'birthday': '1991/02/27'}
bd_2 = {'name': 'SunKate', 'birthday': '1991/02/28'}
bd_3 = {'name': 'MonVlad', 'birthday': '1991/03/01'}
bd_4 = {'name': 'TueFed', 'birthday': '1991/03/02'}
bd_5 = {'name': 'WenSa', 'birthday': '1991/03/03'}
bd_6 = {'name': 'THIr', 'birthday': '1991/03/04'}
bd_7 = {'name': 'Frya', 'birthday': '1991/03/05'}
bd_8 = {'name': 'ghg', 'birthday': '1991/02/26'}
bd_9 = {'name': 'yu', 'birthday': '1991/03/07'}

users = [bd_1, bd_2, bd_3, bd_4, bd_5, bd_6, bd_7, bd_8, bd_9]

congratulate(users)