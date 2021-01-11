#first and last character to be exchanged

str1=(input("enter a string:"))
print("print after swapping 1st and last character:",(str1[-1:]+str1[1:-1]+str1[:1]))
