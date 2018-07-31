# Example python script of the Collatz Sequence
# Daniel G.
# Python 3.6.5

def collatz(num):
    global x
    if num % 2 == 0:
        x = num // 2
    else:
        x = 3 * num +1
    print(x)
    
x = 0
myNum = int(input("Please enter a number:\n"))
collatz(myNum)
while x !=1:
    collatz(x)
