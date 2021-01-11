#swap 1st 2 character of each string
str1=input("enter 1st srting: ")
str2=input("enter 2nd string: ")
new_a=str2[:2] + str1[:1]
new_b=str1[:2] + str2[:2]
print("the new string after swapping 1st 2 characters of both string: ",(new_a+' '+new_b))
