file1=open("Myfile1.txt","w")
L=["This is a right choice"]
file1.write("Hello   ")
file1.writelines(L)
file1.close()
file1=open("Myfile1.txt","r+")
print("Output of read:")
print(file1.read())
file1.close()
#hello

