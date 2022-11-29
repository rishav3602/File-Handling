with open('this.txt') as f :
    content = f.read()

with open ('copy.text','w') as f :
    f.write(content)