import os
import importlib
from kasm_compiler.keywords.base_keyword import BaseKeyword

# Dictionary to store all operator classes
KEYWORDS = {}

# List to store all public classes for __all__
__all__ = []

# Get the directory of the current file (KEYWORDS folder)
current_dir = os.path.dirname(__file__)

# Iterate over all Python files in the KEYWORDS folder
for filename in os.listdir(current_dir):
    if filename.endswith(".py") and filename != "base_keyword.py" and filename != "__init__.py":
        module_name = f"kasm_compiler.keywords.{filename[:-3]}"  # Remove .py extension
        module = importlib.import_module(module_name)

        # Iterate over all attributes in the module
        for attr_name in dir(module):
            attr = getattr(module, attr_name)

            # Check if the attribute is a class and is a subclass of BaseKeyword
            if isinstance(attr, type) and issubclass(attr, BaseKeyword) and attr is not BaseKeyword:
                KEYWORDS[attr().keyword] = attr
                globals()[attr_name] = attr  # Add the class to the global namespace
                __all__.append(attr_name)  # Add the class name to __all__