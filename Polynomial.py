class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def setCoefficient(self, newCoefficient, power):
        self.coefficients[power] = newCoefficient
        return

    def addToCoefficient(self, amount, power):
        self.coefficients[power] += amount
        return

    def claer(self):
        for e in self.coefficients:
            e = 0
            return

    def derivative(self):
        derived = []
        for index, e in enumerate(self.coefficients):
            derived.append(index*e)
        der = Polynomial(derived)
        der.__str__()

    def antiDerivative(self):
        antiderived = []
        for index, e in enumerate(self.coefficients):
            if e == 0:
                antiderived.append(e)
            else:
                antiderived.append((e // (index+1)))
        antiderived[0] = "C"
        antider = Polynomial(antiderived)
        antider.__str__()

    def __add__(self, other):
        if len(self.coefficients) > len(other.coefficients):
            ans = self.coefficients
        else:
            ans = other.coefficients
        ran = min(len(self.coefficients),len(other.coefficients))
        for i in range(ran):
            ans[i] = other.coefficients[i] + self.coefficients[i]

        final_ans = Polynomial(ans)
        print("Added ", end="")
        final_ans.__str__()

    def __sub__(self, other):
        if len(self.coefficients) > len(other.coefficients):
            ans = self.coefficients
        else:
            ans = other.coefficients
        ran = min(len(self.coefficients), len(other.coefficients))
        for i in range(ran):
            ans[i] = other.coefficients[i] - self.coefficients[i] * 2

        final_ans = Polynomial(ans)
        print("Subtracted ", end="")
        final_ans.__str__()

    def __str__(self):
        print('Polynomial : ', end="")
        for i, number in enumerate(self.coefficients):
            print(f'{number}x^{i}', end="")
            if i < len(self.coefficients)-1:
                print(end=" + ")
        print()

    def linear_multiplication(self, n):
        for i, coeff in enumerate(self.coefficients):
            self.coefficients[i] = coeff * n
        print(f"Mupltiplied with {n} ", end="")
        self.__str__()
    def evaluate(self):
        a = self.coefficients[0]
        b = self.coefficients[1]
        c = self.coefficients[2]

        x1 = (-b + ((b**2)-4*a*c)**0.5)/2*a
        x2 = (-b - ((b ** 2) - 4 * a * c) ** 0.5) / 2 * a

        print(f'Roots :\tx1 = {x1}\t,\tx2 = {x2}')