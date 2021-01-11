#a list of words and return the longest one

lis=input("enter a list with some string(space sepaated):")
words_list=lis.split()
word_len= []
for n in words_list:
    word_len.append((len(n),n))
word_len.sort()
print(word_len)
print("longest word",word_len[-1][1],"and length=",word_len[-1][0])
