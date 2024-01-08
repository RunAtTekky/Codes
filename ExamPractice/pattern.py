# Maximum number of stars in a line
n = 5

# Printing the upper triangle
for i in range(1,n+1):

    for j in range(1,i+1):
        print("*", end="")
    
    print()

# Printing the lower triangle
for i in range(n-1,0,-1):

    for j in range(1, i+1):
        print("*", end="")
    print()

