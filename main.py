# Declare variables

x = 0
number = 0

# Ask for input

def inputValue():
  global number
  number = int(input("How many sheeps do you want me to count? "))
  while number < 0:
    number = int(input("I can't count to a negative number of sheeps! let's try again... "))
    continue

# Count to number given

def count():
  global x
  while x < number:
    x = x + 1
    print(x, "sheeps")

def main():
  inputValue()
  count()

main()