#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
"""
Milestone:
-  read log file Done
- extract puzzle urls, find all the "puzzle" path urls Done 
- combine path from each url with the server name to form full url Done
- screen out urls that appear more than once (rem dup) Done
- return -> list of full urls, sorted in alphabetical order, and without duplicates Done
- simplest case: main() should just print the urls, one per line Done
- 
"""
# uf = urllib.urlopen("http://google.com")
# uf.read()
# urllib.urlretrieve(),  'name.extension' <- download 

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  
  puzzle_url = [] #list of final urls
  dict_final_urls = {} #dict of urls as keys
  
  head, url_append = filename.split("_") #extracting server name
  file_contents = open (filename, 'rU')
  for file_line in file_contents:
    match_puzzle_url = re.search(r'GET\s(\S*puzzle\S*)\s', file_line)
    if match_puzzle_url:
      final_url = "http://"+url_append+match_puzzle_url.group(1)
      puzzle_url.append(final_url)
  
  place_type = False
  for final_url in puzzle_url:
    check_url_type = re.search(r"-(\w+)-(\w+).jpg", final_url)
    if check_url_type: #do custom sort
      place_type = True
      break
  
  #use a list to remove duplicates from a list
  set1  = set(puzzle_url)
  result = list(set1) #convert back to a list  
  
  if place_type == False:
    puzzle_url = sorted(result) #sorted the list
  else:
    result.sort(key = myKeyString2)
    puzzle_url = result

  return puzzle_url

def myKeyString2(sumString): #used to get the key to unscramble picture
  check_url_type = re.search(r"-(\w+)-(\w+).jpg", sumString)
  return check_url_type.group(2)
  
"""
Milestones:
- use puzzle_url, download the image in given directory (create dir if not present) Done
- give local filenames Done
- create an index.html file Done
- write images to the image file Done
"""
def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  if os.path.exists(dest_dir) == False : # create a dir if it does not exist
    os.mkdir(dest_dir)
    
  index = file(os.path.join(dest_dir, 'index.html'), 'w')
  index.write('<html><body>')
  
  count  = 0
  for img_url in img_urls:
    url_name = 'img%d'%count
    urllib.urlretrieve(img_url, os.path.join(dest_dir, url_name))
    print "Retrieving file " + img_url
    index.write('<img src="%s">' % (url_name,))
    count+=1
   
  index.write('</body></html>')

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])
  
  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
