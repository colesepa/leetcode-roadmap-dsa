
def solution(nums: list[int], target: int) -> int:
    
    count = 0 
    for num in nums:
        if num == target:
            return count
        else:
            count += 1
    return -1 


"""

Análise de complecidade:


    *Tempo: 
            
                        count = 0 
            for num in nums:
                if num == target:
                    return count
                else:
                    count += 1
            return -1

"""