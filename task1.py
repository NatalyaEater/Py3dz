# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


import random
num = 10
print()

numbers = list()
k = 0
while num > k:
    rat = random.randint(-10, 10)
    numbers.append(rat)
    k = k+1

print ('Вид рандомного списка',numbers)

def sum(a):
    summa=0
    for i in range(1,len(a),2):
        summa=summa+a[i]
    print(summa)

print('Сумма элементов списка, стоящих на нечётных позициях равна :')
sum(numbers)
