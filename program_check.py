with open('log.txt') as f:
    content = f.read()

if "python" in content.lower():
    print("Yes, its a python related file.")

else:
    print("No, its not a python related file.")