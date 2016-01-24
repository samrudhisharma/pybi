#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""
def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  file = open(filename, 'rU' )
  year_found = False ##var to prevent condition from being checked after result found
  name_dict = {}
  for line in file:
    match_year= re.search('Popularity in (\d\d\d\d)',line) 
    if match_year and year_found == False:
      year_print = match_year.group(1)  ## Milestone 1: Extract year 
      year_found = True
    ## Milestone 2: Extract names, rank numbers, print
    match_info = re.search("<tr align=\"right\"><td>(\d*)</td><td>(\w*)</td><td>(\w*)</td>", line)
    if match_info:
      ## Milestone 3: Get the names data into a dict, print 
      if match_info.group(2) not in name_dict.keys():
        name_dict[match_info.group(2)] = match_info.group(1)
      if match_info.group(3) not in name_dict.keys():
        name_dict[match_info.group(3)] = match_info.group(1)

  ranked_names = sorted(name_dict.keys())
  name_list = []
  name_list.append(year_print)
  for name in ranked_names:
    name_list.append(name + " " + name_dict[name])
  
  return name_list
  
def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  #print args[0]
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  for filename in args:
    names = extract_names(filename)

    # Make text out of the whole list
    text = '\n'.join(names) + '\n'

    if summary:
      outf = open(filename + '.summary', 'w')
      outf.write(text + '\n')
      outf.close()
    else:
      print text


if __name__ == '__main__':
  main()
