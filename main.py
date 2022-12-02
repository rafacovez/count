# Declare variables
x = 0
number = 0

# Ask for input
def inputValue():
  global number
  number = input("How many sheeps do you want me to count? ")
  isNumeric = number.isnumeric()
  while not isNumeric:
    number = input("I can't count to a negative number of sheeps! let's try again... ")
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