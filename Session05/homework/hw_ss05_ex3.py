prices = {}
prices['banana'] = 4
prices['apple'] = 2
prices['orange'] = 1.5
prices['pear'] = 3

stock = {}
stock['banana'] = 6
stock['apple'] = 0
stock['orange'] = 32
stock['pear'] = 15

for key in prices.keys():
    print(key)
    print('Price:', prices[key])
    print('Stock:', stock[key])
    print()

total = 0
for key in prices.keys():
    sum_each = prices[key] * stock[key]
    total += sum_each
print('Total:', total)
