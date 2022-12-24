# Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06


n = int (input('Введите число: ')) 
def get_squerence(n):
    return [round((1+1/x)**x, 5) for x in range (1, n+1)]
nums = get_squerence(n)
print(nums)
print(round(sum(nums), 5))
