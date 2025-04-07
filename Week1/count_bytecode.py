import dis
import collections
import importlib.util
import sys

def count_instructions(module):
    """Disassemble all functions in a module and count bytecode instructions."""
    instruction_counts = collections.Counter()

    for name in dir(module):
        obj = getattr(module, name)
        if callable(obj):  # Check if the attribute is a function
            bytecode = dis.Bytecode(obj)
            for instr in bytecode:
                instruction_counts[instr.opname] += 1

    # Print results
    print("\nBytecode instruction counts in quicks.py:")
    for instr, count in instruction_counts.items():
        print(f"{instr}: {count}")

    return instruction_counts

def load_module_from_file(filepath, module_name="quicks"):
    """Dynamically load a module from a Python file."""
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

if __name__ == "__main__":
    quicks_path = "crypto.py"  # Change this if the file is in another directory

    try:
        quicks_module = load_module_from_file(quicks_path)
        count_instructions(quicks_module)
    except FileNotFoundError:
        print(f"Error: File '{quicks_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")
