def counting_digits(s:str)->int:
    count=0
    for ch in s:
        if ord(ch)>=48 and ord(ch)<=57:
            count+=1
    return count

b=str(input())

print(counting_digits(b))

