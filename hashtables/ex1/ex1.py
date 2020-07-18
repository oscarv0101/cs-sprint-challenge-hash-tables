def get_indices_of_item_weights(weights, length, limit):
    # create cache
    cache = {}
    # fail if input array is shorter than 2 entries (test case 1)
    if length <= 1:
        print("Error: List too short.")
        return None

    for i in range(length):
        current = weights[i]
         # check if the current weight is in the cache
        if current in cache:
            # prev weight index = value, so get index of prev
            previous = cache[current]
            # print(cache)
            return (i, previous)
        # now the hash table/cache key is the smaller weight needed to reach limit
        cache[limit - weights[i]] = i

    return None
weights = [4, 6, 10, 15, 16]
print(get_indices_of_item_weights(weights, 5, 21)) 