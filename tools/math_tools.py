from langchain_core.tools import tool
import math
import cmath
from sympy import simplify

@tool
def add(a:float, b:float) -> float:
    "Adds two numbers"
    return a+b

@tool
def subtract(a:float, b:float) -> float:
    "SUbstract the second number from the first"
    return a-b

@tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers."""
    return a * b

@tool
def divide(a: float, b: float) -> float:
    """Divides the first number by the second."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

@tool
def modulus(a: int, b: int) -> int:
    """Returns the remainder when a is divided by b."""
    return a % b

@tool
def power(a: float, b: float) -> float:
    """Returns a raised to the power of b."""
    return a ** b

@tool
def square_root(a: float) -> float | complex:
    """Returns the square root of a number."""
    if a >= 0:
        return math.sqrt(a)
    return cmath.sqrt(a)

##Math Expressions##
@tool
def evaluate_expression(expression: str) -> float | str:
    """
    Evaluates a safe mathematical expression.
    Supports +, -, *, /, %, **, sqrt, pow, abs, math functions.
    Example: "sqrt(9) + pow(2, 3) / 4"
    """
    allowed_names = {
        "sqrt": math.sqrt,
        "pow": pow,
        "abs": abs,
        "round": round,
        "math": math,
    }
    try:
        result = eval(expression, {"__builtins__": None}, allowed_names)
        return result
    except Exception as e:
        return f"Error evaluating expression: {str(e)}"
    
@tool
def simplify_expression(expr: str) -> str:
    """
    Simplifies an algebraic expression symbolically.
    Example: "2*x + 3*x - 5" -> "5*x - 5"
    """
    try:
        return str(simplify(expr))
    except Exception as e:
        return f"Error simplifying expression: {str(e)}"