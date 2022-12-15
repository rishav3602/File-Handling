#tell , #seek

f = open("test2.txt")
print(f.read(5)) #read only five characters
print(f.tell()) #will tell the current position of the pointer.
print(f.read(10)) #it will read next 10 characters after the previous read function done
print(f.tell())
f.seek(1) #it will bring the pointer to the desired location.
print(f.read(2))
print(f.tell())
f.close()