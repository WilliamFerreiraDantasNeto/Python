"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande.
"""

nome = input('Digite seu nome: ')
qtd_car = len(nome)

if qtd_car > 1:
    if qtd_car <= 4:
        print('Seu nome é curto')
    elif qtd_car <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite um número com mais de 1 caractere')
