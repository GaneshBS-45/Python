def counting_longest(a:str)->str:
    longest=""
    current=""
    for ch in a:
        if ch==" ":
            if len(current)>len(longest):
                longest=current
                current=""
        else:
            current+=ch
    if len(current)>len(longest):
        longest=current
    return longest

b=str(input())

print(counting_longest(b))