CPF = input('Digite o seu CPF com pontos e traço: ')
CPF2 = ''
CPFteste = ''
for x in CPF:
    if not x == '.' and not x == '-':
        CPFteste = CPFteste+x
cont = 10
soma = 0
for x in CPF:
    if x == '-':
        break
    elif not x == '.':
        CPF2 = CPF2+x
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
print('CPF Válido' if CPF2 == CPFteste else 'CPF Inválido')
