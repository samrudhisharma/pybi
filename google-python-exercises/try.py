import os
import sys
import commands

def getCurrenDir(cd):
  #cd = os.getcwd()
  cmd = "ls -l "+ cd
  return
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write("there was an error" + output)
    sys.exit(1)
    
  print output
  
  """filenames = os.listdir(cd)
  for filename in filenames:
    path = os.path.join(cd, filename)
    print path
    print os.path.abspath(path)"""

def main():
  getCurrenDir(sys.argv[1]) #python try.py . 

if __name__ == '__main__':
  main()
