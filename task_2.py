# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали
# одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Примеры/Тесты:
# 6 >>>  1  4  1
# 24 >>> 4  16  4
# 60 >>> 10  40  10

# число журавликов будет кратное 3-м, т.е. % 3 == 0
s = int(input("Введите количество журавликов кратное 3-м, которые сделали дети: "))
group_man = (s // 3)
made_man = group_man // 2                             # сделал один мальчик
# birds_k = (made_man * 2) * 2
birds_k = made_man * 4
print(f'Катя сделала {birds_k} жураликов, а Сережа и Петя по {made_man}')
