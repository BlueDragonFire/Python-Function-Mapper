#This class is for reading through a path and creating a map of all files and folders therein

import os

class path_scanner:

    def detect_folders(self, path):

        folder_list = []

        for i in os.listdir(path):
            if not os.path.isfile(os.path.join(path, i)):
                if not i.startswith('.'):
                    folder_list.append(i)
                    
        return folder_list

    #possibly redundant
    def detect_all_files(self, path):

        file_list = []
        for i in os.listdir(path):
            if os.path.isfile(os.path.join(path, i)):
                file_list.append(i)
                #print(i)

        return file_list

    def detect_python_files(self, path):

        file_list = []
        for i in os.listdir(path):
            if os.path.isfile(os.path.join(path, i)):
                if i.endswith('.py'):
                    file_list.append(i)

        return file_list

    def BFS(self, path):
        x = os.walk(path)
        return x


a = path_scanner()

b = a.BFS("/home/heph/Python/Constellator")
print('')
for i in b:
    print(i)