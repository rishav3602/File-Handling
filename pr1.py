try:
    a = int(input("Enter your number : "))
    b = int(input("Enter your number : "))
    c = a/b

except ArithmeticError as a:
    with open ("test7.txt",'w') as f :
        f.write("Your divison is not successful")
        print("divison by zero is not possible")
else:
    try:
        with open("test7.txt",'w') as f:
            f.write("Your divison is successful\n")
            f.write(str(c))
    except FileNotFoundError:
        print("File is not available")

