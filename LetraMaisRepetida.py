frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido Van Rossum.'

i = 0
letra_mais_repetida = ''
qtd_vezes = 0
while i <len(frase):
    letra_atual = frase[i]
    if letra_atual == ' ' or letra_atual == '.':
        i += 1
        continue
    if frase.count(letra_atual) > qtd_vezes:
        letra_mais_repetida=letra_atual
        qtd_vezes = frase.count(letra_atual)
    i += 1
print(f'A letra "{letra_mais_repetida}" foi a primeira letra mais a repetida, aparecendo {qtd_vezes} vezes')

