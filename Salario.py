op=input('Menu de opções:\n1. Imposto\n2. Novo salário\n3. Classificação\nDigite a opção desejada. ')
if op=='1' or op=='2' or op=='3':
    salario=input('Digite o salario do funcionario para o calculo do imposto\nR$:')
    try:
        salario_float=float(salario)
        if op=='1':
            if salario_float < 500.00:
                print(f'Imposto de {salario_float*0.05:.2f}')
            elif salario_float < 850.00:
                print(f'Imposto de {salario_float*0.1:.2f}')
            else:
                print(f'Imposto de {salario_float*0.15:.2f}')
        elif op=='2':
            if salario_float > 1500.00:
                print(f'aumento de R$ 25,00, novo valor do salario R${salario_float+25:.2f}')
            elif salario_float >= 750.00:
                print(f'aumento de R$ 50,00, novo valor do salario R${salario_float+50:.2f}')
            elif salario_float >= 450.00:
                print(f'aumento de R$ 75,00, novo valor do salario R${salario_float+75:.2f}')
            else:
                print(f'aumento de R$ 100,00, novo valor do salario R${salario_float+100:.2f}')
        elif op=='3':
            if salario_float <= 750.00:
                print('Mal remunerado')
            else:
                print('Bem remunerado')
    except:
        print ('Salario invalido')
else:
    print('Opção invalida')
