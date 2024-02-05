import os, requests
from constants import BASE_DIR, PARSED_FILE_DIR
from utils import convert_json_to_escaped_string, read_json_from_file, read_program_as_string, write_to_json_file

def parser(filepath):
  json_body = {
    "language": "python",
    "source_code": read_program_as_string(filepath=filepath)
  }

  response = requests.post("https://its.comp.nus.edu.sg/cs3213/parser", json=json_body)
  
  if response.status_code == 200:
    data = response.json()
    return data
      
  else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)
    return None

def alignment_structure(referenced_filepath, student_filepath):
  # Read the parsed reference program
  reference_program_text = parser(referenced_filepath)
  write_to_json_file(os.path.join(PARSED_FILE_DIR, "reference.json"), reference_program_text)
  reference_data = read_json_from_file(os.path.join(BASE_DIR, "parsed_files", "reference.json"))
  
  # Read the parsed student program
  student_program_text = parser(student_filepath)
  write_to_json_file(os.path.join(PARSED_FILE_DIR, "student.json"), student_program_text)
  student_data = read_json_from_file(os.path.join(BASE_DIR, "parsed_files", "student.json"))
  
  # Convert Python objects to JSON strings with escaped characters
  reference_json_string = convert_json_to_escaped_string(reference_data["program"])
  student_json_string = convert_json_to_escaped_string(student_data["program"])
  
  json_body = {
    "reference_solution": reference_json_string,
    "student_solution": student_json_string
  }
  
  response = requests.post("https://its.comp.nus.edu.sg/cs3213/alignment_structural", json=json_body)
  
  if response.status_code == 200:
    data = response.json()
    return data
  else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)
    return None