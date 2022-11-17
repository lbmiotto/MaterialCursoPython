# Exercício 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import pow, sqrt
co = float(input('Informe o Cateto Oposto: '))
ca = float(input('Informe o Cateto Adjacente: '))
hip = pow(co,2) + pow(ca,2)

print('A hipotenusa vai medir: {:.2f}'.format(sqrt(hip)))