def average(grades):
    return sum(grades)/len(grades)

def minimum(grades):
    return min(grades)

def maximum(grades):
    return max(grades)

def count_above(grades, value):
    res = 0
    for i in grades:
        if i > value: res += 1
    return res 

def main():
    grades = list(map(int, input().split()))
    minn = int(input())
    print("Середній бал: " + str(average(grades)))
    print("Мінімальна: " + str(minimum(grades)))
    print("Максимальна: " + str(maximum(grades)))
    print("Вище " + str(minn) + ": " + str(count_above(grades, minn)))

main()