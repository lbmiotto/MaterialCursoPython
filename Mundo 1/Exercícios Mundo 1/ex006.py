# Exercício 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

valor = int(input('Informe um número inteiro: '))
dobro = valor * 2
triplo = valor * 3
raiz = valor**(1/2)

print('O dobro de {} é : {}'.format(valor, dobro))
print('O triplo de {} é : {}'.format(valor, triplo))
print('A raiz de {} é : {}'.format(valor, raiz))