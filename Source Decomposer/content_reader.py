import re

class content_reader:

    def read_file(self, path):
        open_file = open(path, 'r')
        file_contents = open_file.read()
        return file_contents

    def find_functions(self, text):
        x = re.findall("def.*:", text)
        return x

    def get_functions(self, text):
        a = self.read_file(text)
        b = self.find_functions(a)
        return b