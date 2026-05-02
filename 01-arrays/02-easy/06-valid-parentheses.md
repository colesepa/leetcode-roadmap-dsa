# Valid Parentheses

## Dificuldade
Easy

## Estrutura treinada
Stack

## Descrição
Dada uma string contendo apenas os caracteres `(`, `)`, `{`, `}`, `[` e `]`, determine se a string é válida.

Uma string é válida se:
- Todo par aberto é fechado pelo mesmo tipo de parêntese.
- Os pares são fechados na ordem correta.

## Exemplos

Entrada:
"()"

Saída:
true

Entrada:
"()[]{}"

Saída:
true

Entrada:
"(]"

Saída:
false

Entrada:
"([)]"

Saída:
false

Entrada:
"{[]}"

Saída:
true

## Restrições
- A string contém apenas caracteres de parênteses.
- Use uma stack/lista.
- Não use regex.

## Antes de resolver, pense:
- O que devo fazer quando encontro um caractere de abertura?
- O que devo fazer quando encontro um caractere de fechamento?
- Como saber se o último caractere aberto combina com o atual?

## Hints

### Hint 1
Use uma lista como pilha.

### Hint 2
Quando encontrar abertura, empilhe.

### Hint 3
Quando encontrar fechamento, compare com o topo da pilha.

### My Solution
```python
def solution(text: str) -> bool:
   
    pair = {
        "(":")",
        "{":"}",
        "[":"]",
        ")":"(",
        "}":"{",
        "]":"["
    }
    
    stack = []
    for char in text:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            if pair[char] != stack.pop():
                return False
    return len(stack) == 0
```
### Complexity
Temp -> O(n)
Space -> O(n)

# Observações
Em geral, para estuturas Lifo, devemos priorizar o topo da lista no final da estrutura.
Se eu conmstruisse o exercicio utilizando uma linked list, a complexidade seria O(n), uma vez que 
inserir elemento no head e no tail tem baixo custo.