with open('this.txt') as f :
    text1 = f.read()

with open ('poem.txt') as f :
     text2 = f.read()

if text1 == text2:
    print("Yes, both files have same content")
else:
    print("No, both files have do not same content")