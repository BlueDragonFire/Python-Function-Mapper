#This class is for reading through a path and creating a map of all files and folders therein

import os

class path_scanner:


    def BFS(self, path):
        print('')
        for (root,dirs,files) in os.walk(path):
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            files[:] = [f for f in files if f.endswith('.py') | f.endswith('.json')]
            print(root)
            print(dirs)
            print(files)
            print("=======================")


a = path_scanner()

b = a.BFS("/home/heph/Python/yt-dlp")
