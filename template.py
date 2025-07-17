import os 
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
project_name="real-time-video-optimizer"

list_of_files=[
        ".github/workflows/.gitkeep",
    f"{project_name}/data/__init__.py",
    f"{project_name}/models/__init__.py",
    f"{project_name}/data/__init__.py",
    f"{project_name}/data/__init__.py",
    f"{project_name}/data_preprocessing.py",
    f"{project_name}/evaluation.py",
    f"{project_name}/machine_learning.py",
    f"{project_name}/network_optimization.py",
    f"{project_name}/real_time_processing.py",
    f"{project_name}/video_compression.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "test.py"

]
    
for filepath in list_of_files:
    filepath =Path(filepath)
    filedir ,filename=os.path.split(filepath)
    
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w")as f:
            pass
            logging.info(f"Creating empty file:{filepath}")
    else:
        logging.info(f"{filename} IS already Exsit")
