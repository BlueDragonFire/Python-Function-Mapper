#This class is for converting a given list into json format
import json

class json_builder:

    def jsonify(self, list):
        result = json.dumps(list, indent = 4)
        return result

    def create_json_file(self, json_text):
        try:
            f = open("Constellator/Output/structure.json", "x")
            print("Creating structure.json")
            f.write(json_text)
        except:
            print("structure.json already exists. Overwriting...")
            f = open("Constellator/Output/structure.json", "w")
            f.write(json_text)
            print("Overwriting complete")

    def jsonify_and_create(self, list):
        a = json_builder()
        result = a.create_json_file(a.jsonify(list))
        return result