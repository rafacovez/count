# Declare variable

x = 0

# Ask for input

number = int(input("What number do you want me to count to? "))

# Count to number given

def count():
  global x
  while x < number:
    x = x + 1
    print(x)

count()