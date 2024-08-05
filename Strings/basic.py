a= "anirudh"
print(a)
print(type(a))
# a[0]=z we cannot change the value it is  strings are immutable

# iteration
# by index
for i in range(len(a)):
    print(a[i],end=" ")
    print()

# by value
for i in a:
    print(i,end=" ")

print(a.find("n"))
