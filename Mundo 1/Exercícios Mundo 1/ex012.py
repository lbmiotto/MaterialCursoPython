# Exercício 012: Faça um algoritmo que leia o preço de um prodruto e mostre seu novo preço, com 5% de desconto.

valor = float(input('Informe o preço do produto: '))
desconto = (valor * 5) / 100
novo_valor = valor - desconto

print('O produto com 5% de desconto fica {}'.format(novo_valor))