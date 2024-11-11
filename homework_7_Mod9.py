# Домашнее задание по теме "Декораторы"
# Задание: Декораторы в Python
# Цель: освоить механизмы создания декораторов Python.
# Практически применить знания, создав функцию декоратор и обернув ею другую функцию.

def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        sum_num = sum(args)
        k = 0
        for i in range(2, sum_num // 2 + 1):
            if sum_num % i == 0:
                k = k + 1
        if k <= 0:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
