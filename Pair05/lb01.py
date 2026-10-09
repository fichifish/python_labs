def circle():
    r = float(input())
    return 2*3.14159*r

def rectangle():
    a = float(input())
    b = float(input())
    return a*b

def triangle():
    a = float(input())
    h = float (input())
    return a*h/2

shape = input("Фігура: ")
if shape == "круг": print(circle())
elif shape == "прямокутник": print(rectangle())
elif shape == "трикутник": print(triangle())