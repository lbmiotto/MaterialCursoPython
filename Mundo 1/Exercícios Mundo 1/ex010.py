# Exercício 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere que 1 dolor vale 3,27 reais

valor = float(input('Informe o seu valor em reais: '))
compra = valor/3,27
print('Com {} Reais, você pode comprar {} Dólares!'.format(valor,compra))