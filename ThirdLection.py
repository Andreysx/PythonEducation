# print("Введите имя: ")
# a = input()
# print("Hello", a, "!")

#
# a = [1,2,3,4,5]
# x = lambda b: b % 2 == 0
# print(list(filter(x,a)))

a = [1,10,3,4,5,6]
b = []
for i, x in enumerate(a):
    if (i+1) % 3 == 0:
        b.append(a[i])
print(b)







