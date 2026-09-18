from addition import addition_2positional, addition_4default, addition_unlimited
from subtraction import subtraction
from multiplication import multiplication
from division import modulo_division, floor_division, normal_division

print("Addition:", addition_2positional(10, 20))

print("Addition with default:", addition_4default(10, 20))

print("Addition unlimited:", addition_unlimited([10, 20, 30, 40]))

print("Subtraction:", subtraction(20, 10))

print("Multiplication:", multiplication(2, 3, 4))

print("Modulo Division:", modulo_division(10, 3))

print("Floor Division:", floor_division(10, 3))

print("Normal Division:", normal_division(10, 3))