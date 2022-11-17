# Exercício 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
valor = float(input('Informe o valor do ângulo: '))
sen = math.sin(math.radians(valor))
cos = math.cos(math.radians(valor))
tan = math.tan(math.radians(valor))

print('O ângulo de {} tem o SENO de {:.2f}'.format(valor, sen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(valor, cos))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(valor, tan))