# # ----------Search(To search a character)----------
# import re
# a="apple is red"
# res=re.search("is",a)
# print(res)

# # ----------To find from a first letter to a last letter----------
# import re
# a="apple is red impossible"
# res=re.search("i.*s",a)
# print(res)

# # ----------to find by start char to end char----------
# import re
# a="apple is red impossible"
# res=re.search("^a.*impossible$",a)
# print(res)

# # ----------Split(To find a character)----------
# import re
# a="apple is red impossible"
# res=re.findall("i",a)
# print(res)

# # ----------Split(to split string)----------
# import re
# a="apple is red impossible"
# res=re.split("i",a)
# print(res)

# # ----------Finditer : to find characters(if multiple )---------
# import re
# a="apple is red impossible"
# res=re.finditer("i",a)
# for i in res:
#     print(i.start())
#     print(i.group())
#     print(i)






# # ----------Check a password valid by checking it contains 123----------
# import re
# username=input("Enter the user name=")
# password=input("Enter the password=")
# res=re.search("123",password)
# if res:
#     print("Valid password")
# else:
#     print("Invalid passwordD")

# # ----------Check a password valid by checking it contains any one character from ABCD----------
# import re
# username=input("Enter the user name=")
# password=input("Enter the password=")
# res=re.search("[ABCD]",password)                      #Here from ABCD only one charceter is needed to make it valid cause of[]
# if res:
#     print("Valid password")
# else:
#     print("Invalid password")


# # ----------Check a password valid by checking it start with any one character from ABCD----------
# import re
# username=input("Enter the user name=")
# password=input("Enter the password=")
# res=re.search("^[ABCD]",password)                       #valid only by starting with A or B or C or D
# if res:
#     print("Valid password")
# else:
#     print("Invalid password")

#                                                     # ----------Check a password valid by checking it only not  with any one character from ABCD----------
#                                                     import re
#                                                     username=input("Enter the user name=")
#                                                     password=input("Enter the password=")
#                                                     res=re.search("[^ABCD]",password)                       #valid only by not starting with A or B or C or D
#                                                     if res:
#                                                         print("Valid password")
#                                                     else:
#                                                         print("Invalid password")

# import re
# password=input("Enter the password=")
# res=re.search("^a0?e$",password)                      #? is used to check the prefix character zero or one times...
# if res:
#     print("Valid password")
# else:
#     print("Invalid password")


# import re
# password=input("Enter the password=")
# res=re.search("^a[0-9]{3}e$",password)                      #{} is used to put a limit...
# if res:
#     print("Valid password")
# else:
#     print("Invalid password")


# import re
# password=input("Enter the password=")
# res=re.search("^a[0-9]{3,}e$",password)                      #{} is used to put a limit and comma denotes minimum...
# if res:
#     print("Valid password")
# else:
#     print("Invalid password")



#----------[  Email Validation  ]----------
import re                        
mail=input("Enter the mail=")
res=re.search("^[a-z0-9._-]+[@][a-z]+[.][a-z]{2,3}$",mail)                      
if res:
    print("Valid password")
else:
    print("Invalid password")


    #special sequences