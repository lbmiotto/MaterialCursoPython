# Operadores Aritméticos

Em aulas anteriores, acabamos usando uma propriedade muito interessante, a adição, mas saiba que essa propriedade não é a única. Nessa aula vamos ver um pouco mais dos operadores aritméticos, quais são, como funcionam e como escrever códigos com eles.

**Operadores:**
Anteriormente utilizamos a propriedade de adição (+), porém essa não é a única propriedade aritmética no Python, a seguir veja alguns dos operadores que podem ser usados no Python:

- Adição (+)
- Subtração (-)
- Multiplicação (*)
- Divisão (/)
- Potência (**)
- Divisão Inteira (//)
- Resto da Divisão

Veja alguns exemplos de como utilizar cada um:

*OBS: Anteriormente vimos que o sinal de = é dado como "recebe", nesse caso, utilizaremos o sinal = duas vezes, para que assim ele possa ser lido como um sinal de atribuição*

- 5 + 2 == 7
- 5 - 2 == 3
- 5 * 2 == 10
- 5 / 2 == 2.5
- 5 ** 2 == 25
- 5 // 2 ==2
- 5 % 2 == 1

*Lembrete: Seguindo os exemplos acima, veja como é feito alguns cálculos
- Potência: Esse operador resulta o operando vezes o número do expoente, nesse caso, o 5 é o operando, e o 2 é o expoente, logo 5 ** 2 = 25
- Divisão Inteira: Esse operador resulta o ultimo número inteiro de uma divisão, nesse caso, o 2 é o ultimo número inteiro que podemos dividir por 2, logo 5 // 2 = 2
- Resto da Divisão: Esse operador resulta o resto de uma divisão inteira, nesse caso, o 1 é o resto de da divisão inteira de 5 % 2, sendo assim, 5 % 2 = 1*

**Ordem de Precedência** 

Acabamos de ganhar mais alguns operadores para trabalhar em nosso códigos, porém é muito importante saber a ordem de precedência desses operadores, ou seja, qual operador é deve ser calculado primeiro em uma expressão, para isso, veja a ordem a seguir:

- 1: ()
- 2: **
- 3: * | / | // | %
- 4: + | -

Tendo essa ordem em mente, saiba que quando temos uma expressão matemática em um programa, o calculo sempre vai começar pela expressão que está entre (), depois as potências **, e por assim em diante.

Para ficar mais fácil, segue o exemplo a seguir:

5+3*2 =11
*OBS: Nessa expressão existe os operadores de + e de *, seguindo a ordem de precedência, devemos fazer primeiro o 3*2, e o resultado fazer com + 5*

3*5+4**2= 31
*OBS: Nessa expressão existe os operadores de + , **  e de *, seguindo a ordem de precedência, devemos fazer primeiro a potência, depois multiplicação e depois a adição*

**Vamos Práticar!**

Vamos construir um programa que faça os todos os operadores que vimos nessa aula:

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