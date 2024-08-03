lst=[4,5,4,5,7,6,7,6,4 ]
def frequency(my_list:list)->dict:
    my_dict={}
    for num in my_list:
        my_dict[num]=my_dict.get(num,0)+1
    print(my_dict)
    max=0
    maxfrequency=0
    for i in my_dict:
        print(i)
        if my_dict[i]>max:
            maxfrequency=i
            max=my_dict[i]

    return maxfrequency,max

# a=list(input())
print(frequency(lst))