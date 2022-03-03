def invcount(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]>arr[j]:
                arr[i]=arr[j]
                i = i + 1

arr = [1, 20, 6, 4, 5]
print("Number of inversions are", invcount(arr))