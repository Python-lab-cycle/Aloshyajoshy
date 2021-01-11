#count the no of vowels,constants,digits and special characters

str=input("enter a string :")
vowels=constants=digits=specialcharacter=0
for char in str:
    if char in 'aeiouAEIOU':vowels+=1
    if char in 'bBcCdDeEfFgGHhiIjJkKlLmMnNoOPpQqrRSsTtUuVvWwXxYyZz':constants+=1
    if char in '0123456789':digits+=1
    if char in '!@#$%^&*<>?:;':specialcharacter+=1
    
       
print("the number of vowels=",vowels)
print("The number of constants=",constants)
print("The number of digits=",digits)
print("The number of specialcharacter=",specialcharacter)
       
