def solution(nums: list[int], target: int) -> list[int]: #type: ignore
    
    hash_map = {}
    for idx in range(0, len(nums)):
        if target - nums[idx] in hash_map:
            complement = target - nums[idx]
            return [hash_map[complement], idx]
        else:    
            hash_map[nums[idx]] = idx

print(solution([2, 7, 11, 15],9))