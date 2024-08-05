def replacing_allconsonents(s:str)->str:
    result=""
    for ch in s.lower():
        if ch not in "aeiou":
            result+="*"
        else:
            result+=ch
    return result
b=str(input())
print(replacing_allconsonents(b))