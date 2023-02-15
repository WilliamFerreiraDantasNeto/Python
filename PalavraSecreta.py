"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a 
possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra 
digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta exiba*.
Faça a contagem de tentativas do seu usuário.
"""
import os

palavra_secreta = 'Perfume'
palavra_tentada = '*******'
palavra_formatada = ''
tentativas = 0
print('Tente descobrir a palavra secreta letra a letra')
while palavra_secreta != palavra_tentada:
    letra_tentada=input('Digite uma letra: ')
    if len(letra_tentada) > 1:
        print('Digite apenas uma letra')
        continue
    for l in range(len(palavra_secreta)):
        if letra_tentada == palavra_secreta[l]:
            palavra_formatada += letra_tentada
        elif palavra_tentada[l] == palavra_secreta[l]:
            palavra_formatada += palavra_tentada[l]
        else:
            palavra_formatada += '*'
    print(f'Palavra formatada: {palavra_formatada}')
    palavra_tentada = palavra_formatada
    palavra_formatada = ''
    tentativas +=1
os.system('cls')
print(f'Parabéns você descobriu a palavra secreta "Perfume" em {tentativas} tentativas')
