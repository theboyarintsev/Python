# Дана последовательность натуральных чисел, завершающаяся числом 0.
# Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.
# Используйте цикл while для считывания символов последовательности.

a = int(input())
len2 = len = 0
while a != 0:
    b=int(input())
    if a == b:
        len += 1
        if len > len2:
            len2 = len
    else:
        len = 0
    a = b
print(len2+1)