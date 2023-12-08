"""Рекурсия - вызов функции самой себя
Когда вы реализуете рекурсивную функцию, в ней необходимо указать какой момент следует прервать рекурию
Каждая рекурсивная функция состоит из базового случая(момент прерывания функции) и рекурсивного случая"""

def count_down(i):
    print(i)
    if i <= 0:  # Базовый случай
        return
    count_down(i-1)  # Рекурсивный случай


"""Рекурсивная функция проверки нахождения числа в списке списков"""

#box = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
box = [5]


def search_number(box, number):
    for item in box:  # Проходимся по списку списков
        if type(item) == list:  # Если элемент равен списку, то мы вызываем функцию ещё раз
            search_number(item, number)  # Вызываем функцию и проходимя по списку ещё раз
        if number == item: # Если элемент равен искомому значению, выводим True
            print("True")



"""Функция перебора циклом и нахождения числа в списке списков"""


def search_number2(box, number):
    for i in box:
        if type(i) == list:
            for j in i:
                if j == number:
                    print("True")
        if i == number:
            print("True")

