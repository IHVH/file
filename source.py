import os
from dataclasses import dataclass

@dataclass
class Point:
     x: int
     y: int


filename = r"Download\test.txt"
path = os.path.dirname(filename)
os.makedirs(path, exist_ok=True)
with open(filename, "w") as f:
    f.write("test")



