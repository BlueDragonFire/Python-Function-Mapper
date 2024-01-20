#This class is for reading through a path and creating a map of all files and folders therein

import os
from json_builder import *
from content_reader import *

class path_scanner:

    
    def BFS(self, path):
        
        c = content_reader()
        result = []
        for (root,dirs,files) in os.walk(path):
            temp = []
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            files[:] = [f for f in files if f.endswith('.py')]
            temp.extend((root, dirs, files))
            result.append(temp)

        for i in result:
            for j in i:
                if not len(j) == 0:
                    if not isinstance(j, str):
                        print(j)

        return result
a = path_scanner()
b = json_builder()
b.jsonify_and_create(a.BFS("/home/heph/Python/Constellator"))