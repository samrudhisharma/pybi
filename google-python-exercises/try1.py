import sys
import os 

print "Hello :)"

def Cat(filename):
  try:
    f = open(filename)
    text = f.read()
    print '----', filename
    print text
  except IOError:
    print "No such file found: ", filename

# Define a main() function that prints a little greeting.
def main():
  args = sys.argv[1:]
  for arg in args:
    Cat(arg)
    
#This is the standard boilerplate that calss the main() function.
if __name__ == '__main__':
  main()
