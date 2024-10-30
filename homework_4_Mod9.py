# Домашнее задание по теме "Создание функций на лету"
# Цель: освоить на практике замыкание, объекты-функторы и lambda-функции.
# Задача "Функциональное разнообразие":

first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, "w", encoding='UTF-8') as file:
            for element in data_set:
                file.write(str(element) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

import random

class MysticBall:
    def __init__(self, *words: str):
        self.words = words

    def __call__(self):
        return random.choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

