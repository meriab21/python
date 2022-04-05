# Function for nth Fibonacci number
n = input()
def Fibonacci(n):

	# Check if input is 0 then it will
	# print incorrect input
    for i in range(0, n):
        if i < 0:
            print("Incorrect input")
        elif i == 0:
            return 0
        elif i == 1 or i == 2:
            return 1
        else:
            return Fibonacci(i-1) + Fibonacci(i-2)

# Driver Program
print(Fibonacci(n))

# This code is contributed by Saket Modi
# then corrected and improved by Himanshu Kanojiya
