# Lab_03_2.py
# Товтин ОЛександра
# Лабораторна робота №3.2
# Розгалуження, задане формулою: функція з параметрами
# Варіант  21

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
x = int(input("x = "))
def method1(a, b, c, x):
    if x < 0 and b != 0:
        F = a * x**2 + b
    if x > 0 and b == 0:
        F = (x - a) / (x - c)
    else: 
        F = x / c
    return F
result1 = method1(a, b, c, x)
print("1) F = ", result1)

def method2(a, b, c, x):
    if x < 0 and b != 0:
        F = a * x**2 + b
    elif x > 0 and b == 0:
        F = (x - a) / (x - c)
    else: F = x / c
    return F
result2 = method2(a, b, c, x)
print("2) F = ", result2)