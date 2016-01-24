#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
""" 
Milestones:
1 fetch filenames in given directory
2 use regex find special file names
3 create abs path for the special file
4 return list of special file abs paths
5 given a list of paths, copy into given directory  
    create dir if not exists
6 Create a zip file
7 Print app. cmd msg
"""
def get_special_paths(dir): 
#return a list of abs paths of the special files in the given directory
  filenames = os.listdir(dir)
  list_special_files = []
  for filename in filenames:
    match_special_files = re.search(r'__\w+__', filename) 
    if match_special_files:
      path = os.path.join(dir, filename)
      list_special_files.append(os.path.abspath(path))
  
  return list_special_files
  
def copy_to(files, dir):
# given a list of paths, copies those files into the given directory  
  if os.path.exists(dir) == False : #make dir
    os.mkdir(dir)
    
  for file in files:
    file_name = os.path.basename(file) #strip the abs path from file
    #print file_name
    shutil.copy(file, os.path.join(dir, file_name))
   
def zip_to(files, zippath):
#given a list of paths, zip those files up into the given zipfile
  cmd = "zip -j "+ zippath + " " +" ".join(files) #spaces necessary
  print "Command I'm going to do: ", cmd
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    print sys.stderr.write(output)
    sys.exit(1)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  files = []
  for filename in args:
    files.extend(get_special_paths(filename))
   
  if todir:
    copy_to(files, todir)
  elif tozip:
    zip_to(files, tozip)
  else:
    text = '\n'.join(files)
    print text
  
  
if __name__ == "__main__":
  main()
