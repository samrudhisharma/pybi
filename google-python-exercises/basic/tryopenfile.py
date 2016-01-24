import sys
## Remember most control available through variable names, use wisely. 
def Cat(filename):
  f = open (filename, 'rU')
  #for line in f:
    #print line,
  #lines = f.readlines()
  text = f.read()  
  print text,
  f.close()
 
def main():
  print sys.argv[1]
  Cat(sys.argv[1])
  
if __name__ == '__main__':
  main()
