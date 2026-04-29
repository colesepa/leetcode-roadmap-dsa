# Find Maximum Element

## Dificuldade
Easy

## Estrutura treinada
Array

## Descrição
Dada uma lista de números inteiros, retorne o maior valor presente na lista.

## Exemplos

Entrada:
[3, 7, 2, 9, 4]

Saída:
9

Entrada:
[-5, -2, -10, -1]

Saída:
-1

## Restrições
- A lista terá pelo menos 1 elemento.
- Os elementos serão números inteiros.

## Antes de resolver, pense:
- Preciso ordenar a lista?
- Consigo resolver percorrendo apenas uma vez?
- Qual valor inicial devo usar para comparar?

## Hints

### Hint 1
Você precisa guardar o maior valor visto até agora.

### Hint 2
Comece assumindo que o primeiro elemento é o maior.

### Hint 3
Percorra o restante da lista comparando cada número com o maior atual.

## Assinatura sugerida

```python
def solution(nums: list[int]) -> int:
    pass

```
## My Solution

```python

def solution(nums: list[int]) -> int:
    
    max_num = nums[0]
    for num in nums[1:]:

        if num > max_num:
            max_num = num
    
    return max_num
```
## Complexity

Temp = O(n)
Space = 0(1)