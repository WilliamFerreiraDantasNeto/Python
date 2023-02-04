"""
Exercício
peça ao usuário para digitar seu nome
sua idade
se nome e idade forem digitados:
exiba:
Seu nome é
seu nome invertido é
seu nome contém (ou não espaços)
A primeira letra do seu nome é
A última letra do seu nome é
Se nada for digitado em nome ou idade
exiba "Descule, voce deixou campos vazios."
"""
nome=input('Digite seu nome: ')
idade=input('Digite sua idade: ')
if nome or idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if (' ' in nome):
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
    
else:
    print('Desculpe, você deixou campos vazios.')