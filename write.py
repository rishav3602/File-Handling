info = "Hello I am Rishav, I am learning data science from Ineuron"
det = "Hola , Beunos dias"

f = open("test4.txt", 'w')
f.write(info)
print("done")


with open("test5.txt",'w') as f:
    f.write(det)
    

try :
    with open ("test6.txt",'r') as f:
        f.write("Good Morning, Gaya")
except Exception:
    print("File open in read mode")

