# First Unique Character

## Dificuldade
Easy

## Estrutura treinada
Hashmap / Queue

## Padrão
Contagem de frequência

## Descrição
Dada uma string, retorne o primeiro caractere que aparece apenas uma vez.

Se não existir nenhum caractere único, retorne `None`.

## Exemplos
Entrada:
"leetcode"

Saída:
"l"

Entrada:
"loveleetcode"

Saída:
"v"

Entrada:
"aabb"

Saída:
None

## Restrições
- A string pode estar vazia.
- A string contém apenas letras minúsculas.
- Não use `count()` dentro de loop.
- Preserve a ordem dos caracteres.

## Antes de resolver, pense:
- Como contar quantas vezes cada caractere aparece?
- Depois de contar, como descobrir quem apareceu primeiro?
- Preciso de uma fila explícita ou consigo resolver com duas passagens?

## Hints
### Hint 1
Use um dicionário para contar frequências.

### Hint 2
Faça uma primeira passagem contando os caracteres.

### Hint 3
Faça uma segunda passagem procurando o primeiro caractere com frequência 1.

## Sua solução
```python
from typing import Any

def solution(text: str) -> str | None:
    
    count: dict[str, int] = {}
    if not text:
            return None

    for char in text:
        count[char] = count.get(char, 0) + 1

    for char in text:
        if count[char] == 1:
            return char
    
    return None
```

## Análise
Complexidade de tempo:
Complexidade de espaço:

## Revisão
O que errei? 
Errei na otimização da complexidade de tempo, utilizei funções que internamente podem se tornar O(n²). 

O que aprendi?
A contagem com dict, em conjunto com o "get", nos dá a liberdade de preencher pela primeira vez (get retona "None") e somar caso haja valor para a chave da vez.

Resolveria de novo?