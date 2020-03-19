import os 
import shutil 

# Write the name of the directory 
# that needs sorted here:
path = "C:\\Users\\xxx\\Downloads"


# This will create a properly organized 
# list with all the filenames that are 
# in the path directory 
list_ = os.listdir(path) 

# This will go through each and every file 
for file_ in list_: 
    name, ext = os.path.splitext(file_) 

	# This will store the extension type 
    ext = ext[1:] 

	# This forces the next iteration, 
	# if it is the directory 
    if ext == "": continue

	# This will move the file to the directory 
	# where the name 'ext' already exists 
    if os.path.exists(path+"/"+ext): 
        shutil.move(path+"/"+file_, path+"/"+ext+"/"+file_)
        # If ext folder does not exist, a folder is created
    else:
        os.makedirs(path+"/"+ext) 
        shutil.move(path+"/"+file_, path+"/"+ext+"/"+file_) 
