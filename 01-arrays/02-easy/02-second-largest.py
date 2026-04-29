def Solution(nums: list[int]) -> int: #type: ignore
    
    max_value: int = nums[0]
    second_max_value : int|None = None
    
    for num in nums[1:]:
        
        if num > max_value:

            second_max_value = max_value
            max_value = num
        
        elif second_max_value is None or num > second_max_value:
            second_max_value = num
    
    if second_max_value is not None:
        return second_max_value
            

print(Solution([3,7,2,9,4]))
print(Solution([10,5,8,1]))
