# Two Sum Brute Force

## Dificuldade
Easy

## Estrutura treinada
Array

## Descrição
Dada uma lista de números inteiros `nums` e um inteiro `target`, retorne os índices de dois números cuja soma seja igual ao `target`.

Considere que sempre haverá exatamente uma solução válida.

## Exemplos

Entrada:
nums = [2, 7, 11, 15]
target = 9

Saída:
[0, 1]

Explicação:
nums[0] + nums[1] = 2 + 7 = 9

## Restrições
- Não use `dict` ainda.
- Não use `set` ainda.
- Use força bruta com dois loops.
- Não use o mesmo índice duas vezes.

## Antes de resolver, pense:
- Como comparar cada número com todos os outros?
- Como evitar usar o mesmo elemento duas vezes?
- O que devo retornar: valores ou índices?

## Hints

### Hint 1
Você precisa testar pares de números.

### Hint 2
Use dois `for`.

### Hint 3
O segundo `for` pode começar em `i + 1`.

### My Solution

```python
def solution(nums: list[int], target: int) -> list[int]: #type: ignore
    
    for idx in range(0, len(nums)):
        for idx2 in range(idx+1, len(nums)):
            test_sum = nums[idx] + nums[idx2]
            if test_sum == target:
                return[idx, idx2]
```
### Complexity

Temp = O(n²)
Space = O(1)