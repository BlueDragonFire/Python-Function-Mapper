#This class is for reading through a path and creating a map of all files and folders therein

import glob
from content_reader import *

class path_scanner:

    def search(self, path):
        
        x = glob.glob(path + "/**/*.py", recursive=True)

        return x