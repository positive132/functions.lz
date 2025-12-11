import math 
def dlina():
    R = float(input('Введите радиус круга в сантиметра:'))
    return 3.14 * 2 * R 
a = dlina(R)    
print('Длина окружности в см:', a)
   
def pl(R):
    return 3.14 * R ** 2
b = pl(R)    
print('Площадь круга в см:' , b)

def main() :
    R = float(input())
    a = dlina(R)
    b = pl(R)    
if __name__ == '__main__' :
    main()



