n=int(input())
n2=int(input())
count=0
while n<=n2:
    if n%2==0:
        count=count+1
    n+=1

print(count)