# https://leetcode.com/problems/campus-bikes/
class Solution:
    def assignBikes(self, workers, bikes):
        def find_distance(worker_loc, bike_loc):
            return abs(worker_loc[0] - bike_loc[0]) + abs(worker_loc[1] - bike_loc[1])
        
        # Calculate the distance between each worker and bike.
        all_triplets = []
        for worker, worker_loc in enumerate(workers):
            for bike, bike_loc in enumerate(bikes):
                distance = find_distance(worker_loc, bike_loc)
                all_triplets.append((distance, worker, bike))
    
        
        # Sort the triplets. By default, sorting will prioritize the
        # tuple's first value, then second value, and finally the third value
        all_triplets.sort()
        
        # Initialize all values to False, to signify no bikes have been taken
        bike_status = [False] * len(bikes)
        # Initialize all values to -1, to signify no worker has a bike
        worker_status = [-1] * len(workers)
        # Keep track of how many worker-bike pairs have been made
        pair_count = 0
        
        for distance, worker, bike in all_triplets:
            # If both worker and bike are free, assign the bike to
            # the worker and mark the bike as taken
            if worker_status[worker] == -1 and not bike_status[bike]:
                bike_status[bike] = True
                worker_status[worker] = bike
                pair_count += 1
                
                # If all the workers have the bike assigned, we can stop
                if pair_count == len(workers):
                    return worker_status
        
        return worker_status


workers = [[0,0],[1,1],[2,0]]
bikes = [[1,0],[2,2],[2,1]]

print(Solution().assignBikes(workers, bikes))
# Output: [0,2,1]

# HEAP
# If there are multiple (workeri, bikej) pairs with the same shortest Manhattan distance, we choose the pair with the smallest worker index. If there are multiple ways to do that, we choose the pair with the smallest bike index. Repeat this process until there are no available workers
import heapq

class Solution:
    def assignBikes(self, workers, bikes):
        
        def find_distance(worker_loc, bike_loc):
            return abs(worker_loc[0] - bike_loc[0]) + abs(worker_loc[1] - bike_loc[1])
        
        # List of triplets (distance, worker index, bike index) for each worker-bike combination
        worker_to_bike_list = []
        pq = []
        
        for worker, worker_loc in enumerate(workers):
            curr_worker_pairs = []
            for bike, bike_loc in enumerate(bikes):
                distance = find_distance(worker_loc, bike_loc)
                curr_worker_pairs.append((distance, worker, bike))
            
            # Sort the worker_to_bike_list for the current worker in reverse order
            curr_worker_pairs.sort(reverse=True)
            # Add the closest bike for this worker to the priority queue
            heapq.heappush(pq, curr_worker_pairs.pop())
            
            # Store the remaining options for the current worker in worker_to_bike_list
            worker_to_bike_list.append(curr_worker_pairs)
            
        # Initialize all values to false, to signify no bikes have been taken
        bike_status = [False] * len(bikes)
        # Initialize all values to -1, to signify no worker has a bike
        worker_status = [-1] * len(workers)
        count = 0
        while pq:
            # Pop the worker-bike pair with smallest distance
            count += 1

            distance, worker, bike = heapq.heappop(pq)
            print("bike", bike)
            if not bike_status[bike]:
                # If the bike is free, assign the bike to the worker
                bike_status[bike] = True
                worker_status[worker] = bike
            else:
                # Otherwise, add the next closest bike for the current worker to the priority queue
                print(worker_to_bike_list)
                print(worker)
                next_closest_bike = worker_to_bike_list[worker].pop()
                heapq.heappush(pq, next_closest_bike)
        
        return worker_status
