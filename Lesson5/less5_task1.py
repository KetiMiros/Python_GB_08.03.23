"""
Напишите рекурсивную функцию для возведения числа a в степень b
Разрешается использовать только операцию умножения. Циклы использовать нельзя
Примеры/Тесты:
    <function_name>(2,0) -> 1
    <function_name>(2,1) -> 2
    <function_name>(2,3) -> 8
    <function_name>(2,4) -> 16
"""

a = 2
b = 4

def fun_self(a, b):
    if b == 0:
        return 1
    return fun_self(a, b - 1) * a

print(fun_self(a, b))
