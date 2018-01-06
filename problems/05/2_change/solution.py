def grd_change(coins, change):
    n = 0
    for coin in sorted(coins, reverse=True):
        while change >= coin:
            change -= coin
            n += 1
    return -1 if change else n
