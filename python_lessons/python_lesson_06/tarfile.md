# Tarfile examples

Core Methods:
The tar module offers several core methods for creating and extracting tar archives:
- add Method: The add method is used to add files or directories to a tar archive.
- list Method: The list method displays the contents of a tar archive.
- name Attribute: The name attribute is used to set or retrieve the name of the tar archive.
- Compression Methods: The tar module supports various compression formats, including bzip2 and gzip, enhancing the efficiency of tar archives.

-----------------------------------------------------------
import tarfile

-----------------------------------------------------------
# Example: Create a tar archive and add files
with tarfile.open('example.tar', 'w') as tar:
    tar.add('file1.txt')
    tar.add('file2.txt')

----------------------------------------------------------
# creating tar archive with only 'txt' files:
with tarfile.open("test.tar", "w") as tar_file:
    txt_files = glob.glob("./**/*.txt", recursive = True)
    for file in txt_files:
        tar_file.add(file)
        
tar_file = tarfile.open("test.tar", "r")        
tar_file.list()       
# output: 
?rw-rw-r-- dan/dan         13 2023-12-22 22:30:53 ./test1.txt 
?rw-rw-r-- dan/dan         31 2023-12-22 22:31:15 ./test2.txt         

----------------------------------------------------------       
# create directory and extract in it:
tar_file.extractall("./tmp_txt")

# return name:
tar_file.name
Output: 
'/home/dan/test.tar'   

-----------------------------------------------------------
# Example: List the contents of a tar archive
with tarfile.open('example.tar', 'r') as tar:
    print('Contents of example.tar:', tar.getnames())
    
-----------------------------------------------------------
# Example: Extract all contents of a tar archive
with tarfile.open('example.tar', 'r') as tar:
    tar.extractall()        
        
        
     