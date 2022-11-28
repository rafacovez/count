# Declare variable

x = 0
number = 0

# Ask for input

def inputValue():
  global number
  number = int(input("What number do you want me to count to? "))
  if number < 0:
    int(input("I can't count to a negative number! let's try again... "))

# Count to number given

def count():
  global x
  while x < number:
    x = x + 1
    print(x)

def main():
  inputValue()
  count()

main()