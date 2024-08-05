def verifyalphanum(s:str)->bool:
    return s.isalnum()

def verifyalphanum2(s:str)->bool:
    alphanum=False
    for ch in s:
        if ord(ch)<=65 and ord(ch)>=90 and ord(ch)<=97 and ord(ch)<=122 or ord(ch)<=48 and ord(ch)<=57:
            alphanum=True
        else:
            alphanum=False
            break
    return alphanum

c=str(input())
print(verifyalphanum(c))
print(verifyalphanum2(c))
