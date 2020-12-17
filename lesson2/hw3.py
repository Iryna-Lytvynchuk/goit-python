
while True:
    user_input_n1 = input("Еnter the number1: ")
    
    try:
        user_input_n1 = float(user_input_n1)
        break
    
    except ValueError:
        print(f"{user_input_n1} is not correct, try once more")
    
while True:
    user_input_operator = input("Enter operator (+,-,*,/): ")

    if user_input_operator in ('+', '-', '*', '/'):
        break
    else:
        print(f"{user_input_operator} is not correct, try once more")

while True:
    user_input_n2 = input("Еnter the number2: ")
    
    try:
        user_input_n2 = float(user_input_n2)
        break    
    
    except ValueError:
        print(f"{user_input_n2} is not correct, try once more")

result = float()
user_input_r = str(input('Еnter operator = :'))

if user_input_operator == '+':
    result = user_input_n1 + user_input_n2
    print (result)

elif user_input_operator == '-':
    result = user_input_n1 - user_input_n2
    print (result)

elif user_input_operator == '*':
    result = user_input_n1 * user_input_n2
    print (result)

elif user_input_operator == '/':
    result = user_input_n1 / user_input_n2
    print (result)

else:
    print('not correct')