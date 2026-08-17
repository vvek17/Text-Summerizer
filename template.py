import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format= '[%(asctime)s]: %(message)s:')

project_name = "textSummerizer"

list_of_files = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/constant/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Docerfile",
    "requirment.txt",
    "setup.py",
    "research/trials.ipynb"
    
]

# looking for a list stuff from list_of_files , we trying to create a file dynamically rather than creating manually

for filepath in list_of_files:
    filepath = Path(filepath)
    # first we will go for the folder and then file so we need to create folder first and then file
    filedir,filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory: {filedir} for the file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"creating empty file : {filepath}")
            
    else:
        logging.info(f"{filename} is already existscl") 
        