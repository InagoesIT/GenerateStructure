# InaVivdiciA6_6BGenerateStructure
The project for the course "Python" in the 5th semester of university. The project is of class B, index 6, name: Generate Structure.

## The requirements:
  Creati un script care primeste de la linia de comanda un path catre un director si un fisier
  JSON. In fisierul JSON se afla un dictionar in care se afla o structura de directoare si fisiere
  astfel: fiecare cheie care are ca valoare un dictionar este un director iar dictionarul contintul,
  iar fiecare cheie care are ca valoare un string reprezinta un fisier iar string-ul respectiv este
  continutul fisierului. Scriptul va crea in folderul dat ca argument directoarele si fisierele
  conform dictionarului din JSON.
  
  INPUT: ```py create_structure.py root_folder_path structure_json_file_path```
  Exemplu de dictionar:
  ```py {“dir1” : {“dir2”: {“file1”: “continut1”, “file2”: “continut2”}, “file3”: “continut3”}, “file4”: “continut4”}```
  
  OUTPUT:
  root_folder
  ---dir1
  ------dir2
  ---------file1: continut1
  ---------file2: continut2
  ------file3: continut3
  ---file4: continut4
