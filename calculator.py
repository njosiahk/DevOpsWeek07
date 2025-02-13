import math

# Addition
def add(num1, num2):
    return num1 + num2

# Subtraction
def subtract(num1, num2):
    return num1 - num2

# Multiplication
def multiply(num1, num2):
    return num1 * num2

# Division
def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is undefined."
    return num1 / num2

# Cosine
def cosine(angle_degrees):
    return math.cos(math.radians(angle_degrees))

# Sine
def sine(angle_degrees):
    return math.sin(math.radians(angle_degrees))

# Tangent
def tangent(angle_degrees):
    return math.tan(math.radians(angle_degrees))
