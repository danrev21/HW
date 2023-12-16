#!/usr/bin/env python

import os

path = "/home/dan/Workdir/it_station_lab/HW/python_lessons/python_lesson_05/test"

def enumeratepaths(path=path):
  '''Returns the path to all files in a directory as a list'''
  path_collection = []
  for dirpath, dirnames, filenames in os.walk(path):
    for file in filenames:
      fullpath = os.path.join(dirpath, file)
      path_collection.append(fullpath)
  return path_collection

def enumeratefiles(path=path):
  '''Returns the names of all files in a directory as a list'''
  file_collection = []
  for dirpath, dirnames, filenames in os.walk(path):
    for file in filenames:
      file_collection.append(file)
  return file_collection

def enumeratedir(path=path):
  '''Returns the names of all subdirectories in a directory as a list'''
  dir_collection = []
  for dirpath, dirnames, filenames in os.walk(path):
    for dir in dirnames:
      dir_collection.append(dir)
  return dir_collection

if __name__ == "__main__":

  print("Recursive listing of all paths in a dir:")
  for path in enumeratepaths():
    print(path)

  print("Recursive listing of all files in dir:")
  for file in enumeratefiles():
    print(file)

  print("Recursive listing of all dirs in dir:")
  for dir in enumeratedir():
    print(dir)