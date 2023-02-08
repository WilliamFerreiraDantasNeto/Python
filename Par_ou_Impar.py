"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. 
Caso o usuário não digite um número inteiro,
informe que não é um número inteiro.
"""

num = input('Digite um numero inteiro: ')

try:
    num = int(num)
    if num % 2 == 0:
        print(f'{num} é par')
    else:
        print(f'{num} é impar')
except:
    print('não digitou um numero inteiro')
    
