try:
    with open("new3.txt",'a') as f :
        f.write("This is my append file") #it will keep on adding this line if we keep on 
                                          # running this code again again.
except:
    pass