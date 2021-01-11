#FACTORIAL OF A NUMBER

a=int(input("enter the number:"))
fact=1
for i in range(1,a+1):
    fact=fact*i
print("Factoril of",a,"is",fact)
