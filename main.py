import Polynomial
def main():

    p = Polynomial.Polynomial([2, 3, 4])
    v = Polynomial.Polynomial([5, 12, 16])
    print("1st", end="")
    p.__str__()
    print("2nd", end="")
    v.__str__()
    p.addToCoefficient(100, 0)
    print("After Adding to Coefficient: ", end="")

    p.__str__()
    print("After Setting Coefficient: ", end="")
    p.setCoefficient(99, 0)
    print("1st ", end="");
    p.__str__()
    print("Dervied: ", end="")
    p.derivative()
    print("Anti Derived: ", end="")
    p.antiDerivative()
    p.evaluate()

    print()
    p.linear_multiplication(5)
    print()

    print("2nd ", end="");
    v.__str__()

    print()

    Polynomial.Polynomial.__add__(p,v)
    Polynomial.Polynomial.__sub__(p,v)



if __name__ == '__main__':
    main()