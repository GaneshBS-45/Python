s=["history","scrince","maths","eng"]
m=[42,78,64,98]
def ass(a:list,b:list)->dict:
    my_dict={}
    
    for i in range(len(a)):
        my_dict[a[i]]=b[i]
    return my_dict

print(ass(s,m))