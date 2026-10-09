def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0: return False
    return True

def divisors(n):
    idk = []
    for i in range(1, n+1):
        if n%i == 0: idk.append(i)
    return idk

def digit_sum(n):
    sum = 0
    for i in str(n): sum += int(i)
    return sum

def main():
    number = int(input())
    print("Просте число: ", end="")
    if is_prime(number): print("так")
    else: print("ні")
    print("Дільники: " + str(divisors(number)))
    print("Сума цифр: " + str(digit_sum(number)))

main()