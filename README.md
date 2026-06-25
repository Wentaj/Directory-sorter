# Directory sorter

Directory sorter is a Python script that sorts stray files into folders.

You can add custom folders to the config and specify which file extensions should go into them.

## Config guide

```json
{
	"folders": {
		"folder1": [
			"ext1",
			"ext2"
		],
		"folder2": [
			"ext3",
			"ext4"
		]
	},
	"dirsToClean": [
		"/home/dir1/",
		"/home/dir2/",
		"/home/dir3/"
	]
}
```

***

- **folders** — defines which folders should be created or used and which file extensions belong in each folder.
- **folder name** — inside each folder entry, put the file extensions in square brackets for files that should be moved there.
- **dirsToClean** — directories on which script should work.
