"""
Iterando strings com while
"""
nome=input('Digite seu nome: ')
tamanho_nome=len(nome)
nome_separado='*'
indice=0
while indice < tamanho_nome:
    nome_separado += nome[indice]
    nome_separado +='*'
    indice += 1
print(nome_separado)