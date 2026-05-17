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

print(my_solution([1, 2, 3, 1]))
print(my_solution([1, 2, 3, 4]))
print(my_solution([]))