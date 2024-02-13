from path_scanner import *
from content_reader import *
from graph_builder import *
import json

def main(path):
    
    x = graph_builder()
    y = path_scanner()
    a = y.search(path)
    x.create_graph_file(a)

if __name__ == "__main__":
    print("input directory")
    x = input()
    main(x)