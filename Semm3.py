# Задача №17 Задан список чисел
# Определите сколько в нем встречается различных чисел
# Input [1,1,2,,0,-1,3,4,4]
# Output 6
 
# import random
 
# num = int(input('Введите количество элементов в списке: '))
# list = list()
 
# for i in range(num):
# list.append(random.randint(-4,4))
# print('Дан список', list)
 
# list = set(list)
# print('В нем содержится',len(list),"уникальных элементов")
 
# Дана последовательность из N целых чисел и число K
# Необходимость сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K - 
# положительное число
# Input [1,2,3,4,5] k = 3
# Output [4,5,1,2,3]
 
# array_length = input("Введите количество чисел: ")
# k = input("Введите сдвиг: ")
 
# nums_array = [i for i in range(1,int(array_length) + 1)]
# print(nums_array)
 
# for i in range(int(k)):
# nums_array.insert(0,nums_array.pop())
# print(nums_array)
 
# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
 
# array = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {" VIII":" S007 "}]
# print(array)
 
# unique_dict = {}
 
# for i in range(len(array)):
# for j in array[i].values():
# unique_dict[j] = "None"
 
# print('{',*unique_dict.keys(),'}')



 
# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
 
import random
 
nums = input('Введите количетсво целых чисел: ')
 
array = [random.randint(-10,10) for _ in range(int(nums))]
counter = 0
result_string = ''
print(array)
 
for i in range(len(array) - 1):
    if (array[i] < array[i+1]):
        counter += 1
result_string += f'{array[i]} < {array[i + 1]}'
 
print(f'{counter} ({result_string})') 