#!/usr/bin/python3

import importlib.util

def print_module_names():
    # Load the compiled module hidden_4.pyc
    spec = importlib.util.spec_from_file_location("hidden_4", "/tmp/hidden_4.pyc")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Get all names defined in the module
    module_names = dir(module)

    # Print names that do not start with '__' in alphabetical order
    for name in sorted(module_names):
        if not name.startswith('__'):
            print(name)

if __name__ == "__main__":
    print_module_names()

