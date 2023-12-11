from collections import Counter
x = int(input())
y = Counter(map(int, input().split()))
z = int(input())

total = 0
for i in range(z):
    size, rate = map(int, input().split())
    if y[size]: 
        y[size] -= 1
        total += rate
print(total)

'''
The first line contains X, the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains N, the number of customers.
The next N lines contain the space separated values of the shoe size desired by the customer and x(i) , the price of the shoe.

Print the amount of money earned by Raghu.'''