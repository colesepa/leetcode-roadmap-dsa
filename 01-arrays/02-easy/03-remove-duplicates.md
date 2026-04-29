# Remove Duplicates

## Dificuldade
Easy

## Estrutura treinada
Array / List

## Descrição
Dada uma lista de números inteiros, retorne uma nova lista contendo os elementos sem repetição, mantendo a ordem original.

## Exemplos

Entrada:
[1, 2, 2, 3, 1, 4]

Saída:
[1, 2, 3, 4]

Entrada:
[5, 5, 5]

Saída:
[5]

## Restrições
- Não use `set(nums)` diretamente como retorno.
- A ordem original deve ser preservada.
- A lista pode conter números negativos.
- A lista pode estar vazia.

## Antes de resolver, pense:
- Como saber se um número já apareceu antes?
- Preciso preservar a ordem?
- Qual estrutura me ajuda a consultar rapidamente valores já vistos?

## Hints

### Hint 1
Você pode usar uma lista auxiliar para guardar o resultado.

### Hint 2
Você precisa verificar se cada número já apareceu antes.

### Hint 3
Uma estrutura do tipo `set` pode ajudar a verificar presença em O(1).

## My Solution

```python
def solution(nums: list[int]) -> list[int]:
    
    unique_values: set[int] = set()
    list_unique: list[int] = []
    
    for num in nums:
        
        if num not in unique_values:
            list_unique.append(num)
            unique_values.add(num)
        else:
            pass
    
    return list_unique
```
## Complexity
Temp = O(n)
Space = O(n) 