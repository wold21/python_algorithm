def solution(nums):
    answer = 0
    length = len(nums) // 2
    nums = list(set(nums))
    for value in nums:
        if answer < length:
            answer += 1
    print(answer)


nums1 = [3, 3, 3, 2, 2, 2]
solution(nums1)

nums2 = [3, 3, 3, 2, 2, 4]
solution(nums2)

nums3 = [3, 1, 2, 3]
solution(nums3)
