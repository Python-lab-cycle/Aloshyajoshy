#all the occurence of first char have been changed to $ except the first char itself.

str1=input(" enter a sring: ")
print("orginal string: ",str1)
char=str1[0]
str1=str1.replace(char,'$')
str1=char+str1[1:]
print("replaced string:",str1)
