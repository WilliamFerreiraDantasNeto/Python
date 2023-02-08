# Calculadora com while
condicao=True
while condicao:
    num_1 = input('Digite o primeiro número: ')
    num_2 = input('Digite o segundo número: ')
    op = input('digite o operador (+, -, *, /): ')
    numero_1_valido = None
    numero_2_valido = None
    num_1_float = 0
    num_2_float = 0
    try:
        num_1_float = float(num_1)
        numero_1_valido = True
    except:
        numero_1_valido = None
    if numero_1_valido is None:
        print('Primeiro número invalido')
        continue
    try:
        num_2_float = float(num_2)
        numero_2_valido = True
    except:
        numero_2_valido = None
    if numero_2_valido is None:
        print('Segundo número invalido')
        continue
    op_permitidos='+-/*'
    

    if op not in op_permitidos or len(op) > 1:
        print('Operador inválido.')
        continue
    
    if op=='+':
        print(num_1_float+num_2_float)
    if op=='-':
        print(num_1_float-num_2_float)
    if op=='*':
        print(num_1_float*num_2_float)
    if op=='/' and num_2_float != 0:
        print(num_1_float/num_2_float)
    else:
        print('Não é possivel dividir por 0')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair:
        condicao=False