"""Бинарный поиск - алгоритм: на входе  получает отсортированный список и искомое число.
В бинарном поиске берется число в середине диапазона и исключается половина
оставшихся чисел, пока не найдёте искомое.

Время выполнения алгоритма бинарного поиска определяется логарифмическим временем O(log n)"""


def binary_search(list_for_search, item):
    low = 0  # Индекс первого элемента
    high = len(list_for_search) - 1  # индекс последнего элемента

    while low <= high:  # Цикл повторяется, пока индекс меньшего элемента, меньше или сравняется с индексом большего
        mid = round((low + high) / 2)  # Индекс эелемента в середине списка
        quees = list_for_search[mid]  # Число из середина списка для сравнения с искомым числом

        if quees == item:  # Если число середины равно искомому числу, вернуть это число
            return mid
        if quees > item:  # Если число середины больше искомого, то индекс последнего элемента становится меньше
            high = mid - 1
        if quees < item:  # Если число середины меньше искомого, то индекс начального элемента становится больше
            low = mid + 1

    return None  # Возвращение None при отсутствии искомого числа в списке





