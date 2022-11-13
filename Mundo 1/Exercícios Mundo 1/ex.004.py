# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações sobre ele

valor = input('Informe algo: ')
print('O tipo primitivo é: ', type(valor))
print('O valor está em caixa baixa: ', valor.islower())
print('O valor está em caixa alta: ', valor.isupper())
print('O valor é alfanumérico: ', valor.isalnum())
print('O valor é alfabético: ', valor.isalpha())
print('O valor é númerico: ', valor.isnumeric())
