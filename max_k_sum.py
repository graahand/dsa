from collections import defaultdict

def max_k_sum(numbers, k):
    merodict = defaultdict(int)
    pairs = 0 
    # result = []

    for number in numbers:
        if merodict[k-number] > 0:
            pairs += 1
            # if we were required to return actual pairs
            # result.append((number, k-number))
            merodict[k-number] -= 1
        else:
            merodict[number] += 1
    return pairs 


numbers = [1, 2, 3, 4, 3]
k = 6
print(max_k_sum(numbers, k))


''' 
Simulation:

numbers = [1, 2, 3, 4, 3]
k = 6

merodict = {}
pairs = 0 

for 1 in numbers: 
if merodict[5] > 0 (false because merodict[5] = 0):
else:
merodict[1] += 1 = {1: 1}

for 2 in numbers: 
if merodict[4] > 0 (false because merodict[4] = 0):
else:
merodict[2] += 1 = {1: 1, 2: 1}

for 3 in numbers: 
if merodict[6-3] > 0 (false because merodict[3] = 0):
else:
merodict[3] += 1 = {1: 1, 2: 1, 3: 1}

for 4 in numbers:
if merodict[6-4] > 0 (true because merodict[2] = 1):
pairs += 1 = 1
merodict[6-4] = merodict[2] -= 1 = {1: 1, 2: 0, 3: 1} 

for 3 in numbers: 
if meroedict[6-3] > 0 (true because merodict[3] = 1):
pairs += 1 = 2
merodict[6-3] = merodict[3] -= 1 = {1: 1, 2: 0, 3: 0}

return pairs = 2


'''






    
