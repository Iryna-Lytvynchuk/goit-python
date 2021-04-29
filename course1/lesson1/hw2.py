a = int(input("Коеф.а: "))
b = int(input("Коеф.b: "))
c = int(input("Коеф.c: "))
d = int(b**2 - 4*a*c)
x1 = float((-b + d**0.5)/(2*a))
x2 = float((-b - d**0.5)/(2*a))
x = f"x1 = {x1}; x2 = {x2}"
print(x)
