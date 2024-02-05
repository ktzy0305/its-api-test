import os
from constants import PROGRAMS_DIR, PARSED_FILE_DIR
from utils import write_to_json_file
from its_functions import parser, alignment_structure

def test_parser():
  parsed_program = parser(os.path.join(PROGRAMS_DIR, "empty.py"))
  if parsed_program is not None:
    write_to_json_file(filepath=os.path.join(PARSED_FILE_DIR, "parsed_program.json"), data=parsed_program)
    print("Success")
    
def test_alignment_structure():
  reference_program_path = os.path.join(PROGRAMS_DIR, "reference.py")
  student_program_path = os.path.join(PROGRAMS_DIR, "student.py")
  response = alignment_structure(
    referenced_filepath=reference_program_path, 
    student_filepath=student_program_path
  )
  if response is not None:
    print(response)
  
  
if __name__ == "__main__":
  test_parser()
  test_alignment_structure()
  