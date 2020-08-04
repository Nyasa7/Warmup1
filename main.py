def sum():
  num1 = 1
  num2 = 2
  num3 = 3
  num4 = 4
  for i in range(1):
    print(num1 + num2 + num3 + num4)

sum()

def multiply():
  num1 = 1
  num2 = 2
  num3 = 3
  num4 = 4
  for i in range(1):
    print(num1 * num2 * num3 * num4)

multiply()

def sum(nums):
  result = 0
  for i in nums:
    result += i
  return result


def calc():
  num1 = float(input("Choose a number: "))
  num2 = float(input("Choose second number: "))
  op = float(input("Choose operator: "))
  if op == "+":
    print(num1 + num2)
  elif op == "/":
    print(num1 / num2)
  elif op == "*":
    print(num1 * num2)
  elif op == "-":
      print(num1 - num2)
calc()