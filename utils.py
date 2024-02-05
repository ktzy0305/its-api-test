import json

def read_program_as_string(filepath):
  program_lines = ""
  with open(filepath, "r") as file:
    lines = file.readlines()
    for line in lines:
      program_lines += line
  file.close()
  return program_lines

def read_json_from_file(filepath):
  with open(filepath, "r") as json_file:
    json_object = json.load(json_file)
    return json_object

def write_to_json_file(filepath, data):
  with open(filepath, "w") as output_file:
    json.dump(data, output_file, indent=2)  
  
def convert_json_to_escaped_string(json_data):
  return json.dumps(json_data, ensure_ascii=False)