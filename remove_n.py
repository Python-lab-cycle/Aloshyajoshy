str1=input("enter a string: ")
n=int (input("ener the index possition of the charactor to be removed: "))
first_part=str1[:n-1]
last_part=str1[n:]
print("the new string after removing the character=",(first_part + last_part))
