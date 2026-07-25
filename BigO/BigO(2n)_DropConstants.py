def print_items(n):
    for i in range(n): #n times iterated
        print(i)

    for j in range(n): #n times iterated
        print(j)

print_items(10)

'''In this program we have 2 for loops iterated n times. So Big O can be writted as O(2N).
We can drop constants in this case, so O(100n) is same as O(2n) or O(n)'''
