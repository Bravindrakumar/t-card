import sys
import json
import os

def main():
  if len(sys.argv) !=2:
    print("Path to file containing modified paths is required.")
    exit(1)
  
  # compile the list of modified files into unique set of root directories
  b = []
  exclude = set(['ab', 'zx'])
  
  for dname, dirs, files in os.walk('b'):
    dirs[:] = [d for d in dirs if d not in exclude]
    b.append({"env": dname})
    
  includeMatrix = { "include": b }
  print(json.dumps(includeMatrix))
  
  
  
if __name__ == "__main__":
  main()
