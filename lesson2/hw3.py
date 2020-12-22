
while True:
        user_input_n1 = input("Еnter the number: ")
    
        try:
            user_input_n1 = float(user_input_n1)
            break
    
        except ValueError:
            print(f"{user_input_n1} is not correct, try once more")

while True:
   
    while True:
        user_input_operator = input("Enter operator (+,-,*,/,=): ")

        if user_input_operator in ('+', '-', '*', '/', '='):
            break
        else:
            print(f"{user_input_operator} is not correct, try once more")
        
    if user_input_operator == '=':
        print (user_input_n1)
        break

    while True:
        user_input_n2 = input("Еnter the number: ")
    
        try:
            user_input_n2 = float(user_input_n2)
            break    
    
        except ValueError:
            print(f"{user_input_n2} is not correct, try once more")

    if user_input_operator == '+':
        user_input_n1 = user_input_n1 + user_input_n2
        

    elif user_input_operator == '-':
        user_input_n1 = user_input_n1 - user_input_n2
        
    
    elif user_input_operator == '*':
        user_input_n1 = user_input_n1 * user_input_n2
        

    elif user_input_operator == '/':
        user_input_n1 = user_input_n1 / user_input_n2
        

    else:
        print('not correct')
