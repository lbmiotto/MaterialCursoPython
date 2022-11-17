# Exercício 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
num = float(input('Informe um número: '))
print('O número informado é {}, e sua porção inteira é {}'.format(num,(trunc(num))))