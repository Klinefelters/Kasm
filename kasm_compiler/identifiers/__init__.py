import os
import importlib
from kasm_compiler.identifiers.base_identifier import BaseIdentifier

# Dictionary to store all operator classes
IDENTIFIERS = {}

# Get the directory of the current file (IDENTIFIERS folder)
current_dir = os.path.dirname(__file__)

# Iterate over all Python files in the IDENTIFIERS folder
for filename in os.listdir(current_dir):
    if filename.endswith(".py") and filename != "base_identifier.py" and filename != "__init__.py":
        module_name = f"kasm_compiler.identifiers.{filename[:-3]}"  # Remove .py extension
        module = importlib.import_module(module_name)

        # Iterate over all attributes in the module
        for attr_name in dir(module):
            attr = getattr(module, attr_name)

            # Check if the attribute is a class and is a subclass of BaseIdentifier
            if isinstance(attr, type) and issubclass(attr, BaseIdentifier) and attr is not BaseIdentifier:
                IDENTIFIERS[attr().identifier] = attr