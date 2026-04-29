
def solution(nums: list[int]) -> int:
    
    max_num = nums[0]
    for num in nums[1:]:

        if num > max_num:
            max_num = num
    
    return max_num