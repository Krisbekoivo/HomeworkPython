a = int(input('Введите число '))
b = int(input('Введите степень '))

def rec(a,b):
    if b == 0:
        return 1
    return a * rec(a, b -1)

print(rec(a,b))