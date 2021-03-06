# Помогите жителям Трешландии понять, сколько питомцев они могут завести. 
# Напишите рекурсивную реализацию функции, определяющей по номеру значение n-ого числа Фибоначчи.
# Формат ввода
# На вход подается n - целое число в диапазоне от 0 до 30.
# Формат вывода
# Нужно вывести n-ое число Фибоначчи.
# Пример 1
# Ввод	
# 3
# Вывод
# 3
# Пример 2
# Ввод	
# 0
# Вывод
# 1

with open("input.txt") as f:
    n = int(f.readline())

def fibonacci(n):
    if n in (0, 1):
        return 1
    else:
        x = fibonacci(n -1) + fibonacci(n - 2)
        return x

print(fibonacci(n))