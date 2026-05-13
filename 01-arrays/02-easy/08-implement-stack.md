# Implement Stack

## Dificuldade
Easy

## Estrutura treinada
Stack

## Descrição
Implemente uma stack usando uma lista em Python.

A stack deve ter os seguintes métodos:

- `push(value)`: adiciona um valor ao topo
- `pop()`: remove e retorna o valor do topo
- `peek()`: retorna o valor do topo sem remover
- `is_empty()`: retorna `True` se a stack estiver vazia

## Exemplo

```python
stack = Stack()

stack.push(10)
stack.push(20)

stack.peek()
# 20

stack.pop()
# 20

stack.pop()
# 10

stack.is_empty()
# True
```

### Restrições
- Use uma lista internamente.
- O topo da stack deve ser o final da lista.
- Não use insert(0).
- Não use pop(0).
  
#### Antes de resolver, pense:
- Onde fica o topo da stack?
- Qual operação da lista é O(1)?
- O que deve acontecer se pop() for chamado com a stack vazia?

## Hints
### Hint 1

Use self.items = [].

### Hint 2

push deve usar append.

### Hint 3

pop deve usar pop() sem índice.


## Assinatura sugerida:

```python
class Stack:
    def __init__(self):
        pass

    def push(self, value: int) -> None:
        pass

    def pop(self) -> int | None:
        pass

    def peek(self) -> int | None:
        pass

    def is_empty(self) -> bool:
        pass
```
### My Solution:
```python
from typing import Any

class Stack:
    
    def __init__(self):
        self.items = []
    
    def push(self, item: Any) -> None:
        
        self.items.append(item)
    
    def pop(self) -> Any:
        
        if self.is_empty():
            return None
        return self.items.pop()
    
    def peek(self) -> Any:
        
        if self.is_empty():
            return None
         
        return self.items[len(self.items)-1]
    
    def is_empty(self) -> bool:
        
        if len(self.items) == 0:
            return True
        else:
            return False 
```