a=int(input("Enter a number="))
flag=0
for i in range(2,a):
    if a%i==0:
        flag=1
if flag==0:
    print("The number is prime number")
else:
    print("The number is not prime")