# Домашнее задание по теме "Введение в функциональное программирование"
# Цель: научиться обращаться к функциям, как к объекту и передавать их в другие функции для вызова.
# Задача "Вызов разом":

def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))