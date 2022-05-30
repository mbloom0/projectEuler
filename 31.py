#Problem 31: Coin sums
"""In the United Kingdom the currency is made up of pound (£) and pence (p). There
 are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?"""

from itertools import combinations, repeat, chain


coinOptions = [1, 2, 5, 10, 20, 50, 100, 200]
coinOptions.reverse()
coinsAvailable = [200,100,40,20,10,4,2,1]
coinsAvailable.reverse()

coins = [list(repeat(x,y)) for (x,y) in zip(coinOptions,coinsAvailable)]
coins = list(chain(*coins))
print(coins)

def coin_sums(target):
    """ Return the number of ways to make a target amount of money using the
    available coins. """
    # Start with the largest coin, and accumulate solutions for every combination
    # of lesser denomintion coins that can make up for a larger one.

    # The number of ways to make a target amount of money using the available
    # coins is the number of ways to make the target amount of money using the largest coins,
    # plus the number of ways to make the largest coins using the smaller coins, and so on to the smallest coin.
    solutions = []

    currCombo = []
    for coin in coins:
        if coin == target:
            currCombo.append(coin)
            solutions.append(currCombo)
        elif 
        
#print(coin_sums(200))