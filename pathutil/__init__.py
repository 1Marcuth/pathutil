from pydantic import validate_arguments
import os

@validate_arguments
def mktree(path: str):
    
    if os.path.exists(path):
        if os.path.isfile(path):
            raise Exception("ERROR: The path cannot be a file.")

    if os.path.sep in path:
        dirs = path.split(os.path.sep)

    else:
        dirs = path.split(os.path.altsep)

    current_dir = ""

    for dir in dirs:
        current_dir = os.path.join(current_dir, dir)
        
        if not os.path.exists(current_dir):
            os.mkdir(current_dir)
