num = input('Digite um numero inteiro: ')

try:
    num = int(num)
    if num % 2 == 0:
        print(f'{num} é par')
    else:
        print(f'{num} é impar')
except:
    print('não digitou um numero inteiro')
    
