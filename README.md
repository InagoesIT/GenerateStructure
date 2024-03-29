# InaVivdiciA6_6BGenerateStructure
The project for the course "Python" in the 5th semester of university. The project is of class B, index 6, name: Generate Structure.

## [The requirements](https://drive.google.com/file/d/1_1WIMjIdwAQkqX9yXBwbUNlhv7HsCNzg/view?usp=sharing):
### Romanian
  Creati un script care primeste de la linia de comanda un path catre un director si un fisier
  JSON. In fisierul JSON se afla un dictionar in care se afla o structura de directoare si fisiere
  astfel: fiecare cheie care are ca valoare un dictionar este un director iar dictionarul contintul,
  iar fiecare cheie care are ca valoare un string reprezinta un fisier iar string-ul respectiv este
  continutul fisierului. Scriptul va crea in folderul dat ca argument directoarele si fisierele
  conform dictionarului din JSON.
  
  #### INPUT: 
  ```python 
  create_structure.py root_folder_path structure_json_file_path
  ```
  Exemplu de dictionar: {“dir1” : {“dir2”: {“file1”: “continut1”, “file2”: “continut2”}, “file3”: “continut3”}, “file4”: “continut4”}
  
  #### OUTPUT:
  root_folder  
  ---dir1  
  ------dir2  
  ---------file1: continut1  
  ---------file2: continut2  
  ------file3: continut3  
  ---file4: continut4  

  ### English
  Create a script that gets a path to a directory and a JSON file from the command line. 
  The JSON file will contain a dictionary that contains a structure of folders and files in this manner: 
  every key that has as a value a dictionary is a directory name and the dictionary is its content, 
  and every key that is a string represents a file name and its value is the content of the file. 
  In the directory given as an argument to the script, the script will create all the directories 
  and files as specified in the JSON file. 
  
  #### INPUT: 
  ```python 
  create_structure.py root_folder_path structure_json_file_path
  ```
  Dictionary example: {“dir1” : {“dir2”: {“file1”: “content1”, “file2”: “content2”}, “file3”: “content3”}, “file4”: “content4”}
  
  #### OUTPUT:
  root_folder  
  ---dir1  
  ------dir2  
  ---------file1: content1  
  ---------file2: content2  
  ------file3: content3  
  ---file4: content4  
  
  ## The steps needed for completing this project are:
  1. Create the project structure
  2. Extract and validate the command line arguments
  3. Extract the dictionary from the JSON file
  4. Validate the dictionary
  5. Generate the specified folder structure
  6. Print the directory structure
