cotDolar=1.8
cotMarco=2.0
cotLibra=3.57
viajante=input('Digite o valor em reais: ')
viajante=viajante.replace(',','.')
reais = float(viajante)
print(f'Você tem R$:{reais:.2f}')
print(f'O equivalente a $: {reais/cotDolar:.2f} dolares')
print(f'O Equivalente a £: {reais/cotLibra:.2f} libras esterlinas')
print(f'O equivalente a ℳ : {reais/cotMarco:.2f} marco alemão')
