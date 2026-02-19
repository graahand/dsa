def isSubsequence(s, t):
    i, j = 0, 0 
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return True if i == len(s) else False


s = 'gdf'
t = 'abcdefgdf'
print(isSubsequence(s, t))
'''
s = 'gdf'
t = 'abcdefgdf'

i, j = 0, 0

first iteration:
while 0 < 3 and 0 < 10:
if g = a (false)
j = 1

second iteration: 
while 0 < 3 and 1 < 10:
if g = b (false)
j = 2

third iteration:
while 0 < 3 and 2 < 10:
if g = c (false)
j = 3

fourth iteration: 
while 0 < 3 and 3 < 10:
if g = d (false)
j = 4

fifth iteration:
while 0 < 3 and 4 < 10:
if g = e (false)
j = 5

sixth iteraton: 
while 0 < 3 and 5 < 10:
if g = f (false)
j = 6

seventh iteration:
while 0 < 3 and 6 < 10:
if g = g (true)
i = 1
j = 7

eighth iteration: 
while 1 < 3 and 7 < 10:
if d = d (true)
i = 2
j = 8

ninth iteration:
while 2 < 3 and 8 < 10:
if f = g (false)
j = 9

tenth iteration: 
while 2 < 3 and 9 < 10:
if f = d (false)
j = 10

while 2 < 3 and 10 < 10 (false)
return True if 2 == 3 else False (false)    





'''