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

def ask_for_int():
        myNum = int(input("Please enter a number:\n"))
        collatz(myNum)
        while x !=1:
            collatz(x)
          
if __name__ == '__main__':
    try:
        ask_for_int()
    except:
        print("Error, please enter an integer")
        ask_for_int()
