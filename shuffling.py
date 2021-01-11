#prgm to shuffle andprint a specified list

import random
color=input("enter a list(seperated by commas):")
listcolor=list(color.split())
random.shuffle(listcolor)
print("list after shuffling:",end=' ')
print(listcolor)
