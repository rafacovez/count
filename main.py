# get input from user
number = input("How many sheeps do you want me to count? ")

# handle error in case input is not a positive number
try:
  number = int(number)
except:
  number = -1

x = 0

# count sheep to number given
if number < 0:
  print("That's not a valid input")
else:
  while x < number:
    x += 1
    print(x, "sheeps")