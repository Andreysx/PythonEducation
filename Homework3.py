# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.
 
# Ввод: 5
# Ввод: 1
 
# 1 2 1 2 2
# Вывод: 2
 

# import random

# n = int(input('Введите количество элементов: '))


# list_1 = [random.randint(1,n//2) for i in range(n)]
# print(list_1)
# x = int(input('Введите число которое необходимо проверить: '))
# count = 0
# for i in list_1:
#     if i == x:
#         count += 1
# print(count) 



 
# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.
 
# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6

# import random
 
# n = int(input('Введите количество элементов: '))
# list_1 = [random.randint(1,n) for i in range(n)]
# dict_1 = dict() 
# print(list_1)
 
# x = int(input('Введите число которое необходимо проверить: '))
# count = None
# for i in list_1:
#     dict_1[i] = i - x
# print(dict_1)

# temp_value = list(dict_1.values())[0]

# list_2 = list()

# for key,value in dict_1.items(): 
#     if abs(value) <= abs(temp_value) and key <= 0:
#         list_2.append(key)
#     elif abs(value) <= abs(temp_value) and key >= 0:
#         list_2.append(key)
#     else:
#         pass 
# print(min(list_2))    
        

    

# Задача 20:
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
 
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, либо только русские буквы.
 
# Ввод: ноутбук
# Вывод: 12

# words_dict = {
#     1:["A", "E", "I", "O", "U", "L", "N", "S", "T", "R","А","В","Е","И","Н","О", "Р","С", "Т" ],
#     2: ["D", "G","Д", "К", "Л", "М", "П", "У"], 3:["B", "C", "M", "P","Б", "Г", "Ё", "Ь", "Я"],
#     4:["F", "H", "V", "W", "Y","Й", "Ы"], 5:["K","Ж", "З", "Х", "Ц", "Ч"], 8:["J", "X","Ш", "Э", "Ю"],
#     10:["Q", "Z","Ф", "Щ", "Ъ"]
# }

# a = input("Введите слово: ")

# count = 0
# for i in a:
#     for key,value in words_dict.items():
#         if i.upper() in value:
#             count += key
# print(count)
    