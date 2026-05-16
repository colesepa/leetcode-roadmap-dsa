
def my_solution(enum: list[int]) -> list[int]:

    i = 0
    while i < len(enum)-2:
        j = i+1
        if enum[i] == 0 and j <= len(enum)-1:
            while enum[j] == 0:
                j += 1
            enum[i] = enum[j]
            enum[j] = 0
        i += 1

    return enum

input_list = [0,1,0,3,12]
input_list = my_solution(enum=input_list)

print(input_list)

input_list = [0,0,1]
input_list = my_solution(enum=input_list)

print(input_list)


def solution(enum: list[int]) -> list[int]:
    
    position = 0

    # Percorre a lista
    for i in range(0, len(enum)):
     
    # Verifica se o numero na posi
        if enum[i] != 0:
            enum[position] = enum[i]
            position += 1
    
    while position < len(enum):
        enum[position] = 0
        position += 1

    return enum


input_list = [0,1,0,3,12]
input_list = solution(enum=input_list)

print(input_list)

input_list = [0,0,1]
input_list = solution(enum=input_list)

print(input_list)