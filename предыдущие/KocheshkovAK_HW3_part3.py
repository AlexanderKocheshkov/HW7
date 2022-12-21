from math import sqrt
print("Введите коэффициенты квадратного уравнения: ") #Будем считать, что коэффициент а не равен нули, иначе уравнение из квадратного превратится в линейное
a = float(input())
b = float(input())
c = float(input())
D = (b**2) - (4*a*c)
if D == 0:
    x = (-b) / (2*a)
    print("x = %.2f", x)
elif D > 0:
    x1 = (-b+sqrt(D)) / (2*a)
    x2 = (-b-sqrt(D)) / (2*a)
    print("x1 = %.2f" %x1, "\nx2 = %.2f" %x2)
else:
    print("D = %.2f" %D, ". Нет корней")
