Este repositório contém as implementações solicitadas no desafio técnico, divididas em dois problemas clássicos, cada um resolvido em duas abordagens: recursiva e linear (iterativa).

A resolução das perguntas conceituais (modelo OSI, sistemas operacionais e projetos open source) foi enviada por e-mail, conforme instruído no enunciado.
Linguagem utilizada: Python 3

Descrição das soluções

Fibonacci:


fibonacci_recursivo.py: A solução divide o problema em subproblemas menores do mesmo tipo: fib(n) é calculado a partir de fib(n-1) e fib(n-2), até chegar nos casos base (fib(0) = 0 e fib(1) = 1). A função "desce" a árvore de chamadas até os casos base e depois "sobe" somando os resultados.
Uma abordagem que acaba recalculando os mesmo valores várias vezes, sendo exponencial.

fibonacci_linear.py: Em vez de recalcular subproblemas, a solução constrói a sequência "de baixo para cima": parte dos valores conhecidos (fib(0) e fib(1)) e vai somando um termo por vez até chegar em N, guardando apenas os dois últimos valores calculados a cada passo.


primos_linear.py: Para cada número do intervalo de 2 até N, a solução testa se existe algum divisor além de 1 e do próprio número. Para reduzir o número de testes, os divisores são verificados apenas até a raiz quadrada do número -caso não exista divisor até esse ponto, também não existirá divisor maior, já que divisores aparecem em pares que se multiplicam entre si para resultar no número original. Uma variável de controle acompanha se algum divisor foi encontrado durante o laço.


primos_recursivo.py: Usa a mesma lógica da raiz quadrada da versão linear, mas substitui o laço de teste de divisores por chamadas recursivas: a cada chamada, a função testa um único divisor e, se não for conclusivo, chama a si mesma testando o divisor seguinte. A recursão para em um de dois casos base: quando o divisor testado ultrapassa a raiz quadrada do número (indicando que ele é primo) ou quando um divisor exato é encontrado (indicando que não é primo).
