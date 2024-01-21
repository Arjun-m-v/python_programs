word="apple is res"
# b=["a","e","i","o","u"]
c=0
for i in word:
    if i in "aeiou":    # if i in b:
        c+=1
print(c)