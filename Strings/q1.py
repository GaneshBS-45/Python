def reversed_string(b:str)->str:
    rev_str=""
    for ch in b:
        rev_str=ch+rev_str 
    return rev_str

def rever_str(b:str)->str:
    return b[::-1]

c=str(input())
print(reversed_string(c))
print(rever_str(c))