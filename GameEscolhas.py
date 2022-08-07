print('Bem vindo ao meu primeiro jogo em python!')
name = input('Qual o seu nome? ').capitalize()
age = int(input('Qual a sua idade? '))

pv = 10

if age >= 18:
    print('Você tem idade suficiente para jogar')
    wants_to_play = input('Você quer jogar? ').lower()
    if wants_to_play == 'sim':
        print('Vamos jogar')
        print(f'você começa com {pv} de vida')
        left_or_righht = input('Primeira escolha... Esquerda ou direita (Esquerda/Direita)? ').lower()
        if left_or_righht == 'esquerda':
            ans = input('Bem, você segue o caminho e chega a um lago... voce atravessa nadando ou da a volta (nada/contorna)?').lower()
            if ans == 'contorna':
                print('Você contorna e alcança o outro lado do lago')
            elif ans == 'nada':
                print('Voce consegue nadar atravez do lago, mas é mordido por peixes e perde 5 de vida')
                pv -= 5
            ans = input('você nota uma casa e um rio. Você vai para qual (rio/casa)? ').lower()
            if ans == 'casa':
                print('Você vai para a casa e é atacado pelo proprietario, você perde 5 de vida')
                pv -= 5
                if pv <= 0:
                    print('Você tem 0 pv e perdeu...')
                else:
                    print('Você sobreviveu... você ganhou')
            else:
                print("Você não consegue atravessar o rio e perde...")
        else:
            print('Você se perdeu na floresta, caiu em um buraco e perdeu')
    else:
        print('Então tchal')
else:
    print('Você não tem idade suficiente para jogar')
