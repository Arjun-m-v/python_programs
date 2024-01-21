# # ----------Read-----------

# f=open("randomlibrary.py")
# # print(f.read())

# print(f.readline())
# # print(f.readlines())


# # ----------Write---------

# f=open("alan.txt","w")
# f.write("Computer science")

# f=open("alan.txt","w")
# list=["apple","is","red"]
# f.writelines(list)

# #----------Append----------
# f=open("alan.txt","a")
# f.write("Computer science")
# list=["apple","is","red"]

# #----------Create----------
# f=open("alan1.txt","x")
# f.write("Computer science")


#----------Read after Write----------
f=open("alan.txt","w")
f.write("Computer science")
f.close()
f=open("alan.txt")
f.read()
