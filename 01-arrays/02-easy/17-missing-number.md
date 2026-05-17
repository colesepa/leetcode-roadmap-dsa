# Missing Number

## Dificuldade
Easy

## Estrutura treinada
Array / Hashmap

## Padrão
Soma matemática / Busca com conjunto

## Descrição
Dada uma lista contendo `n` números distintos no intervalo de `0` até `n`, retorne o único número que está faltando.

## Exemplos

Entrada:
[3, 0, 1]

Saída:
2

Entrada:
[0, 1]

Saída:
2

Entrada:
[9,6,4,2,3,5,7,0,1]

Saída:
8

## Restrições
- A lista contém números distintos.
- Os valores estão no intervalo de `0` até `n`.
- Sempre haverá exatamente um número faltando.
- Não use `sort()`.

## Antes de resolver, pense:
- Qual seria a soma esperada dos números de 0 até n?
- Qual é a soma real da lista?
- A diferença entre essas somas revela o quê?

## Hints

### Hint 1
Para `n = 3`, os números possíveis são `0, 1, 2, 3`.

### Hint 2
A soma de `0` até `n` pode ser calculada com fórmula.

### Hint 3
Número faltando = soma esperada - soma real.

## Sua solução
```python
def my_solution(enum: list[int]) -> int:
    
    if not len(enum):
        return 0
    max_value = max(enum) 
    expected_sum = 0
    real_sum = 0
    
    for i in range(0, max_value + 1):
        expected_sum += i
        if i <= len(enum)-1:
            real_sum += enum[i]
    miss_number = expected_sum - real_sum

    if miss_number == 0:
        miss_number = max_value + 1
     
    return miss_number    
```
## Soulção Sugerida
```python
def solution(nums: list[int]) -> int:
    n = len(nums)

    expected_sum = n * (n + 1) // 2
    real_sum = sum(nums)

    return expected_sum - real_sum
```


## Análise
Complexidade de tempo:
Complexidade de espaço:

## Revisão
A solução sugerida apresenta uma solução com uma formula matemática que resulta no valor da soma de um conunto. Essa formula era desconhecida por mim.
Na solução sugerida a complexidade de tempo é extremamente eficiente O(1). Minha 
solução se apresentou ineficiente, uma vez que preciso percorrer a lista ao menos
uma vez O(n).