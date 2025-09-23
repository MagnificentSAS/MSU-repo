list1 = [x for x in range(5, 16, 1)]
list2 = [x for x in 'abcdefghijk']
list1[3:7] = list2[-5:]
print(list1)
