# Polynomial Expression Solver

This Python script provides functionality to work with polynomial expressions, including setting coefficients, adding to coefficients, computing derivatives, computing antiderivatives, and evaluating roots.

## Usage

1. Instantiate polynomial objects: Create `Polynomial` objects with the coefficients of the polynomial expression.
2. Perform operations: Use methods such as `setCoefficient()`, `addToCoefficient()`, `derivative()`, `antiDerivative()`, `evaluate()`, and `linear_multiplication()` to manipulate and analyze polynomial expressions.

## Requirements
Python 3.x

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests if you find any bugs or want to improve the code.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

3. Example usage:

```python
from Polynomial import Polynomial

def main():
    p = Polynomial([2, 3, 4])
    v = Polynomial([5, 12, 16])
    
    # Example operations
    p.setCoefficient(99, 0)
    p.derivative()
    p.antiDerivative()
    p.evaluate()
    p.linear_multiplication(5)
    
