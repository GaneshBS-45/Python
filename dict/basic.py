details={
    "history":80,
    "science":60,
    "maths":65,
    "ENglish":75,
    "kannada":98
}
# print(details)

# d=(1,2,5,9,8,74)

# print(type(d))

for k in details:
    print(f"k = {k}, details={details[k]}")


for k,v in details.items():
    print(k,v)