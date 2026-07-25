def print_items(n):
    for i in range(n):          #total n^2 iterations
        for j in range(n):
            print(i,j)

    for k in range(n):  #total n iterations
        print(k)

print_items(10)

'''In the above function we have two for loops.
The first have a for loop inside another for loop which makes the iteration n^2
The second for loop have iteration of n
So we have O(n^2)+O(n)
Here O(n^2) is dominant, we ignore O(n)'''
