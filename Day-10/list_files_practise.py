import os

def list_folder(path):
    try:
        l= os.listdir(path)
        return l,None
    except FileNotFoundError:
        return None,"Directory does not exist" 
    except PermissionError:
        return None,"You don't have enough permission to list the folder"

path = input("Enter the path of directory seprated by spaces").split()

for i in path:
    list_of_files,Error = list_folder(i)
    if list_of_files:
        for j in list_of_files:
            print(j)
    elif Error:
        print(Error)
    
