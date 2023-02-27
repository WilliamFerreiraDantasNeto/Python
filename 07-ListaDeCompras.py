"""
Faça uma lista de compras com listas
o usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista
"""
import os
lista = []
teste = True
while teste:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar [f]inalizar: ')
    if opcao == 'i':
        os.system('cls')
        item = input('Item: ')
        lista.append(item)
    elif opcao == 'a':
        os.system('cls')
        indice_str = input('Escolha o índice para apagar: ')
        try:
            indice = int(indice_str)
            del lista[indice-1]
        except IndexError:
            print('Não foi possível apagar este índice')
        except ValueError:
            print('Digite um numero inteiro para o índice')
        except Exception:
            print('Isso não deveria ter acontecido (Erro desconhecido)')
    elif opcao == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Nada para listar')
        else:
            for i, j in enumerate(lista):
                print(i+1, j)
    elif opcao =='f':
        os.system('cls')
        teste = False
        print('Até a próxima compra')
    else:
        print('Opção invalida selecione a opção i, a, l ou f')
