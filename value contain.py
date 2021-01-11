#a spacified value contained in the group

lis=input("enter a list(values  space separated):")
n=int(input("enter the number to be searched:"))
lis1=list(map(int,lis.split()))
print(lis1)
k=len(lis1)
for value in lis1:
    if n==value:
        print("the number",n,"is found in the list")
        break
    else:
     print("the number",n,"is not fount in the list")
