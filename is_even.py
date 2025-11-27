import math
print('Введите число, чтобы узнать его четность:')
C = int(input())
def chislo(C):
    if C % 2 == 0:
        print('Ваше число четное')
    elif C % 2 != 0:
        print('Ваше число нечетное')
print(chislo(C))        
