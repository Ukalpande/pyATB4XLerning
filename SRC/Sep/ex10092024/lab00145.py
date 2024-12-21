
file = open("ujwal.txt", "r")
content = file.read()
print(content)



import os

full_path_file = os.path.join("/Users/Admin/PycharmProjects/pyATB4XLerning/SRC/Sep/example","ujwal2.txt")
file = open(full_path_file, 'r')
content = file.read()
print(content)
