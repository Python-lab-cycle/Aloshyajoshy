#area perimeter on rectangle,circle,cuboid,phere packages

from graphics.circleAPFunction import *
from graphics.rectangleAPFunction import *
from graphics.Dgraphics.cuboidAPFunction import *
from graphics.Dgraphics.sphereAPFunction import *

#area and perimeter of rectangle
l=int(input("Enter the lenght: "))
w=int(input("Enter the width: "))
print("Area of the Rctangle is = ",RArea(w,l))
print("Perimeter of Rectangle is = ",Rperimeter(w,l))


#area and perimeter of circle 
r=int(input("Enter the radius of the circle:"))
print("Area of a circle is = ", CArea(r))
print("Perimeter of circle is = ",CPerimetr(r))


#area and perimeter of cuboid
a=int(input("enter the  edge: "))
l=int(input("enter the length: "))
b=int(input("enter the breadth: "))
h=int(input("enter the height: "))
print("area of cuboid is : ", Acuboid(a))
print("perimetr of cubiod is : ",Pcuboid(l,b,h))


#area and perimeter of sphere
r=int(input("enter the radius: "))
print("Areaof a sphere is = ",Asphere(r))
print("Perimeter of a shpere is = ",Psphere(r))



      



