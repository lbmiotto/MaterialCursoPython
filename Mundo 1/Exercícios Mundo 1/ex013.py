# Exercício 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = float(input('Informe o salário do funcionário: '))
novo_sal = sal + ((sal*15)/100)

print('O salário com 15$ de aumento fica: {}'.format(novo_sal))