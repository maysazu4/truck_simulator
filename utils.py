# fn loads all sub python files from road_types dir

import os
from importlib import import_module

# load file names
operation_files = [f.replace(".py","") for f in os.listdir('road_types') if f.endswith('.py') and not f.startswith("__")]
# ["add"]

def load_road_types():
    operations = {}
    for name in operation_files:
        module = import_module(f"road_types.{name}")
        fn = getattr(module,name)
        if callable(fn):
            operations[name] = fn
    return operations
