"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. EX.
Bom dia 0-11, Boa tarde 12-17 e boa noite 18-23
"""


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
