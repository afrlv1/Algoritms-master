# Алла ошиблась со структурой данных. Она решила хранить массив в кольцевом буфере. 
# Проблема в том, что массив был отсортирован. 
# И в нем можно было искать элемент за логарифмическое время. 
# Алла скопировала данные из кольцевого буфера а обычный массив. 
# Но он больше не является отсортированным. Тем не менее нужно обеспечить возможность находить 
# в нем элемент за O(logn).

# Формат ввода
# В первой строке записано число n - длина массива.
# Во второй строке записано положительное число k - искомый элемент. 
# n и k не превосходят 1000.
# Далее в строку через пробел записаны n положительных чисел, каждое из которых не превосходит 1000.

# Формат вывода
# Выведите индекс искомого элемента в массиве, если он найден. Иначе выведите -1.

# Пример 1
# Ввод	
# 8
# 3
# 1 2 3 5 6 7 9 0
# Вывод
# 2

with open("input.txt") as f:
    n = int(f.readline())
    x = int(f.readline())
    arr = list(map(int, (f.readline().split())))

for i in range(n):
    if arr[i] == x:
        pos = i
        break
    else:
        pos = -1
print(pos)
