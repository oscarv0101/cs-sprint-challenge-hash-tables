#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # hash table to store route's airport source and destination info
    cache = {}
    # initialize route array, next we need to add the original source airport
    route = [None] * length

    # iterate thru each ticket and store its destination in the ht
    for t in tickets:
        cache[t.source] = t.destination

    # first ticket along the route has NONE source, so we start there
    dest = cache["NONE"]

    # next we find each ticket's next destination and add it to the destinations array
    # flight is current ticket
    for flight in range(length):
        # record value of next destination
        route[flight] = dest
        # the next destination is the value in the ht, the key is the destination just added to the array 
        # aka the next flight in the trip
        # continue until complete
        dest = cache[dest]
    return route
