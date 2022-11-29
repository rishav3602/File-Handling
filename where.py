content = True
i = 1

with open('log.txt') as f:
    while content:
        content = f.readline()

        if "python" in content.lower():
            print(content)
            print("Yes, its a python related file.")
            print(i)
        i = i + 1

