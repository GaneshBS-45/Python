def counting_numbers(a:str)->int:
    return len(a.split())

def counting_numbers2(a:str)->int:
    if not a:
        return 0
    count=0
    current=""
    for ch in a:
        if ch==" ":
            count+=1
            current=""
        else:
            current+=ch
    return count
    

b=str(input())
print(counting_numbers(b))
print(counting_numbers2(b))