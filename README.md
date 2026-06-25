<h1>Directory sorter is a python script to sort stray files into folders.</h1>
You can add custom folders to config and specify what extensions should go into them. 
<h1>config guide</h1>  
{
        "folders":{   
            "folder1":["ext1","ext2"],  
            "folder2":["ext3","ext4"]  
        },  
        "dirsToClean":["/home/dir2/","/home/dir2/",/home/dir3/]  
    }  
---  
**folders** - this is where you put what folders should be created or in which folders files should go.  
**folder** - you put into square brackets **extensions** of files that should be moved into this folder    
**dirsToClean** - directories on which script should work  
        
