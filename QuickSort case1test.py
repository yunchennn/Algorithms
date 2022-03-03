Nameofile = "QuickSort.txt"
inFile = open(Nameofile, 'r')

with inFile as f:
    numList = [int(integers.strip()) for integers in f.readlines()]
"""
readlines()返回一个包含每个元素一行的列表。 
请注意，这些行在行尾包含\n （换行符）。 
你可以使用strip()方法去掉这个换行符。 
即呼叫lines[index].strip()为了获得没有换行符的string。
"""
count = 0

def countComparisons(x):
    global count
    if len(x) == 1 or len(x) == 0:
        return x

    else:
        count = count + (len(x)-1)
        
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