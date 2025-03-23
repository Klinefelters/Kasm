import os
import importlib
from kasm_compiler.operators.base_operator import BaseOperator

# Dictionary to store all operator classes
OPERATORS = {}

# Get the directory of the current file (operators folder)
current_dir = os.path.dirname(__file__)

# Iterate over all Python files in the operators folder
for filename in os.listdir(current_dir):
    if filename.endswith(".py") and filename != "base_operator.py" and filename != "__init__.py":
        module_name = f"kasm_compiler.operators.{filename[:-3]}"  # Remove .py extension
        module = importlib.import_module(module_name)

        # Iterate over all attributes in the module
        for attr_name in dir(module):
            attr = getattr(module, attr_name)

            # Check if the attribute is a class and is a subclass of BaseOperator
            if isinstance(attr, type) and issubclass(attr, BaseOperator) and attr is not BaseOperator:
                OPERATORS[attr().operator] = attr()