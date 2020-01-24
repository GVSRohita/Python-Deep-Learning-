print("Enter two number")
# print("Enter first number :")
Num1 = int(input("Enter first number :"))
# print("Enter second number :")
Num2 = int(input("Enter second number :"))
if Num2 == 0:
	Num2 = int(input("Denominator should not be 0  Enter second number :"))
Sum = Num1 + Num2
Dif = Num1 - Num2
Mul = Num1 * Num2
Div = Num1 / Num2
print("Sum of two number is :",Sum)
print("Difference between two number is :",Dif)
print("Product of two number is :",Mul)
print("Division of two number is :",Div)