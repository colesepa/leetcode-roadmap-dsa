def my_solution(enum1: list[int], enum2: list[int]) -> list[int]:
    
    output_set = set()
    hashtable = {}
    hashtable_control = {}
    
    if len(enum1) >= len(enum2):

        for num in enum1:
            hashtable[num] = True

        for num2 in enum2:
            if num2 in hashtable.keys() and num2 not in hashtable_control.keys() :
                output_set.add(num2)
                hashtable_control[num2] = True
    else:
        for num2 in enum2:
            hashtable[num2] = True

        for num in enum1:
            if num in hashtable.keys() and num not in hashtable_control.keys():
                output_set.add(num)
                hashtable_control[num] = True
    return list(output_set)


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(my_solution(nums1, nums2))

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(my_solution(nums1, nums2))

def solution(nums1: list[int], nums2: list[int]) -> list[int]:

    seen = set(nums1)
    output = set()

    for num in nums2:
        if num in seen:
            output.add(num)
    
    return list(output)

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(solution(nums1, nums2))

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(solution(nums1, nums2))