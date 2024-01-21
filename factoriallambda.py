x=lambda n:1 if n==1 else n*x(n-1)
print(x(4))