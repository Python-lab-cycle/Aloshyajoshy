line="python programing is fun"
f1=open("text1.txt","w")
f1.write(line)
f1.close()
f1=open("text1.txt","r")
line=f1.read()
print("line",line)
f1.close()
