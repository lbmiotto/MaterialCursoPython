# Utilizando Módulos

Como vimos anteriormente, é possível fazer muitas coisa no Python, porém existe uma função que pode te dar mais possibilidades do que fazer. Nessa aula vamos trabalhar um abordar um tema muito popular que são os módulos, ou bibliotecas!

**Bibliotecas:**

Muitos acham que quando instalamos o Python, teremos tudo que a linguagem tem a oferecer, porém, isso é uma mentira, quando instalamos o Python, apenas o essencial da linguagem foi instalado, sendo assim, saiba que é possível instalar, ou "importar" mais funcionabilidades, que só o Python normal não tem. Pense no exemplo a seguir: Quando compramos um carro, ele vem somente com o necessário para suprir a função dele, que é dirigir de um lado pro outro, porém, podemos adicionar módulos extras em nossa carro, como ar-condicionado, vidro elétrico e etc. Formando um paralelo com a programação, o Python utiliza o mesmo principio, pois instalamos o Python com tudo que é necessário para o Python funcionar, porém, através do comando "import" podemos adicionar módulos extras, com funções extras. Veja o exemplo a seguir:

    import math
    
Veja que quando colocamos a nossa importação antes de começar a escrever os códigos, é possível utilizar os comandos novos, que não funcionariam antes de importar a biblioteca. Nesse caso, utilizamos a biblioteca math, que é uma das bibliotecas mais famosas do Python, que possibilita o uso de funções matemáticas, assim, facilitando o raciocínio que o programador tem.

OBS: caso você queira importar apenas uma função especifica de uma biblioteca, você pode utilizar o seguinte comando como exemplo:

    from math import ()


**Biblioteca Math:**
 
 Como mencionamos o biblioteca Math como exemplo, veja a seguir algumas funções que podemos utilizar ao importar essa biblioteca:

- ceil: Arredonda valores para cima
- floor: Arredonda valores para baixo
- trunc: Elimina todos os valores depois da virgula
- pow: Faz uma potência (**)
- sqrt: Calcula a raiz quadrada  
- factorial: Calcula uma fatorial

Veja mais funções e mais bibliotecas em -> [www.python.org](https://docs.python.org/pt-br/3/library/index.html)

**Vamos pra prática!**

Vamos fazer alguns teste e para praticar a importação e o uso das funções.

    # Biblioteca Math
    import Math
    num = int(input('Informe um número: '))
    raiz = math.sqrt(num)
    print('A raiz de {} [e {}'.format(num, florr(raiz)))
    
    # Biblioteca random
    import random
    num1 = random.randint(1, 10)
    print(num1)