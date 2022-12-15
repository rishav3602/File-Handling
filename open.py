f = open("test.txt") # To open a file
print(type(f))
f.close() #To close the file


# another method to open a file.
try:
    f = open("test.txt")
    print(f.read())
finally:
    f.close()
