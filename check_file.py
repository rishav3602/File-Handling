f = open('poem.txt','r')
text = f.read()
if "twinkle" in text:
    print("Yes, the word twinkle is present in the file")
else:
    print("No, the word twinkle is not present in the file")
f.close()