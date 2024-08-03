def q1(n:int)->dict:
    my_dict={}
    for i in range(n):
        a=input("Enter your sunject name ")
        b=(input("Enter the subject marks "))
        my_dict[a]=b
    return my_dict
m=int(input("Enter the number of subjects "))
print(q1(m))

