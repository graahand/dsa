# maximum subarray problem leetcode 

def maxSubArray(nums):
    current_sum = 0
    maximum_sum = nums[0]
    for number in nums:
        current_sum = max(number, current_sum + number)
        maximum_sum = max(maximum_sum, current_sum)
    return maximum_sum

nums = [1, 0, 3, -4]
print(maxSubArray(nums))

'''
1
current sum = 0
maximum sum = 1
for 1 in nums:
current sum = max(1, 0+1) = 1
maximum sum = max(1,1) = 1

0
current sum = 1
maximum sum = 1
for 0 in nums:
current sum = max(0, 1) = 1
maximum sum = max(1, 1) =1 

3
current sum = 1
maximum sum = 1
for 3 in nums:
current sum = max(3, 1+3) = 4
maximum_sum = max(1, 4) = 4

-4
current sum = 4
maximum sum = 4
current sum = max(4, 4-4) = 4
maxium sum = max(4, 4) = 4

return 4

if I have to return the element that were used for caculating the elements how would I do that?

def maxSubArray(nums):
    current_sum = 0
    maximum_sum = nums[0]
    start = 0  # start of current subarray
    end = 0    # end of maximum subarray
    max_start = 0  # start of maximum subarray
    
    for i, number in enumerate(nums):
        if number > current_sum + number:  # starting a new subarray
            current_sum = number
            start = i
        else:
            current_sum = current_sum + number
        
        if current_sum > maximum_sum:
            maximum_sum = current_sum
            end = i
            max_start = start
    
    return maximum_sum, nums[max_start:end+1]

nums = [1, 0, 3, -4]
sum_val, subarray = maxSubArray(nums)
print(f"Maximum sum: {sum_val}")
print(f"Subarray: {subarray}")

current sum = 0
maximum sum = 1
start = 0 
end = 0 
max_start = 0 

for 0, 1 in nums
if 1 > 0 + 1: 
current sum = 1
start = i 

if 1 > 0
maximum sum = 1
end = 0
max start = 0

0
current sum = 1
maximum sum = 1
start = 0 
end = 0 
max start = 0 
for 1, 0 in nums
if 0 > 1 + 0 false
else
current sum = 1 + 0 = 1

if 1

'''


# -2 
# max()-2, 0-2 = -2
# max(-2, -2) = -2
# current sum = -2
# maximum sum = -2
# 1
# max(-1, -2+1) = 1
# max(-2, 1) = 1
# current sum = 1
# maximum sum = 1

# -3
# max(-3, 1-3) = -2
# max(1, -2) = 1
# current sum = -2
# maximum sum = 1

# 4
# max(4, -2+4) = 4
# max(1, 4) = 4
# current sum = 4
# maximum sum = 4

