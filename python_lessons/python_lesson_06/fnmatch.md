# Fnmatch examples

import fnmatch

# getting all the files "*.py", "*.c": 
for file in all_files:
    if fnmatch.fnmatch(file, "*.py") or fnmatch.fnmatch(file, "*.c")
        all_c_py_files.append(file)

--------------------------------------------------------------       
import fnmatch
import os

# Example: Find all Python files in the current directory
python_files = [file for file in os.listdir('.') if fnmatch.fnmatch(file, '*.py')]
print('Python Files:', python_files)   

--------------------------------------------------------------     
# Example: Find all image files (jpg and png) in the current directory
image_files = [file for file in os.listdir('.') if fnmatch.fnmatch(file, '*.jpg') or fnmatch.fnmatch(file, '*.png')]
print('Image Files:', image_files)