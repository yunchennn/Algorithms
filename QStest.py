intervals = [10, 55, 15, 23, 11, 7, 87, 6]
# x = intervals[0]

# res = [intervals[0]]
# hi = []
# lo = []
# print (res)

# for i in range(1, len(intervals)-1):
#     if intervals[i] < x:
#         lo.append(intervals[i])
#     i = i + 1
#     #print(lo)

#     if intervals[i] > x:
#         hi.append(intervals[i])
#     i = i + 1
#     #print(hi)
# print (res+lo+hi)

"""
用第一個element當pivot
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
        i = 0
        # print(intervals)
        for j in range(len(x)-1):
            
            if x[j+1] < x[0]:
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
                #print(x)
        x[0],x[i] = x[i],x[0]
        print(intervals)
        first_part = countComparisons(x[:i])
        second_part = countComparisons(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part

countComparisons(intervals)
print (count)

