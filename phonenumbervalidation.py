import re                        
num=input("Enter the number=")
res=re.search("^[+]91[-][0-9]{10}$",num)                      
if res:
    print("Valid number")
else:
    print("Invalid number")