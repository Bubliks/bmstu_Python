#Программа вычисления Объема и Площади шарового сегмента (Кузнецов ИУ7-13)
from math import *
#Здесь вводится радиус
R = float(input("Введите радиус: "))
#Здесь вводится высота
H = float(input("Введите высоту: "))
#Проверка: является ли число положительным и > 0
if R>0 and H  > 0:
  #Высчитывается объем сегмента
  V = pi*H**2*(R-1/3*H)
  #Высчитывается площадь сегмента
  S = 2*pi*R*H
#В случае если не удоволетворяет условию, то выводит "Такого не существует"
else: print("Такого не существует")
#Здесь выводятся объем и площадь с 4 знаками после запятой
print("Объем равен = ",round(V,4))
print("Площадь равна = ",round(S,4))


