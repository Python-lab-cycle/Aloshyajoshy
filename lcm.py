#LCM of 2 positive integers
x=int(input("enter first positive integers:"))
y=int(input("enter 2nd positive integers:"))
if x>y:
    z=x
else:
    z=y
while(True):
    if((z % x == 0) and (z % y == 0)):
        Lcm = z
        break
    z += 1
print("LCM of" ,x,"and",y,"is", Lcm)
