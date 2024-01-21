# a="1234"
# 1.it must be 4 or 6 digis
# 2.alphabet must not be allowed
# 3.even numbers must not allowed

a=input("Enter pin=")
# # b=a.isdigit()
# # c=0
# # d=0
# # for i in a:
# #     c+=1
# # if c==4 or c==6:
# #     if b=!True:
# #        print("Valid number") 
# #     elif b==False:
# #         print("Invalid pin")
# # else:
# #     print("Invalid pin")

# d=0
# for i in a:
#     if i%2==1:
#         d+=1
#     else:
#         ("Invalid number")
# if d==4 or d==6:
#     print("Valid number")






for i in a:
    if i.isalpha():
        print("Not valid")
        break
else:
    if len(a)==4 or len(a)==6:
        for i in a:
            if int(i)%2==0:
                print("Not valid")
                break
        else:
            print("Valid")
    else:
        print("Valid")