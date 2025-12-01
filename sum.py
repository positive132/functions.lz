import math 
S = (input('Введите ваш список для нахождения их суммы:')).split()
def summa(S):
    return sum([float(x) for x in S])
a = summa(S)  

print('Вот ваша сумма всех чисел с предоставленного списка', a)

def main() :
    S = (input()).split()
    a = summa(S)  
if __name__ == '__main__' :
    main()

