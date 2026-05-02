# Min Stack

## Dificuldade
Easy / Medium

## Estrutura treinada
Stack

## Padrão
Design de estrutura de dados

## Descrição
Implemente uma stack que, além das operações comuns, consiga retornar o menor valor atual em O(1).

A classe deve suportar as seguintes operações:

- push(value): adiciona um valor ao topo
- pop(): remove e retorna o valor do topo
- peek(): retorna o valor do topo sem remover
- get_min(): retorna o menor valor atual da stack
- is_empty(): retorna True se a stack estiver vazia

## Exemplos

Entrada:
push(5)
push(3)
push(7)
get_min()

Saída:
3

---

Entrada:
pop()
get_min()

Saída:
3

---

Entrada:
pop()
get_min()

Saída:
5

## Restrições
- Use lista internamente.
- Não use min() diretamente.
- Todas as operações devem ser O(1).
- Se a stack estiver vazia:
  - pop() retorna None
  - peek() retorna None
  - get_min() retorna None

## Antes de resolver, pense:
- Como manter o menor valor sem percorrer toda a lista?
- O que acontece com o mínimo quando você remove elementos?
- Uma única stack é suficiente?

## Hints

### Hint 1
Use uma stack principal para os valores.

### Hint 2
Use uma segunda stack para acompanhar os mínimos.

### Hint 3
Sempre compare o novo valor com o mínimo atual ao fazer push.

## Sua solução
Cole sua solução aqui depois.

## Análise
Complexidade de tempo:
Complexidade de espaço:

## Revisão
O que errei?
O que aprendi?
Resolveria de novo?