import sys
def addition(left, right):
   return left + right
def subtraction(left, right):
   return left - right
def multiplication(left, right):
   return left * right
def division(left, right):
   if right == 0:
       raise ZeroDivisionError("Division by zero")
   return left / right
def modulus(left, right):
   if right == 0:
       raise ZeroDivisionError("Modulus by zero")
   return left % right
def power(left, right):
   return left ** right
def floor_division(left, right):
   if right == 0:
       raise ZeroDivisionError("Floor division by zero")
   return left // right

operations = {
   '+': addition,
   '-': subtraction,
   '*': multiplication,
   '/': division,
   '%': modulus,
   '**': power,
   '//': floor_division
}

def value_expression(expression):
   try:
       
       parts = expression.split()
       left = float(parts[0])
       operator = parts[1]
       right = float(parts[2])
       if operator not in operations:
           raise ValueError("Invalid operator")
      
       result = operations[operator](left, right)
       return result
   except (IndexError, ValueError, ZeroDivisionError) as e:
       return f"Error: Invalid Expression - {expression} ({e})"
def main():
   print("Welcome to Terminal Calculator!")
   print("Enter expressions to evaluate. Type 'quit' or 'q' to exit.")
   while True:
       expression = input("Please enter an Expression:\n:> ")
       if expression.lower() in ['quit', 'q']:
           print("Exiting Calculator. Goodbye!")
           sys.exit(0)
       result = value_expression(expression)
       print(f"Result: {expression} = {result}")
if __name__ == "__main__":
   main()