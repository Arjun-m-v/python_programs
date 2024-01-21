flag=0
phonebook={}

while flag==0:
    op=input("1.Add\n2.View\n3.Delete\n4.Update\n5.Exit\nEnter the value=")
    if op=="1":
        name=input("Enter the name=")
        phone=input("Enter the number=")
        email=input("Enter the mail=")
        phonebook.update({name:{"name":name,"phone number=":phone,"email":email}})
    if op=="2":
        a=input("Enter name=")
        b=phonebook.get(a)
        print(b)
    if op=="3":
        a=input("Enter name=")
        b=phonebook.pop(a)
        print(phonebook)
    if op=="4":
        a=input("Enter name of which have to update=")  #update() name enter,which name phn mail?,then ise phnbuk to call nn thoninn
        b=phonebook.get(a)
        op=input("1.Name\n2.Number\n3.Mail\nEnter the thing=")
        if op=="1":
              c=input("Enter new name=")
              b.update({"name":c})
        if op=="2":
              c=input("Enter new Number=")
              b.update({"phone number":c})
        if op=="3":
              c=input("Enter new Mail=")
              b.update({"email":c})
        print(phonebook)
    if op=="5":
        flag=1








# a.update({"class":"BSc"})




# a=input("Enter name of which have to update=")
        # b=phonebook.get(a)
#         print("What you want to change")
#         op=input("1.Name\n2.Number\n3.Mail\nEnter the value=")
#         if op=="1":
#             name1=input("Enter new name=")
#             b.update({"name":name1})
#             print(phonebook)