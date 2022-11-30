# InaVivdiciA6_6BGenerateStructure
The project for the course "Python" in the 5th semester of university. The project is of class B, index 6, name: Generate Structure.

## [The requirements](https://drive.google.com/file/d/1_1WIMjIdwAQkqX9yXBwbUNlhv7HsCNzg/view?usp=sharing):
  Creati un script care primeste de la linia de comanda un path catre un director si un fisier
  JSON. In fisierul JSON se afla un dictionar in care se afla o structura de directoare si fisiere
  astfel: fiecare cheie care are ca valoare un dictionar este un director iar dictionarul contintul,
  iar fiecare cheie care are ca valoare un string reprezinta un fisier iar string-ul respectiv este
  continutul fisierului. Scriptul va crea in folderul dat ca argument directoarele si fisierele
  conform dictionarului din JSON.
  
  ### INPUT: 
  ```python 
  create_structure.py root_folder_path structure_json_file_path
  ```
  Exemplu de dictionar: {“dir1” : {“dir2”: {“file1”: “continut1”, “file2”: “continut2”}, “file3”: “continut3”}, “file4”: “continut4”}
  
  ### OUTPUT:
  root_folder\n
  ---dir1\n
  ------dir2\n
  ---------file1: continut1\n
  ---------file2: continut2\n
  ------file3: continut3\n
  ---file4: continut4\n
  
  ## The steps needed for completing this project are:
  1. Extract and validate the command line arguments
  2. Extract the dictionary from the json file
  3. Validate the dictionary
  4. Generate the specified folder structure
  5. Print the directory structure
