from path_scanner import *
from content_reader import *
from json_builder import *
import json

def main(path):
    
    scan = path_scanner()
    read = content_reader()
    jsonify = json_builder()
    
    x = scan.BFS(path)
    print(json.dumps(x))
    #y = read.get_functions(x[2])
    #print(y)
    #json.jsonify_and_create(read.get_functions(scan.BFS(path)))



#if __name__ == "__main__":
    #print("input directory")
    #x = input()
    #main("/home/heph/Python/yt-dlp")