# List of coin denominations, descending for clarity
COINS = [50, 25, 10, 5, 1]

def count_change(amount, coins=COINS):
    if amount == 0:
        return 1  # One way to make change for 0: use nothing
    elif amount < 0 or not coins:
        return 0  # No way to make change
    else:
        # Count using the first coin at least once + not using it at all
        return count_change(amount, coins[1:]) + count_change(amount - coins[0], coins)

print(count_change(5))    # 2 → [5], [1,1,1,1,1]
print(count_change(10))   # 4
print(count_change(100))

def mcount_change(amount, coins=COINS, cache=None):
    if cache is None:
        cache = {}

    key = (amount, tuple(coins))
    if key in cache:
        return cache[key]

    if amount == 0:
        result = 1
    elif amount < 0 or not coins:
        result = 0
    else:
        result = count_change(amount, coins[1:], cache) + count_change(amount - coins[0], coins, cache)

    cache[key] = result
    return result


