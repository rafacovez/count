x = 0
number = 0

# Ask for input
def inputValue():
  global number

  number = input("How many sheeps do you want me to count? ")

  # Handle error in case input is not a positive number
  try:
    number = int(number)
  except:
    number = -1

def count():
  global x
  
  # Check if variable number is a positive number
  if number < 0:
    print("That's not a valid number")
  # Count to number given
  else:
    while x < number:
      x = x + 1
      print(x, "sheeps")

def main():
  inputValue()
  count()

main()