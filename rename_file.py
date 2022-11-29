import os

old_filename = "sample2.txt"
new_filename = "renamed_by_python.txt"

with open (old_filename) as f:
    content = f.read()

with open (new_filename,'w') as f :
    f.write(content)

os.remove(old_filename)