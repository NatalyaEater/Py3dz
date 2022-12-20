# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import random

print('Введите кол-во позиций для списка')
num = int(input())
print()

numbers = list()
k = 0
while num > k:
    rat = random.randint(-10, 10)
    numbers.append(rat)
    k = k+1
print('Вид рандомного списка', numbers)

def sum(a):
    list = []
    i = 0
    j = (len(a)-1)
    for i in range(len(a)):
        if i != j:
            para = a[i]*a[j]
            list.append(para)
            i = i+1
            j = j-1
        else:
            para = a[i]*a[i]
            list.append(para)
            break
    print(list)

print('Произведение пар чисел списка:')
sum(numbers)
