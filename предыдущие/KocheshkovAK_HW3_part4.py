from math import sqrt
from cmath import sqrt as csqrt
print("Введите коэффициенты квадратного уравнения: ") 
a = float(input())
b = float(input())
c = float(input())
D = (b**2) - (4*a*c)
if D == 0:
    x = (-b)/(2 * a)
    print("x = %.2f", x)
elif D > 0:
    x1 = (-b+sqrt(D)) / (2*a)
    x2 = (-b-sqrt(D)) / (2*a)
    print("x1 = %.2f" %x1, "\nx2 = %.2f" %x2)
else:
    x1 = (-b+csqrt(D)) / (2*a)
    x2 = (-b-csqrt(D)) / (2*a)
    print("x1 = {:.2f}".format(x1), "x2 = {:.2f}".format(x2))
