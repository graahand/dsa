# two sum leetcode

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]



nums = [2, 3, 11, 15,7]

target = 9
print(twoSum(nums, target))
