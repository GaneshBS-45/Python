st=int(input())
en=int(input())

i=st
j=en
total=0
while i<=j:
    if i%2==0:
        total=total+i
    i+=1

print(total)