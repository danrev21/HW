


# Develop a script that reports the disk usage of each subdirectory within a given directory.

# Requirements:
# Traverse the specified directory and all subdirectories.
# Calculate the total size for each subdirectory.
# Identify and list the largest files.
# Output:
# Print a report of the total size of each subdirectory and the top 5 largest files in the entire directory tree.

# Tips:
# Use the os module to traverse directories.
# Calculate sizes using os.path.getsize.
# Consider using a priority queue or sorting for managing the largest files.