#This class is for converting a given list into json format
from content_reader import *

class graph_builder:

    def DOT_formatter(self, path):

        x = graph_builder()
        y = content_reader()

        graph_string = ''
        path_comps = path.split('/')
        path_comps.pop(0)

        for i in path_comps:
            if not i == path_comps[-1]:
                graph_string += ("\"" + i + "\"" + "->")
            else:
                graph_string += ("\"" + i + "\"")

        return graph_string



    def create_graph_file(self, path):

        x = graph_builder()
        y = content_reader()

        try:

            f = open("Constellator/Output/graph.gv", "x")
            print("Creating graph file")
            f.write("strict digraph G { \n \n")

            for i in path:
                f.write("   " + x.DOT_formatter(i) + "\n")
                for j in y.get_functions(i):
                    f.write("   " + x.DOT_formatter(i) + "->" +"\"" + j + "\"" + "\n")

            f.write("\n}")
            print("Writing complete")

        except:

            print("graph file already exists. Overwriting...")
            f = open("Constellator/Output/graph.gv", "w")
            print("Creating graph file")
            f.write("strict digraph G { \n \n")

            for i in path:
                f.write("   " + x.DOT_formatter(i) + "\n")
                for j in y.get_functions(i):
                    f.write("   " + x.DOT_formatter(i) + "->" +"\"" + j + "\"" + "\n")

            f.write("\n}")
            print("Overwriting complete")



