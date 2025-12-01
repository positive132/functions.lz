import math
C = int(input('Введите число, чтобы узнать его четность:'))
def chislo(C):
    if C % 2 == 0:
        print('Ваше число четное.')
    elif C % 2 != 0:
        print('Ваше число нечетное.')
print(chislo(C))        
