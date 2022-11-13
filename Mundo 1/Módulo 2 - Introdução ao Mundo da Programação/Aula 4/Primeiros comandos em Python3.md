# Primeiros comandos em Python3

Agora com o Python e o IDLE instalados, nessa aula vamos dar os nossos primeiros passos no Python, e vamos executar os nossos primeiros comandos e começar a entender a lógica por trás da programação!

**Primeiros Passos:**

Vamos começar a nossa programação com um código bem simples, onde vamos colocar na tela a seguinte mensagem: "Olá, Mundo!"

De acordo com nossa proposta, temos que inserir um texto na tela, e no python, quando vamos utilizar caracteres de texto, nos usamos as aspas (''), podendo ser simples ou duplas! (A comunidade recomenda utilizar a aspas simples na maioria dos casos), então o começo do nosso código é o seguinte:

    'Olá, Mundo!'

Pro Python3, todos os comandos são funções, logo todas as funções devem ter parênteses (), então o nosso código ficará da seguinte maneira:

    ('Olá, Mundo!')

Uma das funções mais conhecidas do Python é a função **"print"**, que faz exatamente o que o nosso primeiro programa quer, que é colocar algo na tela, sendo assim, o código final vai ficar da seguinte maneira:

    print('Olá, Mundo!')

Olha só como é simples seguir a lógica da linguagem Python, basicamente queríamos escrever uma mensagem de texto na tela, logo utilizamos a função print, que é utilizada justamente para colocar coisas na tela, e seguindo a lógica do Python onde todo comando é uma função, colocamos os parênteses. Por fim, por se tratar de uma mensagem de texto, o Python pede que o texto esteja dentro de aspas, sendo assim, concluímos um o nosso primeiro código em Python3! 

**Nosso Segundo Programa!**

Já vimos algumas coisas interessantes sobre o Python, agora vamos falar de números. Anteriormente, vimos que para utilizar mensagens de texto no Python, era necessário utilizar as aspas, porém, os números são diferentes, pois podemos utiliza-los  para fazer cálculos matemáticos, Veja a seguir um exemplo onde colocamos na tela um número, e o segundo comando é feito um calculo

*Primeiro Comando:*

    print(7)

*Segundo Comando:*

    print(7+4)

## Variáveis

Anteriormente vimos o comando print, porém ele só funciona caso utilizarmos a mesma mensagem e o mesmo número, com isso, nós podemos utilizar um outro conceito das linguagens de programação, que são as **variáveis!**

*Observação: Toda variável é um objeto!*

Nesse exemplo de programa utilizando as variáveis, eu quero armazenar o nome, idade e peso de uma pessoa, veja a seguir como fazer isso:

    nome =
    idade =
    peso =

Veja que foi utilizado o sinal de igual no exemplo acima, isso é, no Python esse sinal é lido como recebe, sendo assim, a variável é um pequeno espaço de memoria no qual podemos armazenar algum dado, dessa maneira, podemos ler que por exemplo, nome recebe alguma coisa. Veja o exemplo a seguir:

    nome = 'Lucas'
    idade = 19
    peso = 76.7

Com o exemplo dado, é possível dizer que cada variável carrega os valores atribuídos a eles. Agora vamos juntar as variáveis com o nosso comando print no exemplo a seguir:

    nome = 'Lucas'
    idade = 19
    peso = 76.7
    print(nome,idade,peso)

**Um Novo Comando**
No exemplo anterior, foi dado um situação muito interessante onde utilizamos as variáveis, porém, caso eu queira perguntar as informações que estão sendo definidas é possível? A resposta é sim, como comando **"input"** é possível pegar dados onde o usuário pode informar, então seguindo o exemplo anterior, veja o novo programa que pergunta as informações e guarda dentro das variáveis criadas:

    nome = input('Qual é o seu nome?')
    idade = input('Qual é a sua idade?')
    peso = input('Quanto você pesa?')
    print(nome,idade,peso)

Veja que os dados informados pelo usuário foram todos entregues as variáveis

**Parte Prática!**

Até agora já vimos alguns comandos, mas agora é a hora de prática os nossos conhecimentos, acesse o IDLE ou crie um SCRIPT, e faça alguns testes utilizando o que aprendemos até agora.

**Relatório da Parte Prática:**

- É possível fazer a junção de mensagens utilizando a , ou o +, porém, isso depende do caso, ao decorrer do curso vamos aprender a quando utilizar um e quando utilizar o outro
- Para utilizar números quebrados, deve se utilizar o . invés da , 

## Desafios

Com tudo que aprendemos nessa aula, faça os seguintes desafios

OBS: Os códigos dos desafios estão dentro da pasta dessa aula

**Desafio 1:** Crie  um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado.

**Desafio 2:** Crie um script Python que leia o dia, mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.

**Desafio 3:** Crie um script Python que leia dois números e tente mostrar a soma entre eles.