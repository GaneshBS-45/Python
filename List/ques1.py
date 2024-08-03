my_list=[1,2,3,4,5,6,7]
total=0
n=len(my_list)
for i in range(n):
    if my_list[i]%2==0:
        total+=my_list[i]

total1=0

for num in my_list:
    if num%2==0:
        total1+=num

total2=0

for i in range(n):
    if i%2==0:
        total2+=my_list[i]
print(f"{total} {total1} {total2}")