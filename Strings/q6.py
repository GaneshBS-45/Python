def s_captialise(s:str)->str:
    return s.title()
def s_capitalise2(s:str)->str:
    result = ""
    is_new_word = True
    for char in s:
        print(f"charc is for condition = {char}")
        if is_new_word and "a"<=char<="z":
            print(f"the char inside if condition = {char}")
            result+=chr(ord(char)-32)
            is_new_word=False
        else:
            result+=char
        if char==" ":
            is_new_word=True      
    return result
    

b=str(input())
print(s_capitalise2(b))
print(s_captialise(b))