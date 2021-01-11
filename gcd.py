#GCD of 2 numbers

a=int(input("enter first number:"))
b=int(input("enter 2nd number: "))
for i in range(1,min(a,b)+1):
    if(a%i==0 and b%i==0):
        GCD=i
print("GCD of ",a,"and",b,"is",GCD)
