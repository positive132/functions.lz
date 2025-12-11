import math 
def dlina(R):
    return 3.14 * 2 * R 

def pl(R):
    return 3.14 * R ** 2

def main() :
    R = float(input('Введите радиус круга в сантиметра:'))
    a = dlina(R)
    b = pl(R)    
    print('Длина окружности в см:', a)
    print('Площадь круга в см:' , b)
if __name__ == '__main__' :
    main()
