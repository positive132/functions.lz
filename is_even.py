import math
def chislo(C):
    if C % 2 == 0:
        print('Ваше число четное.')
    elif C % 2 != 0:
        print('Ваше число нечетное.')
      
def main() :
    C = int(input('Введите число, чтобы узнать его четность:'))
    print(chislo(C))      
if __name__ == '__main__' :
    main()
