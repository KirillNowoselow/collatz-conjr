
def input_f():
    while True:
        x = int(input('Введите натуральное число:'))
        if x > 0:
            return collatz(x)


def x2(num):
    return collatz(num // 2)


def x3_1(a):
    return collatz(a*3+1)


def collatz(x):
    nums = [x]
    if x == 1:
        pass
    elif x % 2 == 0:
        nums.extend(x2(x))
    else:
        nums.append(x3_1(x))
    return nums


print(collatz(x))
