try:
    with open("error.txt") as f:
        print(f.read())
except FileNotFoundError:
    with open("error.txt",'w+') as f:
        f.write("this is my error file")
        print(f.read())
else:
    print("Read")
        

