from random import randint
novo_cpf = ''
for index in range(9):
    novo_cpf += str(randint(0, 9))
reverso = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9
    total += int(novo_cpf[index]) * reverso
    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)
        if d > 9:
            d = 0
        total = 0
        novo_cpf += str(d)

print(novo_cpf)
