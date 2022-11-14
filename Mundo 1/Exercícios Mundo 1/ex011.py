# Exercício 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2²m.

largura = float(input('Informe a largura em metros: '))
altura = float(input("Informe a altura em metros: "))
area = largura * altura
tinta = area/2

print('A sua parete tem {}m²'.format(area))
print('Você precisa de {} litros de tinta para pintar a casa'.format(tinta))