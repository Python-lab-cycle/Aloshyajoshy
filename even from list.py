#print all evn no's from a given no's listin the sameorder and stop the printing if any no that comeafter 237 in a sequence

lis=input("enter a list(space separated):")
lis1=list(map(int,lis.split()))
print(lis1)
print("Even number upto 237")
for x in lis1:
    if x==237:
        break
    elif x%2==0:
        print(x, end=' ')
