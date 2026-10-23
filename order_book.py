from collections import defaultdict
import heapq

class OrderBook:
    # """A simplified limit order book.
    # Bids: Max-heap (highest price has priority)
    # Asks: Min-heap (lowest price has priority)
