def removing_all_alpha(s:str)->str:
    result=""
    for ch in s:
        if ord(ch)>=65 and ord(ch)<=90 or ord(ch)>=97 and ord(ch)<=122:
            result+=ch
    return result

b=str(input())

print(removing_all_alpha(b))