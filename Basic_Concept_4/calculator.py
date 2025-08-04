class Calculator:
    band = "Casio MS990"
    def add(self, num1, num2):
        return num1 + num2
    def multiply(self, num1, num2):
        return num1 * num2
    def division(self, num1, num2):
        return num1 / num2
    def sub(self, num1, num2):
        return num1 - num2

calc = Calculator()
res1 = calc.add(5, 10)
print("Addition = ", res1)
res2 = calc.sub(20, 10)
print("Subtract = ", res2)
res3= calc.multiply(5, 10)
print("Multiply = ", res3)
res4= calc.division(20, 10)
print("Division = ", res4)