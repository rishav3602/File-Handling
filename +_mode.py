try :
    with open("new2.txt",'w+') as f :
        print(f.read())
        f.write("This is my update")
        print(f.read())
except:
    print("something went wrong please try again")