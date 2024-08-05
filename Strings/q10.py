def removing_duplicate(s:str)->str:
    result=""
    for ch in s:
        if ch  not in result:
            result+=ch

b=str(input())
print(removing_duplicate(b))