import re                        
num=input("Enter the number=")
res=re.search("^[0-9]{10}$",num)                    #[+]91[-]     
if res:
    print("Valid number")
    f=open("phonenumber.txt","a")
    f.write(num+"\n")
else:
    print("Invalid number")
