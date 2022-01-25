x = int(input('Введите x: '))
def x2(x):
    x = x / 2
    return collatz(x)

def x3_1(x):
    x = x*3+1
    return collatz(x)
