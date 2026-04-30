# Two Sum Optimized

## Dificuldade
Easy

## Estrutura treinada
Array / Hashmap

## Descrição
Dada uma lista de números inteiros `nums` e um inteiro `target`, retorne os índices de dois números cuja soma seja igual ao `target`.

Considere que sempre haverá exatamente uma solução válida.

## Exemplos

Entrada:
nums = [2, 7, 11, 15]
target = 9

Saída:
[0, 1]

## Restrições
- Use um dicionário/hashmap.
- Não use o mesmo índice duas vezes.
- Retorne os índices, não os valores.

## Antes de resolver, pense:
- Para cada número, qual valor complementar eu preciso encontrar?
- Como guardar números já vistos?
- O dicionário deve guardar número → índice ou índice → número?

## Hints

### Hint 1
Para cada `num`, calcule `complement = target - num`.

### Hint 2
Verifique se o complemento já apareceu antes.

### Hint 3
Guarde no dicionário o valor como chave e o índice como valor.

### My Solution

```python
def Solution(nums: list[int], target: int) -> list[int]: #type: ignore
    
    hash_map = {}
    for idx in range(0, len(nums)):
        if target - nums[idx] in hash_map:
            complement = target - nums[idx]
            return [hash_map[complement], idx]
        else:    
            hash_map[nums[idx]] = idx
```
### Complexity

Temp = O(n)
Space = O(n)