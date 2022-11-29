with open('sample.txt' , 'r') as f :
    a = f.read()
with open('sample.txt' , 'w') as f :
    a = f.write("me")
print(a)