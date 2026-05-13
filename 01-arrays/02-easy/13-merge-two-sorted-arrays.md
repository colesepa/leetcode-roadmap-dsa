# Merge Two Sorted Arrays

## Dificuldade
Easy

## Estrutura treinada
Array

## Padrão
Two Pointers

## Descrição
Dadas duas listas ordenadas em ordem crescente, retorne uma nova lista contendo todos os elementos das duas listas também em ordem crescente.

## Exemplos
Entrada:
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]

Saída:
[1, 2, 3, 4, 5, 6]

Entrada:
nums1 = [1, 2, 7]
nums2 = [3, 4, 5]

Saída:
[1, 2, 3, 4, 5, 7]

Entrada:
nums1 = []
nums2 = [1, 2]

Saída:
[1, 2]

## Restrições
- As duas listas já vêm ordenadas.
- Não use sort().
- Não use sorted().
- Retorne uma nova lista.
- As listas podem estar vazias.

## Antes de resolver, pense:
- Como comparar o menor elemento restante de cada lista?
- Preciso percorrer as duas listas ao mesmo tempo?
- O que acontece quando uma lista acaba antes da outra?

## Hints
### Hint 1
Use dois ponteiros: um para cada lista.

### Hint 2
Compare nums1[i] com nums2[j].

### Hint 3
Quando uma lista acabar, adicione o restante da outra.

## Sua solução
```python

def my_solution (array_1: list[int], array_2: list[int]) -> list[int]:

    if any([len(array_1) == 0, len(array_2) == 0]):
        return array_1 if len(array_1) != 0 else array_2

    if len(array_1) <= len(array_2):
        smallest_array = array_1.copy()
        biggest_array = array_2.copy()
    else:
        smallest_array = array_2.copy()
        biggest_array = array_1.copy()

    output_list = []
    
    while len(smallest_array):
        
        if len(biggest_array) == 0:
            output_list += smallest_array
            break
        
        if smallest_array[0] == biggest_array[0]:
            output_list.append(smallest_array.pop(0))
            output_list.append(biggest_array.pop(0))
            biggest_array.pop(0)

        elif smallest_array[0] < biggest_array[0]:
            output_list.append(smallest_array.pop(0))
        
        elif smallest_array[0] > biggest_array[0]:
            output_list.append(biggest_array.pop(0))
    if len(biggest_array):
        output_list += biggest_array
     
    return output_list
```

## Solução Sugerida
```python

def solution(enum1: list[int], enum2: list[int]) -> list[int]:
    
    i = 0 # Ponteiro 1
    j = 0 # Ponteiro 2 

    outuput = []
    

    while i < len(enum1) and j < len(enum2): # Verificando se os ponteiros estão no range dos arrays

        # Comparação entre os valores dos ponteiros
        if enum1[i] <= enum2[j]:
            outuput.append(enum1[i]) # Adição do menor valor da comparação
            i += 1 # Move o ponteiro do menor valor
        
        else:
            outuput.append(enum2[j]) 
            j += 1 # Move o valor do ponteiro
        
    while i < len(enum1): # Verificação se o ponteiro ainda não chegou ao fim da lista
            outuput.append(enum1[i]) # Adiciona o valor ao final da lista
            i += 1 # Move o ponteiro
        
    while j < len(enum2): # Verifica se o ponteiro ainda não chegou no final da lista 
            outuput.append(enum2[j]) # Adiciona o valor ao final da lista de output
            j += 1 # Move o ponteiro
    
    return outuput

```

## Minha Solução
### Análise de Complexidade

Minha solução apresentou uma complexidade que poderia a chegar O(n²), por conta do .pop(0), onde,
apoós remover o elemento de indice 0, cada elemento da lista tem que ser movido 1 espaço pra esqueda. Já a função pop() é O(1) pois, independete do tamnho da lista a função só irá remover
o primeiro elemento sem alterar os outros.

## Revisão
Apesar da minha solução apresentar o resultado desejado, a complexidade apresentou-se como O(n²), justamento por utilizar o pop(0) e não utilizar índices (ponteiros). Por sua vez, a solução sugerida apresenta-se como O(n+m). 

Com esse exercício, pude melhorar a compreensão da complexidade de extração de uma lista em python, como por exemplo, o caso do pop(0) que pode ser O(n). Aprendi também, a importânica dos ponteiros. 