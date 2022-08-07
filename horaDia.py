hora = input('Que horas são: ')
try:
    hora = int(hora)
    if hora <= 11:
        print('Bom dia')
    elif hora <= 17:
        print('Boa tarde')
    elif hora <= 23:
        print('Boa noite')
    else:
        print('Hora informada invalida')
except:
    print('Não entendi')
