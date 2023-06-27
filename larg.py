def maximum(x, y, z):

    if (x >= y) and (x >= z):

        largest = x

    elif (y >= x) and (y >= z):

        largest = y

    else:

        largest = z

    return largest

Output:

Let us consider the values x=2, y=5, and z=8:

largest=8

                                    
def maximum(x, y, z):

    list = [x, y, z]

    return max(list)
