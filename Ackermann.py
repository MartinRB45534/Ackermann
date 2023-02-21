# Let's see if we can make the Ackermann function using iteration

# First, let's do a recursive version for comparison

def recursiveAckermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return recursiveAckermann(m - 1, 1)
    else:
        return recursiveAckermann(m - 1, recursiveAckermann(m, n - 1))
    
# Now, let's do the iterative version

def iterativeAckermann(m, n):
    # We'll use a stack to keep track of the values of m and n that aren't calculated yet
    stack = [(m, n)]
    # We'll use a dictionary to keep track of the values of m and n that are calculated
    # We'll use the tuple (m, n) as the key, and the value of the Ackermann function as the value
    dict_ = {}
    # We'll use a while loop to keep going until the stack is empty
    while stack:
        # Get the top of the stack
        m, n = stack[-1]
        # If m is 0, we can calculate the value of the Ackermann function
        if m == 0:
            # Calculate the value
            value = n + 1
            # Pop the top of the stack
            stack.pop()
            # Add the value to the dictionary
            dict_[m, n] = value
        # If n is 0, we need the value of the Ackermann function for m - 1 and 1
        elif n == 0:
            # Check if the value is in the dictionary
            if (m - 1, 1) in dict_:
                # If it is, pop the top of the stack
                stack.pop()
                # Calculate the value
                value = dict_[m - 1, 1]
                # Add the value to the dictionary
                dict_[m, n] = value
            else:
                # If it isn't, add the value to the stack
                stack.append((m - 1, 1))
        # If neither m nor n is 0, we need the value of the Ackermann function for m and n - 1
        else:
            if (m, n - 1) in dict_:
                # If the value is in the dictionary, we need the value of the Ackermann function for m - 1 and the value we just calculated
                if (m - 1, dict_[m, n - 1]) in dict_:
                    # If the value is in the dictionary, pop the top of the stack
                    stack.pop()
                    # Calculate the value
                    value = dict_[m - 1, dict_[m, n - 1]]
                    # Add the value to the dictionary
                    dict_[m, n] = value
                else:
                    # If the value isn't in the dictionary, add it to the stack
                    stack.append((m - 1, dict_[m, n - 1]))
            else:
                # If the value isn't in the dictionary, add it to the stack
                stack.append((m, n - 1))
    # Return the value of the Ackermann function for m and n
    # It's the last one we calculated
    return value

# Let's test it out
print(recursiveAckermann(3, 4))
print(iterativeAckermann(3, 4))

print(recursiveAckermann(3, 5))
print(iterativeAckermann(3, 5))
