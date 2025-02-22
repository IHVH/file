import os
from dataclasses import dataclass
import json
import random

@dataclass
class Point:
     x: int
     y: int

     def __init__(self, x: int, y: int):
          self.x = x
          self.y = y

_I = 10

def write_file(data: str, i: int):

     filename = fr"Download\{i}-test.json"
     path = os.path.dirname(filename)
     os.makedirs(path, exist_ok=True)
     with open(filename, "w") as f:
          f.write(data)
    
    
def do_work():
     global _I
     while _I > 0:
          xr = random.randint(1, 999)
          yr = random.randint(1, 999)
          point = Point(xr, yr)
          json_object = json.dumps(point.__dict__)
          write_file(json_object, _I)
          _I -= 1


do_work()
print("OK")


