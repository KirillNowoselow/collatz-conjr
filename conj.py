x = 0
nums = []


def input_f():
    n = int(input('Введите натуральное число:'))
    if n <= 0:
        print('Неверные данные')
        input_f()
    global x
    x = n


def x2(x):
    x = x / 2
    return collatz(x)


def x3_1(num):
    num = num * 3 + 1
    return collatz(num)


def collatz(n):
    global nums
    if n == 1:
        nums.append(int(n))
        print(nums)
        return n
    elif n % 2 == 0:
        nums.append(int(n))
        return x2(n)
    else:
        nums.append(int(n))
        return x3_1(n)


input_f()
collatz(x)
