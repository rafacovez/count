# Declare variables
x = 0
number = 0

# Ask for input
def inputValue():
  global number
  print("How many sheeps do you want me to count?")
  number = input()
  isNumeric = number.isnumeric()
  while not isNumeric:
    print("I can't count to a negative number of sheeps! let's try again...")
    number = input()
    isNumeric = number.isnumeric()
  number = int(number)

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