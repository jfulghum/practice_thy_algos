class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        destinations = collections.defaultdict(list)
        for s, d, cost in flights:
            destinations[s].append([d, cost])
        
        min_distance = float('inf')
        cost_to_destination = collections.defaultdict(int)
        queue = collections.deque()
        queue.append([src, 0])
        stops = 0
        
        while queue and stops <= K:
            for _ in range(len(queue)):
                current, current_cost = queue.popleft()
                for destination, cost in destinations[current]:
                    if destination in cost_to_destination and current_cost + cost > cost_to_destination[destination]:
                        continue
                    cost_to_destination[destination] = current_cost + cost
                    if destination == dst:
                        min_distance = min(min_distance, current_cost + cost)
                        continue
                    queue.append([destination, current_cost + cost])
            stops += 1
        
        return min_distance if min_distance != float('inf') else -1


# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         prices = [float('inf')] * n
#         prices[src] = 0
#         for _ in range(k+1):
#             temp = prices[:]
#             for current, destination, price in flights:
#                 if prices[current] == float('inf'):
#                     continue
#                 if prices[current] + price < temp[destination]:
#                     temp[destination] = prices[current] + price
#             prices = temp
#         return prices[dst] if prices[dst] != float('inf') else -1
