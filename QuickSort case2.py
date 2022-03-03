"""
用最後一個element當pivot
https://nbviewer.org/github/anirudhjayaraman/Algorithms/blob/master/Pivot%20Comparisons%20in%20Quick%20Sort.ipynb
"""
NUMLIST_FILENAME = "QuickSort.txt"
# NUMLIST_FILENAME = "1000.txt"

inFile = open(NUMLIST_FILENAME, 'r')

with inFile as f:
    numList = [int(integers.strip()) for integers in f.readlines()]

count = 0

def countComparisons(x):
    global count
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        count += len(x)-1
        x[0],x[-1] = x[-1],x[0]
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