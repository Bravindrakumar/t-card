import sys
import json
import os

def main():
  if len(sys.argv) < 2:
    print("Path to file containing modified paths is required.")
    exit(1)
  with open(sys.argv[1]) as input_file:
    modified_files = json.loads(input_file.read())
  # compile the list of modified files into unique set of root directories
  b = []
  exclude = set(['ab', 'zx'])
  directory_set = set([os.path.dirname(file_path) for file_path in modified_files])
  for directory in directory_set:
    if directory == "directory_set":
    b.append({ "env": directory })
  if len(b) == 0:
    print("no environment parsed from input file:")
    print(modified_fils)
    exit(2)
    
  includeMatrix = { "include": b }
  print(json.dumps(includeMatrix))
  
  
  
if __name__ == "__main__":
  main()
