num1 = float(input("Enter a number :"))
op = (input("Enter an operator, do yo want to add, substract, multiply or divide? :"))
num2 =float(input("Enter another number :"))

if op == "+":
     result = num1 + num2
elif op == "-":
     result = num1 - num2
elif op == "/":
     result = num1 / num2
elif op == "*":
     result = num1 * num2


print(result)
print ("That's your result!")
print ("Thanks for using my calculator. Bye for now")
