import math 
def summa(S):
    S = (input('Введите ваш список для нахождения их суммы:')).split()
    return sum([float(x) for x in S])

def main() :
    S = (input()).split()
    a = summa(S)  
    print('Вот ваша сумма всех чисел с предоставленного списка', a)
if __name__ == '__main__' :
    main()

