def solution(nums: list[int], target: int) -> list[int]: #type: ignore
    
    for idx in range(0, len(nums)):
        for idx2 in range(idx+1, len(nums)):
            test_sum = nums[idx] + nums[idx2]
            if test_sum == target:
                return[idx, idx2]

print(solution([2, 7, 11, 15], 9))        
print(solution([1,2,3,4,5], 9))    