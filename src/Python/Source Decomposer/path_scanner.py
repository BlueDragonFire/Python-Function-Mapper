#This class is for reading through a path and creating a map of all files and folders therein

import os
from json_builder import *

class path_scanner:


    def BFS(self, path):
        
        result = []
        for (root,dirs,files) in os.walk(path):
            temp = []
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            files[:] = [f for f in files if f.endswith('.py')]
            temp.extend((root, dirs, files))
            result.append(temp)
        
        return result