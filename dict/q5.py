my_string="ahghdlzdfajlknaaaakdsjamafk"

my_dict={}

for key in my_string:
    max=0
    max_cout=0
    min=max
    min_count=0
    my_dict[key]=my_dict.get(key,0)+1
for key,value in my_dict.items():
    if value>max:
        max=value
        max_cout=key
    elif value<min:
        min=value
        min_count=key

print(f"max ={max_cout} {max} , min={min_count}{min}")
print(my_dict)
