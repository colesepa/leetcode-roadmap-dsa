def solution(nums: list[int]) -> list[int]:
    
    unique_values: set[int] = set()
    list_unique: list[int] = []
    
    for num in nums:
        
        if num not in unique_values:
            list_unique.append(num)
            unique_values.add(num)
        else:
            pass
    
    return list_unique