# Exercício 008: Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros.

valor = float(input('Insira um valor em metros: '))
cm = valor * 100
mm = valor * 1000

print('O valor {} em metros corresponde a {}cm e {}mm'.format(valor, cm, mm))