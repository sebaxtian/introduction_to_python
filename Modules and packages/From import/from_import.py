# Import class Calculator from another module
from my_module import hello as hey
from calculator import Calculator

print(hey("User"))

calc = Calculator()  # Name `Calculator` used directly without prefix `calculator`
calc.add(2)
calc.multiply(100)
calc.divide(3)

print(calc.get_current())



