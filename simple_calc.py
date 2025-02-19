# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Enhanced Simple Calculator with Extended Operators and Python 2 Support
--------------------------------------------------------------------------
"""

import operator
import sys

# ------------------------------------------------------------------------
# Global Variables
# ------------------------------------------------------------------------

operators = {
    "+"  : operator.add,
    "-"  : operator.sub,
    "*"  : operator.mul,
    "/"  : operator.truediv,
    "%"  : operator.mod,
    "**" : operator.pow,
    ">>" : operator.rshift,
    "<<" : operator.lshift
}

# Detect Python version
PY2 = sys.version_info[0] == 2

# Use `raw_input()` for Python 2, `input()` for Python 3
def get_input(prompt):
    return raw_input(prompt) if PY2 else input(prompt)

# ------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------

def get_user_input():
    """Get input from the user and return valid numbers and an operator function."""
    
    try:
        num1 = get_input("Enter first number (or 'q' to quit): ")
        if num1.lower() == 'q':
            return None, None, None
        
        num2 = get_input("Enter second number: ")
        if num2.lower() == 'q':
            return None, None, None
        
        # Convert numbers to integers for bitwise operations
        num1 = int(num1) if ">>" in operators or "<<" in operators else float(num1)
        num2 = int(num2) if ">>" in operators or "<<" in operators else float(num2)

        op = get_input("Enter function (+, -, *, /, %, **, >>, <<) or 'q' to quit: ")
        if op.lower() == 'q':
            return None, None, None

        func = operators.get(op)
        
        if func is None:
            print("Invalid operator. Please enter one of: +, -, *, /, %, **, >>, <<")
            return None, None, None

        if op == "/" and num2 == 0:
            print("Error: Division by zero is not allowed.")
            return None, None, None

        return num1, num2, func
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return None, None, None

# ------------------------------------------------------------------------
# Main Script
# ------------------------------------------------------------------------

if __name__ == "__main__":
    while True:
        num1, num2, func = get_user_input()
        
        if num1 is None or num2 is None or func is None:
            print("Exiting program.")
            break
        
        print(f"Result: {func(num1, num2)}\n")

