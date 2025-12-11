import math 
def temp(C):
    return C * 1.8 + 32   

def main() :
    C = float(input('Введите температуру в градусах Цельсия:'))
    a = temp(C)  
    print('Значение в градусах по Фаренгейту:', a)
if __name__ == '__main__' :
    
    main()


