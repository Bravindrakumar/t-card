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
  
  
  
if __name__ == "__main__":
  main()
