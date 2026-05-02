# Queue Using List

## Dificuldade
Easy

## Estrutura treinada
Queue

## Padrão
Implementação de estrutura de dados

## Descrição
Implemente uma fila usando uma lista em Python.

A fila deve seguir o comportamento FIFO:

First In, First Out.

Ou seja, o primeiro elemento inserido deve ser o primeiro elemento removido.

A classe deve ter os seguintes métodos:

- enqueue(value): adiciona um valor ao final da fila
- dequeue(): remove e retorna o primeiro valor da fila
- peek(): retorna o primeiro valor da fila sem remover
- is_empty(): retorna True se a fila estiver vazia

## Exemplos

Entrada:
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.peek()

Saída:
10

Entrada:
queue.dequeue()

Saída:
10

Entrada:
queue.dequeue()

Saída:
20

## Restrições
- Use uma lista internamente.
- Não use collections.deque ainda.
- Se a fila estiver vazia:
  - dequeue() deve retornar None
  - peek() deve retornar None

## Antes de resolver, pense:
- Em uma fila, quem sai primeiro?
- Onde você vai inserir novos elementos?
- De onde você vai remover elementos?
- Qual operação pode ficar custosa em uma lista Python?

## Hints

### Hint 1
Fila é FIFO: o primeiro que entra é o primeiro que sai.

### Hint 2
Você pode inserir com append().

### Hint 3
Para remover o primeiro elemento de uma lista, existe pop(0), mas pense no custo disso.

## Sua solução
Cole sua solução aqui depois.

## Análise
Complexidade de tempo:
Complexidade de espaço:

## Revisão
O que errei?
O que aprendi?
Resolveria de novo?