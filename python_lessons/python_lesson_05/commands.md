==================================================================
The os module is a part of the Python standard library that provides a way to interact with the operating system. 

# Navigating and Managing Directories

import os

os.chdir('/path/to/directory')

os.mkdir('/path/to/new_directory')

# recursively directories creating:
os.makedirs(path, exist_ok=True)

os.rmdir('/path/to/directory_to_remove')

contents = os.listdir('/path/to/directory')
print(contents)

=====================================================================
Traversing Directories

# to iterate directory content:
import os
for foldername, subfolders, filenames in os.walk('/path/to/directory'):
    print('Current folder:', foldername)
    print('Subfolders:', subfolders)
    print('Filenames:', filenames)
    
# join path:    
os.path.join('test', 'file')
Output: 'test/file'

======================================================================
# Renaming and Removing Files/Directories

os.rename('old_name.txt', 'new_name.txt')

os.remove('/path/to/file_to_remove')

os.unlink('/path/to/file_to_remove')

os.rmdir('/path/to/directory_to_remove')

if os.path.exists('/path/to/check'):
    print("Path exists!")

if os.path.isdir('/path/to/directory'):
    print("It's a directory!")

size = os.path.getsize('/path/to/file')
print(f"File size: {size} bytes")

atime = os.path.getatime('/path/to/file')
print(f"Last access time: {atime}")

mtime = os.path.getmtime('/path/to/file')
print(f"Last modification time: {mtime}")

ctime = os.path.getctime('/path/to/file')
print(f"Creation time: {ctime}")

current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")
============================================================
# COPY MOVE REMOVE CHOWN
# The shutil module builds on the functionalities of the os module, providing additional high-level operations for file and directory management.

import shutil

# new file - 644
shutil.copyfile('source.txt', 'destination.txt') 

# save permissions
shutil.copy('source.txt', 'destination_copy.txt') 

# save metadates (time)
shutil.copy2('source.txt', 'destination_copy2.txt') 

shutil.move('source.txt', 'new_location/source.txt')

# рекурсивно копирует весь каталог, сохраняя метаданные (copytree использует copy2):
shutil.copytree('source_directory', 'destination_directory') 

shutil.rmtree('directory_to_remove')

shutil.chown('file_to_change_owner', user='new_owner', group='new_group')

---------------------------------------------------------------
import shutil
disk_usage = shutil.disk_usage('/')
print(f"Total: {disk_usage.total} bytes")
print(f"Used: {disk_usage.used} bytes")
print(f"Free: {disk_usage.free} bytes")
================================================================
# COMPARISON

# The filecmp module of fers functionalities for comparing files and directories, providing insights into similarities and differences between them.

import filecmp
result = filecmp.cmp('file1.txt', 'file2.txt')
print(f"Files are {'identical' if result else 'different'}.")

-------------------------------------------------------------------
import filecmp

# Example directories
dir1 = '/path/to/directory1'
dir2 = '/path/to/directory2'

# Create a directory comparison object
comparison = filecmp.dircmp(dir1, dir2)

# Access comparison results
print(f"Common files: {comparison.common}")
print(f"Files only in {dir1}: {comparison.left_only}")
print(f"Files only in {dir2}: {comparison.right_only}")
print(f"Differences between common files: {comparison.diff_files}")

# Optionally, print a comparison report
if report:
    comparison.report()

=====================================================================
# Walk with Customization

import os

def custom_walk(top, topdown=True, onerror=None, followlinks=False):
    # Custom logic here
    pass

for foldername, subfolders, filenames in custom_walk('/path/to/directory'):
    print('Current folder:', foldername)
    print('Subfolders:', subfolders)
    print('Filenames:', filenames)

-----------------------------------------------------------------------
# Error Handling in File Operations

import os

try:
    with open('nonexistent_file.txt', 'r') as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
    
---------------------------------------------------------------------------
