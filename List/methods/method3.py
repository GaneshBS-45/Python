lst=[23,45,853,77,999,"anirudh",True]
print(lst)
lst.append([1,2,3])
print(lst)
lst.extend([1,2,3])
lst.extend([4,5,6])
# it requires a iterable it will iterate the list and add only the values to the list not the list
print(lst)