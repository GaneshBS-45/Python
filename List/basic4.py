my_list=[23,45,675,98,49,9859,235,2,432,213,3352,4224]

print(my_list[0])

n=len(my_list)
# iterate by index 
for i in range(n):
    print(my_list[i],end=" ")

# reverse print index n to -1
for i in range(n-1,-1,-1):
     print(my_list[i])
# Iterate by value
for i in my_list:
    print(i,end=" ")


    

