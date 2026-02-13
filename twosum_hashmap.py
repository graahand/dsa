# hashmap two sum 

def twoSum(nums, target):
    hashmap = {}
    for index, number in enumerate(nums):
        required_difference = target - number
        if required_difference in hashmap:
            return [hashmap[required_difference], index]
        hashmap[number] = index


nums = [2, 3, 11, 15,7] 
target = 9
print(twoSum(nums, target))



'''
hashmap = {}
for 0, 2 in nums
required_difference = 9 -2 
if 2 in hasmap False
hashmap[2] = 0


hashmap = {2:0}
for 1, 3 in nums
required_difference = 9-3
if 6 in hashmap False
hashmap[3] = 1

hashmap = {2:0, 3:1}
for 2, 11 in nums:
required_difference = 9-11 = -2 
if -2 in hashmap False
hashmap[-2] = 2

hashmap = {2:0, 3:1, -2:2}
for 3, 15 in nums:
required_difference = 9-15 = -6
if -6 in hashmap False
hashmap[-6] = 3

hashmap = {2:0, 3:1, -2:2, -6:3}
for 4, 7 in nums: 
required_difference = 9-7 = 2
if 2 in hashmap True
return [hashmap[2], 4]

0, 4






'''