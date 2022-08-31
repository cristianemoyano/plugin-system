import os
import sys

def setup_path() -> None:
    path: str = os.path.join(os.path.dirname(__file__), os.pardir)
    sys.path.append(path)  

setup_path()