def moveZeroes(nums):
    if len(nums) == 1: 
        return 
    

    i = 0
    while i < len(nums):
        if nums[i] == 0:
            break
        i+=1


    if i == len(nums):
        return 
    

    j = i + 1
    while j < len(nums):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i +=1 
        j +=1

'''
nums = [0, 1, 0, 3, 12]
len(nums) = 5

# --- Initialization Phase ---
i = 0
while 0 < 5: true
if nums[0] == 0: (0 == 0 is true)
break 
# i remains 0

if 0 == 5: false
j = 0 + 1 = 1

# --- Second Loop Phase ---

# Iteration 1
while 1 < 5: (true)
if nums[1] != 0: (1 != 0 is true)
swap nums[0], nums[1] -> [1, 0, 0, 3, 12]
i = 1
j = 2

# Iteration 2
while 2 < 5: (true)
if nums[2] != 0: (0 != 0 is false)
# Skip swap block
j = 3

# Iteration 3
while 3 < 5: (true)
if nums[3] != 0: (3 != 0 is true)
swap nums[1], nums[3] -> [1, 3, 0, 0, 12]
i = 2
j = 4

# Iteration 4
while 4 < 5: (true)
if nums[4] != 0: (12 != 0 is true)
swap nums[2], nums[4] -> [1, 3, 12, 0, 0]
i = 3
j = 5

# Termination
while 5 < 5: (false)
Loop Ends

Final Array: [1, 3, 12, 0, 0]
'''