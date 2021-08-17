# FizzBuzz

# 17/08/2021
# Sam Allen

# User inputs the target number
n = int(input("Enter a number: "))

for i in range(1,n+1):
    # Multiple of 3 and 5
    if(i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")

    # Multple of 3
    elif(i % 3 == 0):
        print("Fizz")

    # Multple of 5
    elif(i % 5 == 0):
        print("Buzz")

    # Standard number output
    else:
        print(i)

    # Increment current number 
    i += 1