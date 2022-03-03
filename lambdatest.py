a = [('b',4), ('a',12), ('d',7), ('h',6), ('j',3)]
a.sort(key = lambda x:x[1]) #排序的位置 #lambda表示一个元组
# a.sort(key = lambda x:x[0])
print(a)