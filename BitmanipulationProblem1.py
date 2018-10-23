# Python3 program for implementation
# of updateBits()

# Function to updateBits M insert to N.
def updateBits(n, m, i, j):
    # Create a mask to clear bits i through
    # j in n. EXAMPLE: i = 2, j = 4. Result
    # should be 11100011. For simplicity,
    # we'll use just 8 bits for the example.

    # will equal sequence of all ls
    allOnes = ~0
    print(allOnes)

    # ls before position j,
    # then 0s. left = 11100000
    left = allOnes << (j + 1)
    print(left)
    # l's after position i. right = 00000011
    right = ((1 << i) - 1)
    print(right)
    # All ls, except for 0s between
    # i and j. mask 11100011
    mask = left | right
    print(mask)
    # Clear bits j through i then put min there
    n_cleared = n & mask

    # Move m into correct position.
    m_shifted = m << i

    return (n_cleared | m_shifted)


# Driver Code
n = 1024  # in Binary N = 10000000000
m = 19  # in Binary M = 10011
i = 2;
j = 6
print(updateBits(n, m, i, j))

# This code is contributed by Anant Agarwal.
