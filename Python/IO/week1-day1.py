# input : nums(숫자배열), target(목표 숫자)
# nums 안의 두 수를 더한 값이 target과 같은 조합이 한 쌍 존재한다.
# output : 조합의 index를 담은 배열

def two sum(nums, target):
    for i in nums:
        for j in nums[nums.index(i)+1:]:
            if i + j == target:
                return [nums.index(i), nums.index(j)]
