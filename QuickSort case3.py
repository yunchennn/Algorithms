"""
Median of 3 Pivot Rule
"""
NUMLIST_FILENAME = "QuickSort.txt"
# NUMLIST_FILENAME = "1000.txt"

inFile = open(NUMLIST_FILENAME, 'r')

with inFile as f:
    numList = [int(integers.strip()) for integers in f.readlines()]

count = 0

def middle_index(x):
    if len(x) % 2 == 0:
        middle_index = len(x)//2 - 1
    else:
        middle_index = len(x)//2
    return middle_index

def median_index(x,i,j,k):
    if (x[i]-x[j])*(x[i]-x[k]) < 0:
        return i
    elif (x[j]-x[i])*(x[j]-x[k]) < 0:
        return j
    else:
        return k

def countComparisons(x):
    global count
    if len(x) == 1 or len(x) == 0:
        return x        
    else:
        count += len(x)-1
        k = median_index(x, 0, middle_index(x), -1)
        if k != 0: x[0], x[k] = x[k], x[0]
        i = 0
        for j in range(len(x)-1):
            if x[j+1] < x[0]:
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0],x[i] = x[i],x[0]
        first_part = countComparisons(x[:i])
        second_part = countComparisons(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part

countComparisons(numList)
print (count)