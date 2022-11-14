# Exercício 005: Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

valor = int(input('Informe um número inteiro: '))
prox = valor + 1
ant = valor - 1

print('O valor {} tem como antecessor o {} e como sucessor o {}'.format(valor, ant, prox))