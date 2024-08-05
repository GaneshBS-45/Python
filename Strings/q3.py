def remove_vowels(a:str)->str:
    consonents=""
    for i in a.lower():
        if i not in "aeiou":
            consonents+=i
    return consonents


b=str(input())

print(remove_vowels(b))