import math 
C = float(input('Введите температуру в градусах Цельсия:'))
def temp(C):
    return C * 1.8 + 32
a = temp(C)    
print('Значение в градусах по Фаренгейту:', a)

def main() :
    C = float(input())
    a = temp(C)  
if __name__ == '__main__' :
    main()

