def replacing_all_spaces(s:str)->str:
    result=""
    for ch in s:
        if ch==" ":
            result+="-"
        else:
            result+=ch
    return result[:-1]

b=str(input())
print(replacing_all_spaces(b))