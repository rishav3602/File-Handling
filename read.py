f = open("test.txt")
print(f.read()) #this will read the whole content of the file 
print(f.read()) #This will try to read from where the previous read function stopped to read.
f.close()
#print(f.read())  #can't read a file after the file is closed. 
