nome = input('Digite seu nome: ')
qtd_car = len(nome)

if qtd_car <= 4:
    print('Seu nome é curto')
elif qtd_car <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
