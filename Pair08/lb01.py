
try: 
    a = float(input("A: "))
    b = float(input("B: "))
    c = input("Операція: ")
    if c=="+": print(a+b)
    elif c=="-": print(a-b)
    elif c=="*": print(a*b)
    elif c=="/": print(a/b)
    else: raise ValueError("Не та операція...")
except ZeroDivisionError:
    print("На нуль ділити не можна")
except ValueError as res:
    if "could not convert string to float" in str(res): print("Введи числа")
    else: print(res)