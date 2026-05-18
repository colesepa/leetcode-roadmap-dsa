# Intersection of Two Arrays

## Dificuldade
Easy

## Estrutura treinada
Array / Hashmap / Set

## Padrão
Busca com conjunto/hash

## Descrição
Dadas duas listas de inteiros, retorne uma lista contendo os valores que aparecem nas duas listas.

Cada valor deve aparecer apenas uma vez no resultado.

A ordem do resultado não importa.

## Exemplos
Entrada:
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

Saída:
[2]

Entrada:
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

Saída:
[9, 4]

## Restrições
- Não use `set(nums1) & set(nums2)` diretamente.
- Cada valor deve aparecer apenas uma vez no resultado.
- A ordem do resultado não importa.
- Tente resolver em O(n + m).

## Antes de resolver, pense:
- Como saber rapidamente se um valor de uma lista aparece na outra?
- Como evitar duplicatas no resultado?
- Qual lista faz mais sentido transformar em estrutura de busca?

## Hints

### Hint 1
Use um `set` para guardar os valores de uma das listas.

### Hint 2
Percorra a outra lista e verifique se cada valor existe no set.

### Hint 3
Use outro set ou uma verificação para evitar duplicatas no resultado.

## Sua solução
```python
def my_solution(enum1: list[int], enum2: list[int]) -> list[int]:
    
    output_set = set()
    hashtable = {}
    hashtable_control = {}
    
    if len(enum1) >= len(enum2):

        for num in enum1:
            hashtable[num] = True

        for num2 in enum2:
            if num2 in hashtable.keys() and num2 not in hashtable_control.keys() :
                output_set.add(num2)
                hashtable_control[num2] = True
    else:
        for num2 in enum2:
            hashtable[num2] = True

        for num in enum1:
            if num in hashtable.keys() and num not in hashtable_control.keys():
                output_set.add(num)
                hashtable_control[num] = True
    return list(output_set)
```

## Solução Sugerida
```python
def my_solution(enum1: list[int], enum2: list[int]) -> list[int]:
    
    output_set = set()
    hashtable = {}
    hashtable_control = {}
    
    if len(enum1) >= len(enum2):

        for num in enum1:
            hashtable[num] = True

        for num2 in enum2:
            if num2 in hashtable.keys() and num2 not in hashtable_control.keys() :
                output_set.add(num2)
                hashtable_control[num2] = True
    else:
        for num2 in enum2:
            hashtable[num2] = True

        for num in enum1:
            if num in hashtable.keys() and num not in hashtable_control.keys():
                output_set.add(num)
                hashtable_control[num] = True
    return list(output_set)
```

## Análise
Complexidade de tempo:
Complexidade de espaço:

## Revisão
Apesar da minha solução apresentar resultados corretos, ela se apresenta, com
lógica mais complexa do que o necessário. Acrescentei um hash de controle que 
em tese não era preciso, uma vez que o o próprio "set" pode cuidar das duplicatas. 
Dessa forma, faz-se necessário percorrer pelo menos uma vez uma das listas 
(sem contar o percorrer do "set"), e verificar se o valor ja está no set de output.