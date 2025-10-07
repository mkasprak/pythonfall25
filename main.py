"""
demonstrate using our calculator module
"""

from math_operations import calculator

def main():
    result = calculator.add(5,3)
    print(f"Addition result {result}")

    result = calculator.subtract(6,2)
    print(f"Subtraction result {result}")

main()
