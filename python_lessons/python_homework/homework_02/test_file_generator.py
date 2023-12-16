#!/usr/bin/env python

# script creates the file with defined phrase 
# and number of repitions this phrase
# ./test_file_generator.py test.txt 'Phrase to write to file' 2000
 
import sys

filename = sys.argv[1]
phrase = sys.argv[2]
number = int(sys.argv[3])

for i in range(0, number):
        with open(filename, 'a') as file:
            file.writelines(f"{phrase}\n")
        file.close()


