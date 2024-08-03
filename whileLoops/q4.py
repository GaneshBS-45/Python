num1=int(input())
num2=int(input())

i=num1
j=num2
if i<j:
    while(i<=j):
        print(i,end=" ")
        i+=1
else:
    while(i>=j):
        print(j,end=" ")
        j+=1