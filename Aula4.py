# Aula 4 - Tipos de dados primitivos

"""
Tipos de dados
str- string - textos com 'aspas simples' ou "aspas duplas"
int - inteiro - ..., -2, -1, 0, 1, 2,...
float - real/ponto flutuante - ..., -2.0, -1.0 ,0, 0.1, 0.2, ...
bool -  booleano/lógico - True (10==10)/False (10==11) (verdadeiro ou falso)
"""
# saber o tipo de dado ex: str
print('Ryuya', type('Ryuya'))
print(1, type(1))
print(1.1, type(1.1))
print(True, type(True))
print('10==20', type(10 == 20), 10 == 20)
print(int(float('1.1')))
# nome texto
print('Ryuya', type('Ryuya'))
# idade int
print(35, type(35))
# altura float
print(1.70, type(1.70))
# boleano maior de idade
print(35 > 18, type(35 > 18))
