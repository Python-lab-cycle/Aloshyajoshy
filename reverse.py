#accept the name and print them in reverse order

name=input("enter your name: ")
l=name.split()
l.reverse()
print("Reversed name:",end=' ')
for i in l:
    print(i,end=' ')
    
