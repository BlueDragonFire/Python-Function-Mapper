import json

class json_builder:

    def jsonify(self, list):
        result = json.dumps(list, indent = 4)
        return result

    def create_json_file(self, json_text):
        try:
            f = open("Constellator/Output Files/structure.json", "x")
            f.write(json_text)
        except:
            print("structure.json already exists. Overwriting...")
            f = open("Constellator/Output Files/structure.json", "w")
            f.write(json_text)
