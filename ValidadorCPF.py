CPF = input('Digite o seu CPF com pontos e traço: ')\
    .replace ('.', '')\
    .replace ('-','')\
    .replace (' ','')

CPF2 = CPF[:9]
cont = 10
soma = 0
if CPF2[1]*9 == CPF2:
    print('Numeros CPF sequenciais')
else:
    for x in CPF2:
        soma += int(x) * cont
        cont -= 1
    soma = 11 - (soma % 11)
    CPF2 += str(0) if soma > 9 else str(soma)

    cont = 11
    soma = 0
    for x in CPF2:
        soma += int(x) * cont
        cont -= 1
    soma = 11 - (soma % 11)
    CPF2 += str(0) if soma > 9 else str(soma)
    print('CPF Válido' if CPF2 == CPF else 'CPF Inválido')
