# Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X.  Пользователь вводит это число с клавиатуры, список можно считать заданным. Введенное число не обязательно содержится в списке.

#     Примеры/Тесты:
#     Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
#     Output: 2
#     Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
#
from collections import abc


lst = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
x = 2

dist = abs(x - lst[0])
find = lst[0]
for idx, el in enumerate(lst):
    if abs(el - x) < dist:
        dist = abs(el - x)
        find = lst[idx]
print(dist)
print(find)
