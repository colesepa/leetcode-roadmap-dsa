# Contains Duplicate

## Dificuldade
Easy

## Estrutura treinada
Array / Hashmap

## Padrão
Busca com conjunto/hash

## Descrição
Dada uma lista de inteiros, retorne `True` se algum valor aparecer pelo menos duas vezes.

Se todos os elementos forem distintos, retorne `False`.

## Exemplos

Entrada:
[1, 2, 3, 1]

Saída:
True

Entrada:
[1, 2, 3, 4]

Saída:
False

Entrada:
[]

Saída:
False

## Restrições
- A lista pode estar vazia.
- Não use `sort()`.
- Não use `count()` dentro de loop.
- Tente resolver em O(n).

## Antes de resolver, pense:
- Como saber se um número já apareceu antes?
- Qual estrutura permite busca rápida?
- Preciso guardar contagem ou apenas presença?

## Hints

### Hint 1
Use uma estrutura para guardar os valores já vistos.

### Hint 2
Antes de inserir um número, verifique se ele já está nessa estrutura.

### Hint 3
Você não precisa contar quantas vezes apareceu; só precisa saber se apareceu antes.

## Sua solução
```python
def my_solution(enum: list[int]) -> bool:
    
    hashtbale = {}
    if not enum:
        return False
    for num in enum:
        
        if hashtbale.get(num) is None:
            hashtbale[num] = 1
        else:
            return True
    
    return False
```

## Análise
Complexidade de tempo: O(n)
Complexidade de espaço: O(1)

## Revisão
Nessa questão não apresentei erro conssitente.