"""
리트코드 1 두 수의 합

"""
nums = [2, 7, 11, 15]
target = 9
answer = []

# 브루트 포스 방식
def twoSum(nums:list , target: int):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i, j]


# in을 이용한 탐색
def twoSum(nums:list , target: int):
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]

# 첫 번째 수를 뺀 결과 키 조회
def twoSum(nums:list , target: int):
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i

    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]

# 조회 구조 개선
def twoSum(nums:list , target: int):
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i

# 투 포인터 이용(불가능 -- 정렬되어잇다는 기준에서만 가능)
def twoSum(nums:list , target: int):
    nums.sort()
    left, right = 0, len(nums) - 1
    while not left == right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]