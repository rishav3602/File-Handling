with open("test3.txt") as f:
    print(f.read())

try:
    with open ("test4.txt") as f:
        print(f.read())

except FileNotFoundError:
    print("sorry this file is not found")
    print("Please try a available file name. ")
