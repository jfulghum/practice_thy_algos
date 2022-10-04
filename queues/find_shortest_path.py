from collections import queue
visited = set()

flights = {"Seattle": "Boston", "Austin",
        "Austin": "New York"} 
start = "Seattle"
end = "New York"
output = 2 


def find_shortest_path(flights, start, end):
  
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
