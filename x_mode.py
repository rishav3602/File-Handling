try:
    with open ("new.txt",'x') as f:
        pass
except FileExistsError:
    with open ("new.txt",'w') as f:
        f.write("File already exist")
        print("File already exist")