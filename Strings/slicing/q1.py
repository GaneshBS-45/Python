my_string="Python is coding Language"

words=my_string.split()
# words.reverse()

words=words[::-1]
print(words)
print(" ".join(word for word in words))