# Exercício 014: Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

tempc = float(input('Insira a temperatura em Celsius: '))
tempf = (tempc * 9/5) + 32

print('O valor {}ºC em Fahrenheit é {}ºF'.format(tempc, tempf))