lst =['Apple', 'Guava', 'Mango', 'Banana', 'kiwi']

print("Length of list:",len(lst))
print("first element:",lst[0])
print("last Element:",lst[-1])

lst.append('Papaya')
print("Updated List:", lst)

lst.remove('Guava')
print("Updated List:", lst)

lst.sort()
print("sorted List:", lst)

lst.pop(1)
print("Updated List:", lst)

lst.reverse()
print("reversed List:", lst)

print("multiplication on list:", lst*2)

lst=lst[:4]
print("sliced list:", lst)

lst.clear()
print("updated list:" ,lst)
