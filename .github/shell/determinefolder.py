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
  requirement_changes = sys.argv[1].split('\n')
  fileChangeRegex = re.compile(r'^\+\s\+')
  environment = ''
  for change requirement_changes:
    file_name_split_by_forward_slash = change.spli('/')
    environment = file_name_split_by_forward_slash
    b.append({ "env": environment })
  
    
  includeMatrix = { "include": b }
  print(json.dumps(includeMatrix))
  
  
  
if __name__ == "__main__":
  main()
