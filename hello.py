#!/usr/bin/env python3
"""
Scientific Calculator
A comprehensive calculator with basic arithmetic, scientific functions, and memory operations.
"""

import math
import sys

class ScientificCalculator:
    """A scientific calculator with memory and history features."""
    
    def __init__(self):
        """Initialize the calculator with empty memory and history."""
        self.memory = 0
        self.history = []
        self.last_result = 0
    
    def add_to_history(self, operation, result):
        """Add an operation and its result to the history."""
        self.history.append(f"{operation} = {result}")
        if len(self.history) > 10:  # Keep only last 10 operations
            self.history.pop(0)
    
    def basic_operations(self, a, b, operator):
        """Perform basic arithmetic operations."""
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y if y != 0 else float('inf'),
            '**': lambda x, y: x ** y,
            '%': lambda x, y: x % y if y != 0 else float('inf')
        }
        
        if operator in operations:
            result = operations[operator](a, b)
            operation_str = f"{a} {operator} {b}"
            self.add_to_history(operation_str, result)
            self.last_result = result
            return result
        else:
            raise ValueError(f"Unknown operator: {operator}")
    
    def scientific_functions(self, value, function):
        """Perform scientific functions on a single value."""
        functions = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'asin': math.asin,
            'acos': math.acos,
            'atan': math.atan,
            'sinh': math.sinh,
            'cosh': math.cosh,
            'tanh': math.tanh,
            'log': math.log10,
            'ln': math.log,
            'sqrt': math.sqrt,
            'exp': math.exp,
            'abs': abs,
            'ceil': math.ceil,
            'floor': math.floor,
            'factorial': math.factorial
        }
        
        if function in functions:
            try:
                result = functions[function](value)
                operation_str = f"{function}({value})"
                self.add_to_history(operation_str, result)
                self.last_result = result
                return result
            except ValueError as e:
                raise ValueError(f"Math domain error for {function}({value}): {e}")
        else:
            raise ValueError(f"Unknown function: {function}")
    
    def memory_operations(self, operation, value=None):
        """Handle memory operations (store, recall, clear, add, subtract)."""
        if operation == 'ms':  # Memory Store
            self.memory = value if value is not None else self.last_result
            return f"Memory stored: {self.memory}"
        elif operation == 'mr':  # Memory Recall
            return self.memory
        elif operation == 'mc':  # Memory Clear
            self.memory = 0
            return "Memory cleared"
        elif operation == 'm+':  # Memory Add
            self.memory += value if value is not None else self.last_result
            return f"Added to memory. Memory: {self.memory}"
        elif operation == 'm-':  # Memory Subtract
            self.memory -= value if value is not None else self.last_result
            return f"Subtracted from memory. Memory: {self.memory}"
        else:
            raise ValueError(f"Unknown memory operation: {operation}")
    
    def get_constants(self, constant):
        """Return mathematical constants."""
        constants = {
            'pi': math.pi,
            'e': math.e,
            'tau': math.tau,
        }
        
        if constant in constants:
            return constants[constant]
        else:
            raise ValueError(f"Unknown constant: {constant}")
    
    def show_history(self):
        """Display calculation history."""
        if not self.history:
            return "No history available"
        return "\n".join(["History:"] + self.history)
    
    def clear_history(self):
        """Clear calculation history."""
        self.history.clear()
        return "History cleared"

def display_menu():
    """Display the calculator menu options."""
    menu = """
    ╔═══════════════════════════════════════════╗
    ║           Scientific Calculator           ║
    ╠═══════════════════════════════════════════╣
    ║ Basic Operations:                         ║
    ║   +, -, *, /, **, % (modulo)             ║
    ║                                           ║
    ║ Scientific Functions:                     ║
    ║   sin, cos, tan, asin, acos, atan         ║
    ║   sinh, cosh, tanh                        ║
    ║   log (base 10), ln (natural log)         ║
    ║   sqrt, exp, abs, ceil, floor, factorial  ║
    ║                                           ║
    ║ Constants:                                ║
    ║   pi, e, tau                              ║
    ║                                           ║
    ║ Memory Operations:                        ║
    ║   ms (store), mr (recall), mc (clear)     ║
    ║   m+ (add), m- (subtract)                 ║
    ║                                           ║
    ║ Special Commands:                         ║
    ║   history, clear, help, quit              ║
    ╚═══════════════════════════════════════════╝
    """
    print(menu)

def parse_input(user_input):
    """Parse user input and determine the operation type."""
    user_input = user_input.strip().lower()
    
    # Check for special commands
    if user_input in ['quit', 'exit', 'q']:
        return 'quit', None
    elif user_input in ['help', 'h']:
        return 'help', None
    elif user_input == 'history':
        return 'history', None
    elif user_input == 'clear':
        return 'clear_history', None
    
    # Check for constants
    constants = ['pi', 'e', 'tau']
    if user_input in constants:
        return 'constant', user_input
    
    # Check for memory operations
    memory_ops = ['ms', 'mr', 'mc', 'm+', 'm-']
    if user_input in memory_ops:
        return 'memory', user_input
    
    # Check for scientific functions
    sci_functions = ['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'sinh', 'cosh', 'tanh',
                    'log', 'ln', 'sqrt', 'exp', 'abs', 'ceil', 'floor', 'factorial']
    
    for func in sci_functions:
        if user_input.startswith(func + '(') and user_input.endswith(')'):
            try:
                value_str = user_input[len(func)+1:-1]
                value = float(value_str)
                return 'scientific', (func, value)
            except ValueError:
                return 'error', f"Invalid number in {func}()"
    
    # Check for basic operations
    operators = ['+', '-', '*', '/', '**', '%']
    for op in operators:
        if op in user_input:
            parts = user_input.split(op)
            if len(parts) == 2:
                try:
                    a = float(parts[0].strip())
                    b = float(parts[1].strip())
                    return 'basic', (a, b, op)
                except ValueError:
                    return 'error', "Invalid numbers in expression"
    
    # Try to parse as a single number
    try:
        value = float(user_input)
        return 'number', value
    except ValueError:
        return 'error', "Invalid input format"

def main():
    """Main function to run the calculator."""
    calculator = ScientificCalculator()
    
    print("Welcome to the Scientific Calculator!")
    print("Type 'help' for instructions or 'quit' to exit.")
    
    while True:
        try:
            user_input = input("\nCalc> ").strip()
            
            if not user_input:
                continue
            
            operation_type, data = parse_input(user_input)
            
            if operation_type == 'quit':
                print("Thank you for using the Scientific Calculator!")
                break
            
            elif operation_type == 'help':
                display_menu()
            
            elif operation_type == 'history':
                print(calculator.show_history())
            
            elif operation_type == 'clear_history':
                print(calculator.clear_history())
            
            elif operation_type == 'constant':
                result = calculator.get_constants(data)
                print(f"{data} = {result}")
                calculator.last_result = result
            
            elif operation_type == 'memory':
                result = calculator.memory_operations(data)
                print(result)
            
            elif operation_type == 'scientific':
                func, value = data
                result = calculator.scientific_functions(value, func)
                print(f"{func}({value}) = {result}")
            
            elif operation_type == 'basic':
                a, b, op = data
                result = calculator.basic_operations(a, b, op)
                print(f"{a} {op} {b} = {result}")
            
            elif operation_type == 'number':
                print(f"Number entered: {data}")
                calculator.last_result = data
            
            elif operation_type == 'error':
                print(f"Error: {data}")
                print("Type 'help' for usage instructions.")
        
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Type 'help' for usage instructions.")

if __name__ == "__main__":
    main()