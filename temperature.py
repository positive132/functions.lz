import math 
print ('Введите температуру в градусах Цельсия:')
C = float(input())
def temp(C):
    return C * 1.8 + 32
a = temp(C)    
print('Значение в градусах по Фаренгейту:', a)

def main() :
    a = temp(C)  
if __name__ == '__main__' :
    main()
