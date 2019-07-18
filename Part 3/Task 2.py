# Напишите функцию, вычисляющую длину отрезка по координатам его концов.
# С помощью этой функции напишите программу, вычисляющую периметр треугольника по координатам трех его вершин.
# На вход программе подается 3 пары целых чисел — координат x₁, y₁, x₂, y₂, x₃, y₃ вершин треугольника.

from math import sqrt
print('x1, y1')
x1, y1 = map(float,input().split())
print('x2, y2')
x2, y2 = map(float,input().split())
print('x3, y3')
x3, y3 = map(float,input().split())
a = sqrt((x2-x1)**2+(y2-y1)**2)
b = sqrt((x3-x2)**2+(y3-y2)**2)
c = sqrt((x1-x3)**2+(y1-y3)**2)
p = (a+b+c)/2.0
print("%.04f"%(a+b+c))