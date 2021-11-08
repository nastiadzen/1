import math
n=[]
m=int(input("Введіть розмір масиву"))
print("Введіть елементи масиву")
for c in range (m):
    n.append(int(input()))
print("Масив")
print(n)
t=max((i for i in n))
if t>0:
    print ("Мінімальний додатній елемент масиву", t)
else:
    print ("Додатні елементи відсутні")
print ("Середнє арифметичне додатніх чисел масиву")
import statistics
print(str(statistics.mean(n)))
print("Ненульові елементи масиву у зворотньому порядку")
for i in reversed(n):
    if i != 0:
        print(i, end = ', ')