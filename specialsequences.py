# import re                        
# txt="apple is red"
# res=re.findall("\Aapple",txt)                     
# print(res)

# import re                        
# txt="apple is red"
# res=re.findall("red\Z",txt)                     
# print(res)

# import re                        
# txt="apple is red"
# res=re.findall(r"\bred",txt)                     
# print(res)


# import re                        
# txt="apple is red"
# res=re.findall("re\B",txt)                     
# print(res)



# import re                        
# txt="apple is red!!"
# res=re.findall("\w",txt)                     
# print(res)


# import re                        
# txt="apple is red!!"
# res=re.findall("\W",txt)                     
# print(res)

# import re                        
# txt="23 apple is red"
# res=re.findall("\d",txt)                     
# print(res)


# import re                        
# txt="apple is red!!"
# res=re.findall("\D",txt)                     
# print(res)

# import re                        
# txt="23 apple is red"
# res=re.findall("\s",txt)                     
# print(res)


import re                        
txt="23 apple is red"
res=re.findall("\S",txt)                     
print(res)