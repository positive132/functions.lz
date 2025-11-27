import math 
print ('Введите радиус круга в сантиметра:')
R = float(input())
def dlina(R):
    return 3.14 * 2 * R 
a = dlina(R)    
print('Длина окружности в см:', a)
   
def pl(R):
    return 3.14 * R ** 2
b = pl(R)    
print('Площадь круга в см:' , b)

