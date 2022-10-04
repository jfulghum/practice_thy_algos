from collections import queue
visited = set()

def possible_vacations(flights):
  visited = set()
  queue = deque()

  output: Dict[str, int] = {}

  distance = 0
  queue.append((start, distance))
  while queue:
    city, distance = queue.popleft()
    for cityName in flights[city]:
      if cityName not in visited:
        queue.append(cityName, )
