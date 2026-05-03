# Queue Using Two Stacks

## Dificuldade
Medium

## Estrutura treinada
Queue / Stack

## Padrão
Implementação de estrutura de dados

## Descrição
Implemente uma fila usando duas stacks.

A fila deve seguir o comportamento FIFO:

First In, First Out.

A classe deve ter os métodos:

- enqueue(value): adiciona um valor ao final da fila
- dequeue(): remove e retorna o primeiro valor da fila
- peek(): retorna o primeiro valor da fila sem remover
- is_empty(): retorna True se a fila estiver vazia

## Exemplos

Entrada:
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
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
- Use duas listas como stacks.
- Não use pop(0).
- Não use insert(0).
- Não use collections.deque.
- Se a fila estiver vazia:
  - dequeue() deve retornar None
  - peek() deve retornar None

## Antes de resolver, pense:
- Como uma stack inverte a ordem dos elementos?
- Como duas stacks podem simular FIFO?
- Quando vale a pena transferir elementos de uma stack para outra?

## Hints

### Hint 1
Use uma stack para entrada e outra para saída.

### Hint 2
No enqueue, empilhe na stack de entrada.

### Hint 3
No dequeue, se a stack de saída estiver vazia, transfira todos os itens da entrada para a saída.

## Sua solução
Cole sua solução aqui depois.

## Análise
Complexidade de tempo:
Complexidade de espaço:

## Revisão
O que errei?
O que aprendi?
Resolveria de novo?