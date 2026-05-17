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

print(my_solution([3, 0, 1]))
print(my_solution([0, 1]))
print(my_solution([9,6,4,2,3,5,7,0,1]))
print(my_solution([]))