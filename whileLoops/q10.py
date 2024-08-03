st=int(input())
en=int(input())

i=st
j=en
count=0

count1=0
while i<=j:
    if i%7==0:
        count=count+1
    if i%7==0 and i%2==0:
        count1=count1+1
    i+=1
print(count,count1)