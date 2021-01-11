#program to accept file name fromthe user print theextension of that.

filename=input("input the file name: ")
f_extens=filename.split(".")
print("the extension of file name is: ",f_extens[-1])
