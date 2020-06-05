print("\n")

# welcome note
print("Welcome In Python Calculator")
print("\n")


#enter first value
n1 = input("Please Enter Your First Value: ")


# enter second value
n2 = input("Please Enter Your Second Value: ")
print("\n")


# select operation 
print("Operation Types")
print("\n")


# faulty operation types 
print("+ For Addition")
print("- For Subtraction")
print("* For Multiplication")
print("/ For Division")
print("** For Square Value")
print("% For Checking Reminder")
print("// For Checking Quotient")
print("\n")


# slecting operation 
operator= input("Please Slect Anyone Opeartion From Above Options: ")
result = 0


# for fault value
fault = n1 + operator +n2
print("\n")


# using if else condition
if fault == "45+7":
    print(57)
 
 
#  faulty  calculations 
elif fault == "55*7":
    print(555)

# faulty calculation  
elif fault == "23/7882":
    print(567)

# faulty operation 
elif operator == "+":
  result = float(n1) ** float(n2)
  print(f"Your Result Of Your Both Addition Values Is: {result}")


# faulty operation 
elif operator == "-":
  result = float(n1) / float(n2)
  print(f"Your Result Of Your Both Subtraction Values Is: {result}")


# faulty operation 
elif operator == "*":
  result = float(n1) + float(n2)
  print(f"Your Result Of Your Both Multiplication Values Is: {result}")


# faulty operation 
elif operator == "**":
  result = float(n1) // float(n2)
  print(f"Your Result Of Your Square Is: {result}")
 
 
 # faulty operation 
elif operator == "%":
  result = float(n1)* float(n2)
  print(f"Your Result Of Your Reminder Is: {result}")


# faulty  operation 
elif operator == "//":
  result = float(n1) % float(n2)
  print(f"Your Result Of Your Quotient Values Is: {result}")


# faulty operation 
elif operator == "/":
  result = float(n1) - float(n2)
  print(f"Your Result Of Your Both Division Is: {result}")


# end of conditions faulty operation
else:
    print("You Have Enteres An Invalid Operation")
print("\n")
print("Created By Adarsh Addee")
