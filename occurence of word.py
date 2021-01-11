#convert the occurence of ech word in a given sentence

str1=input("enter a string")
counts={}
words=str1.split()
for word in words:
    if word in counts:
        counts[word]+=1
    else:
        counts[word]=1
for k,v in counts.items():
    print(k,v)
        
