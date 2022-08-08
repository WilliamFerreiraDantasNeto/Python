# Variaveis

"""
Sem iniciar com letras, pode conter números, separar _, letras minúsculas
"""

nome = 'Joao Neto'
idade = 35
altura = 1.70
e_maior = idade > 18
peso = 106
imc = peso/altura**2
print(nome, type(nome))
print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior?:', e_maior)
print(idade * altura)
print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
