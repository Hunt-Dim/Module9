# Домашнее задание по теме "Генераторы"
# Цель: более глубоко понять особенности работы с функциями генераторами и оператором yield в Python.
# Задача:


def all_variants(text):
    n = len(text)
    for string_lengths in range(1, n + 1):
        for start_index in range(n - string_lengths + 1):
            yield text[start_index:start_index + string_lengths]


a = all_variants("abc")
for i in a:
    print(i)