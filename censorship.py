with open ('sample.txt') as f :
    content = f.read()

words = ['monkey','donkey','kutta','motka','pagal']

for word in words:
    content = content.replace(word,"#@$&^")

with open('sample.txt','w') as f :
    f.write(content)