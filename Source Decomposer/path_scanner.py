#contains methods for reading through a path and creating a map of all files and folders therein

import os

class path_scanner:

    def detect_folders(path):

        #slice_0 = slice(0,1)
        folder_list = []

        for i in os.listdir(path):
            if not os.path.isfile(os.path.join(path, i)):
                if not i.startswith('.'):
                    folder_list.append(i)
                    
        return folder_list


    def detect_all_files(path):

        file_list = []
        for i in os.listdir(path):
            if os.path.isfile(os.path.join(path, i)):
                file_list.append(i)
                #print(i)

        return file_list

    def detect_python_files(path):

        file_list = []
        for i in os.listdir(path):
            if os.path.isfile(os.path.join(path, i)):
                if i.endswith('.py'):
                    file_list.append(i)

        return file_list

    print(detect_folders("/home/heph/Python/yt-dlp"))