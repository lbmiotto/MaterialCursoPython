# Tipos Primitivos e Saída de Dados

Sem nenhuma duvida, o Python sabe utilizar e manipular muito bem os dados que um programa possui, então nessa aula vamos aprofundar um pouco mais sobre os tão famosos 4 tipos primitivos do Python, lembrando que existem mais do que 4, porém nessa aula vamos falar dos mais básicos.

**Tipos Primitivos:**

Os tipos primitivos nada mais são do que a separação de dos 4 tipos de dados mais básicos que o Python consegue interpretar, ou seja, muitas informações e dados que trabalhamos dentro do nosso programa, são divididos em vários tipos, porém os 4 principais são os seguintes:

- int
- float
- bool
- str

Cada um desses tipos recebe um tipo de dado especifico, segue o exemplo a seguir onde mostra qual tipo de dado é separado em cada tipo primitivo:

- int -> Recebe valores numéricos inteiros (7, -4, 0, 75)
- float -> Recebe valores numéricos reais (4.5 , -5.7 , 0.05 , 7.0)
- bool -> Recebe valores lógicos binários (True , False)
- str -> Recebe valores de texto ('Olá' , 'Teste' , 'Oi' , '7.5' , '')

Agora que sabemos que o Python divide os tipos de dados, temos que considerar uma observação importante, pois nas aulas passadas, foi mencionado o comando "input" para pegar dados e colocar em variáveis, porém esse comando transforma tudo que ele pega em um dado do tipo str (string), com isso, para fazer a mudança de tipo de dado, segue-se o exemplo a seguir:

    dado1 = int(input('Informe um número'))
    dado2 = float(input('Informe outro número'))
    dado3 = str(input('Informe algo'))
    dado4 = bool(input('Informe True para sim e False para não'))

Veja que colocamos o tipo primitivo que queremos que o dado assuma antes de colocar o input dentro do código, sendo assim, dando o tipo que queremos colocar em nossos dados!
    
**Formatação: Saída de Dados**

Agora que sabemos como os os tipos dos dados funcionam, vamos falar sobre a formatação. Como foi visto anteriormente, nos utilizamos o comando print para colocar coisas na tela, porém em alguns casos, se torna muito chato ter que ficar alternando os valores dentro do print, como mostrado a seguir:

    n1 = 3
    print('O valor de é: ' , n1 )

Com isso, saiba que existe uma maneira de formatar essa saída de dados com o comando .format, onde a partir dos parâmetros {} dentro do comando print, você pode informar o variável que você deseja colocar, veja no exemplo a seguir:

    n1 = 3
    print('O valor de é: {}'.format(n1))

Veja que a variável que colocamos dentro do .format é adicionada no parâmetro {} dentro do comando do print!

**Vamos colocar em Prática!**

Os 2 programas a seguir vão informar qual é o tipo do dado que foi recebido:

    # Primeiro programa
    valor1 = input('Informe algo: ')
    print(type(valor1))
    
    <class 'str'>
    # Veja que com o input, não inporta o valor dado, ele sempre vai ser transformado em str

	# Segundo Programa
	valor2 = int(input('Informe algo: '))
    print(type(valor2))
    
    <class 'int'>
    # Veja que com o tipo primitivo especificado , ele altera o tipo do dado

O programa a seguir vai mostrar a soma de 2 valores com o comando .format

    n1 = int(input('Informe um número: '))
    n2 = int(input('Informe outro número: '))
    soma = n1+n2
    print('A soma entre {} e {} é {}'.format(n1,n2,soma))

Outra coisa que podemos fazer dentro de um programa é identificar que tipo de dado foi informado, sem ser os tipos primitivos no caso, veja o exemplo com os programas a seguir:

    # Esse programa informa se o valor informado é númerico ou não
    n = input('Informe algo: ')
    print(n.isnumeric())
    
    # Esse programa informa o valor é alfabético
    n = input('Informe algo: ')
    print(n.isalpha())
    
    # Esse programa informa o valor é alfanumérico
    n = input('Informe algo: ')
    print(n.isalnum())
    
    # Esse programa informa o valor possui apenas letras em caixa alta
    n = input('Informe algo: ')
    print(n.isupper())
    
    # Esse programa informa o valor possui apenas letras em caixa baixa
    n = input('Informe algo: ')
    print(n.islower())



# Desafios

**Desafio 1:**  Crie um programa que leia dois números e mostre a soma entre eles

**Desafio 2:**  Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações sobre ele
