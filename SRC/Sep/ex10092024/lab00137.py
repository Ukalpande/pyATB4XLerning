#try , except and finally
#file
#import os
import os

try:
    full_path = os.getcwd()
    print(full_path)
    file = open('example.txt','r')
    print(file.read())
except FileNotFoundError as fnfe:
    print("file not found, fix te path or create file ")
finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)