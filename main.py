# Checks for a number in a range
#num = int(input("Enter a number: "))
def rangecheck(num): # This is called a function declaration
    min = 0
    max = 100
    for i in range(min, max):  # Loop that continues for a known number of iterations
        #print(i)
        #if i in range(0, 100):
        if num > min and num < max:  # Conditional statement
            print(num)
            #exit()  # Will exit the current program
            break  # Will exit the current loop
        else:
            print(f"Number {num} not in {min} to {max}.")
            #exit()
            break

# Once I have declared/created a function, I need to make a FUNCTION CALL
rangecheck(140)
rangecheck(20)
for i in range(1, 51):
    a = i
    b = i * 10
    rangecheck(a)
    rangecheck(b)
    a += i
    b -= i