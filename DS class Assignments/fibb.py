# This function is used to find the Fibonacci number at position n
def fibonacci(n):
    
    # If n is 0, return 0
    # If n is 1, return 1
    # These are called base conditions
    if n <= 1:
        return n
    
    # If n is greater than 1
    # Call the function for (n-1) and (n-2)
    # Add both values and return the result
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Take input from the user for number of terms
terms = int(input("Enter number of terms: "))

# Print message before displaying Fibonacci series
print("Fibonacci series:")

# Loop from 0 to terms-1
for i in range(terms):
    
    # Call fibonacci function for each value of i
    # Print the returned value on the same line
    print(fibonacci(i), end=" ")