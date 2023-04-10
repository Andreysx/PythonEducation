# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# while True:
#     try:
#         num = int(input('Введите трехзначное число: '))
#         if 99 < num and num < 1000:
#             print(f'Сумма цифр: {num // 100 + num // 10 % 10 + num % 10}')
#             break
#         else:
#             print('Это не трехзначное число. Попробуйте еще раз!)')
#     except:
#         print('Некорректный ввод. Попробуйте еще раз!')

# Задача 4
# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10
# while True:
#     try:
#         S = int(input('Введите количество журавликов: '))
#         if S % 6 == 0:
#             x = S // 6
#             print(f'Петя и Сережа сделали по {x}, а Катя - {x * 4} журавликов')
#             break
#         else:
#             print('Это количество нельзя распределить в соответствии с условиями задачи! Попробуйте еще раз!')
#     except:
#         print('Некорректный ввод. Попробуйте еще раз!')

# Задача 6
# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no
# while True:
#     bilet = input('Введите номер билета 000000: ')
#     if bilet.isdigit() and len(bilet) == 6:
#         if bilet[0] + bilet[1] + bilet[2] == bilet[3] + bilet[4] + bilet[5]:
#             print('Это счастливый билет!')
#         else:
#             print('Не повезло(')
#         break
#     else:
#         print('Некорректный номер билета. Попробуйте еще раз!')

# Задача 8
# Требуется определить, можно ли от шоколадки
# размером n × m долек отломить k долек, если разрешается
# сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no
# while True:
#     try:
#         n = int(input("Введите длину шоколадки: "))
#         m = int(input("Введите ширину шоколадки: "))
#         k = int(input("Введите количество кусочков: "))
#         if k < m * n:
#             if (k % m == 0 or k % n == 0):
#                 print(f'Можно ломать!')
#                 break
#         elif k == m * n:
#             print('Ломать не нужно! Забирайте целиком!')
#             break
#         else:
#             print('Столько кусочков нет!')
#             break
#     except:
#         print('Некорректный ввод. Попробуйте еще раз!')