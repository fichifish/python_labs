def minLength(password):
    if len(password) < 8: return False
    else: return True

def isUpper(password):
    for i in password:
        if i.isupper(): return True
    return False

def isLower(password):
    for i in password:
        if i.islower(): return True
    return False

def idDigit(password):
    for i in password:
        if i.isdigit(): return True
    return False

def isSpecial(password):
    for i in password:
        if i.isdigit() == False and i.isalpha() == False: return True
    return False

def validate_password(password):
    a = minLength(password)
    b = isUpper(password)
    c = isLower(password)
    d = idDigit(password)
    e = isSpecial(password)

    if a and b and c and d and e: print("Пароль відповідає вимогам.")
    else: 
        print("Пароль не відповідає вимогам.")
        print("Не виконано:")
        if not a: print("Занадто коротко")
        if not b: print("Немає великої літери")
        if not c: print("Немає маленької літери")
        if not d: print("Немає цифри")
        if not e: print("Немає спеціального символу")

password = str(input())
validate_password(password)