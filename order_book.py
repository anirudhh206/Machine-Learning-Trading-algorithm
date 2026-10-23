from collections import defaultdict
import heapq

class OrderBook:
    # """A simplified limit order book.
    # Bids: Max-heap (highest price has priority)
    # Asks: Min-heap (lowest price has priority)
    def __init__(self):
        self.bids = []
        self.asks = []
        self.timestamp = 0
        self.order_map = defaultdict(list)
        self.tradehistory = []
