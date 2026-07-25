def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

print_items(10)

'''In this program we pass n value as 10, there are 2 for loops.
for loop within a for loop, the out put is as below
00
01
...
99

The total iteration it takes is 100, this is 10**2 or n**2 what we sent.
This is BigO(n^2)'''
