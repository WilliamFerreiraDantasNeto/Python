# Faça um programa que receba a quantidade de dinheiro em reais que uma pessoa que vai viajar possui. 
# Ela vai passar por vários países e precisa converter seu dinheiro em dólares, marco alemão e libra esterlina. 
# sabe-se que a cotação do dólar é de R$ 1,80; do marco alemão, de R$ 2,00; e da libra esterlina, de R$ 3,57. 
# O programa deve fazer as conversões e mostrá-las


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
