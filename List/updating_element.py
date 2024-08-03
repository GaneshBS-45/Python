my_list=[1,2,4,5,56,6,6,7,5,3,4,3,578,5]

my_list[-1]=200

print(my_list)

n=len(my_list)

for i in range(n):
    if my_list[i]%2==0:
        my_list[i]=my_list[i]+1
    else:
         my_list[i]=my_list[i]-1


print(my_list)

a=5
print(id(a))
a=10
print(id(a))