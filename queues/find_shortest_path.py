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

        
        
        

end: 'New York'

sp('Seattle')       // shortestPath: 1
  sp('Dallas')      // shortestPath: Infinity
    sp('Detroit')  => null

*/


const shortestFlightPath = (start, end) => {
  if (start === end) {
    return 0;
  }
  if (!flights[start]) {
    return null;
  }

  let shortestPath = Infinity;
  flights[start].forEach((possibleDest) => {
    const shortestPathFromDest = shortestFlightPath(possibleDest, end);
    if (shortestPathFromDest !== null) {
      shortestPath = Math.min(shortestPath, shortestPathFromDest)
    }
  });

  return shortestPath === Infinity ? null : shortestPath + 1;
}

console.log(shortestFlightPath('Seattle', 'New York'))


const flights = {
  'Seattle': ['Boston', 'Austin', 'Portland', 'Dallas'],
  'Dallas': ['Detroit'],
  'Austin': ['Raleigh', 'DC'],
  'Boston' : ['Milwaukee']
}
