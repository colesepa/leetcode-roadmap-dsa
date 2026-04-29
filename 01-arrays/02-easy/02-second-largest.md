# Second Largest Number

## Dificuldade
Easy

## Estrutura treinada
Array

## Descrição
Dada uma lista de números inteiros, retorne o segundo maior valor presente na lista.

## Exemplos

Entrada:
[3, 7, 2, 9, 4]

Saída:
7

Entrada:
[10, 5, 8, 1]

Saída:
8

## Restrições
- A lista terá pelo menos 2 elementos.
- Considere que sempre existirá um segundo maior número.
- Não use `sort()`.
- Não use `max()`.

## Antes de resolver, pense:
- Preciso guardar apenas o maior número?
- O que acontece quando encontro um novo maior?
- Como atualizo o segundo maior?

## Hints

### Hint 1
Você precisa controlar duas variáveis: o maior e o segundo maior.

### Hint 2
Quando encontrar um novo maior, o antigo maior vira o segundo maior.

### Hint 3
Se o número não for maior que o maior atual, ele ainda pode ser maior que o segundo maior.

## My solution

```python
def Solution(nums: list[int]) -> int: #type: ignore
    
    max_value: int = nums[0]
    second_max_value : int|None = None
    
    for num in nums[1:]:
        
        if num > max_value:

            second_max_value = max_value
            max_value = num
        
        elif second_max_value is None or num > second_max_value:
            second_max_value = num
    
    if second_max_value is not None:
        return second_max_value
```
## Complexity

Temp = O(n)
Space = O(1)