import os
import json
import shutil

data = json.load(open('dirs.json', 'r'))
print(os.getcwd())


    
for key,value in data.items():

    if key == "folders":
        folders = []
        for f in value:
            folders.append(f)
        def folderCreation():
            for folder in folders:
                if not os.path.exists(folder):
                    os.makedirs(folder)
                    print(f"folder: {folder} created")
        def folderCleanup():
            cwd = os.getcwd()
            for file in os.listdir(cwd):
                filename,fileExt = os.path.splitext(file)
                print(f"{file} has extention: {fileExt}") 
                for foldername, extentions in data["folders"].items():
                    if fileExt in extentions:
                        file_path = os.path.join(cwd, file)
                        target_dir = os.path.join(cwd, foldername)
                        shutil.move(file_path, os.path.join(target_dir, file))
                        print(f"{file} moved to {foldername}")

    if key == "dirsToClean":
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
