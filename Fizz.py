import sys

n = int(sys.argv[1])

print(["Fizz"*(not i%3) + "Buzz"*(not i%5) or i for i in range(1,n)])
