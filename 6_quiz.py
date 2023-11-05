#What will be output of below python code?
list1 = [5, 10, 15, 20, 25, 30]
list2 = list1
id(list1)==id(list2)

list2=list1.copy()
print(id(list1)==id(list2))