# from typing import Any

from doctest import OutputChecker


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

print(solution([1,3,5], [2, 4, 6])) 
print(solution([1, 2, 7], [3, 4, 5])) 
print(solution([], [1,2])) 