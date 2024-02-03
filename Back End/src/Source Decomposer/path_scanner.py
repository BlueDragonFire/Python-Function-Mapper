#This class is for reading through a path and creating a map of all files and folders therein

import glob
from json_builder import *
from content_reader import *

class path_scanner:

    def BFS(self, path):
        
        x = glob.glob(path + "/**/*.py", recursive=True)

        return x
a = path_scanner()
b = json_builder()
b.jsonify_and_create(a.BFS("yt-dlp"))
#a.BFS("/home/heph/Python/Misc")