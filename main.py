import os
import json

data = json.load(open('dirs.json', 'r'))
#print(data)
print(os.getcwd())
def folderCreation():
    folders = ["photos","videos","pdfs","textfiles"]
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"folder: {folder} created")
def folderCleanup():
    cwd = os.getcwd()
    for file in os.listdir(cwd):
        filename,fileExt = os.path.splitext(file)
        print(f"{file} has extention: {fileExt}") #ostatni update
for key,value in data.items():
    for e in value:
        print(e)
        while True:
            try:
                os.chdir(e)
                folderCreation()
                folderCleanup()
                break
            except OSError as error:
                print(error)
                print("this directory does not exist")
                break
