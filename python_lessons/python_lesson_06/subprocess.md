# The subprocess module in Python provides a way to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. This module is essential for interacting with the underlying operating system, executing external commands, and managing external processes.

----------------------------------------------------------------------
import subprocess

----------------------------------------------------------------------
# using the call method (depricated)
subprocess.call(['ls', '-l'])

----------------------------------------------------------------------
# using the run method, аналог call метода, но богаче функционал:
subprocess.run("ls", shell = True)
# or:
subprocess.run(["ls"])

----------------------------------------------------------------------
# PIPE - запись stdout в память
# text = True  - преобразование result.stdout из bytes в string
result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE, text=True)
print('Return Code:', result.returncode)  
# output: Return Code: 0
print('Output:', result.stdout)
# output:
Output: total 24
-rwxrwxr-x 1 dan dan   448 Dec 22 19:41 file1.txt
-rw-rw-r-- 1 dan dan   773 Dec 23 16:49 file2.txt

# one more example of run method
# listing detailed information about the /dev/null file:
result = subprocess.run(["ls", "-l", "/dev/null"], capture_output=True)
print('Output:', result.stdout)
Output: b'crw-rw-rw- 1 root root 1, 3 Dec 23 14:02 /dev/null\n'
 print('Output:', result.stderr)
Output: b''

----------------------------------------------------------------------
# to write stdout in file:
with open("test3.txt", "w") as file:
    subprocess.run(["ls", "-lah"], stdout = file)

with open("./src/documents/report.txt", "w") as file:
    subprocess.run("journalctl -xe | tail", shell = True, stdout = file)    
    
----------------------------------------------------------------------
# to write stdout in /dev/null:
subprocess.run(["ls"], stdout = subprocess.DEVNULL)

----------------------------------------------------------------------
# using the Popen method
# Popen можно использовать для параллельного запуска процессов с помощью метода poll(), например:
a = subprocess.Popen("sleep 60 && ls", shell = True)
while a.poll() !=0:
    print("111")
# здесь будет выводится "111" пока не выполнится команда "sleep 60 && ls"

-----------------------------------------------------------------------
# 
process = subprocess.Popen(['echo', 'Hello, subprocess!'], stdout=subprocess.PIPE)
output, error = process.communicate()
print('Output:', output.decode())

----------------------------------------------------------------------
## Practical Examples:
Running a Python Script:

import subprocess

# Example: Running a Python script
script_path = 'myscript.py'
subprocess.call(['python', script_path])
Redirecting Output:

----------------------------------------------------------------------
import subprocess

# Example: Redirecting output to a file
with open('output.txt', 'w') as f:
    subprocess.call(['ls', '-l'], stdout=f)
Handling Errors:

----------------------------------------------------------------------
import subprocess

# Example: Handling errors gracefully
try:
    subprocess.check_call(['nonexistent_command'])
except subprocess.CalledProcessError as e:
    print(f'Error: {e}')
- Core Methods:
The subprocess module offers several key methods for working with external processes.

----------------------------------------------------------------------
Popen Method: The Popen method provides more flexibility. It allows for more advanced interaction with the process, such as reading from or writing to its input/output streams.

import subprocess

# Example: Using the Popen method
process = subprocess.Popen(['echo', 'Hello, subprocess!'], stdout=subprocess.PIPE)
output, error = process.communicate()
print('Output:', output.decode())
check_call Method: The check_call method is similar to run but raises a CalledProcessError if the command returns a non-zero exit code, allowing for more robust error handling.

----------------------------------------------------------------------
import subprocess

# Example: Using the check_call method
subprocess.check_call(['ls', '-l'])
check_output Method: The check_output method captures the standard output of a command as a byte string. Like run, it raises a CalledProcessError for non-zero exit codes.

----------------------------------------------------------------------
import subprocess

# Example: Using the check_output method
output = subprocess.check_output(['ls', '-l'])
print('Output:', output.decode())

----------------------------------------------------------------------
- subprocess.PIPE: This constant is used to create a pipe to the standard input/output/error of the process, allowing interaction with those streams.
- subprocess.DEVNULL: This constant is used to indicate that the corresponding standard stream should be redirected to the system's null device, effectively discarding the output.
- subprocess.STDOUT: This constant is used to redirect the standard error stream to the same location as the standard output stream.