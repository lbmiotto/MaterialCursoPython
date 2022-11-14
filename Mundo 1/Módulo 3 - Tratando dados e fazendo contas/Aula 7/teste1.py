n1 = int(input('Insira um valor: '))
n2 = int(input('Insira outro valor: '))
    
soma = n1+n2
sub = n1-n2
mult = n1*n2
div = n1/n2
pot = n1**n2
divint = n1//n2
divres = n1%n2
    
print('A adição de {} e {} é: {}'.format(n1,n2,soma))
print('A subtração de {} e {} é: {}'.format(n1,n2,sub))
print('A multiplicação de {} e {} é: {}'.format(n1,n2,mult))
print('A divisão de {} e {} é: {}'.format(n1,n2,div))
print('A potência de {} e {} é: {}'.format(n1,n2,pot))
print('A divisão inteira de {} e {} é: {}'.format(n1,n2,divint))
print('A resto da divisão de {} e {} é: {}'.format(n1,n2,divres))