#remove char which has odd index

str1=input("enter a string:")
result=" "
for i in range(0,len(str1),2):
    result=result+str1[i]
print("string after removing character in odd positions:",result)    
