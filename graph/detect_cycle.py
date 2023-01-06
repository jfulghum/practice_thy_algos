def detect_cycle(adjacency_list, visited, path_taken, curr_course):
    if curr_course in visited:
        return False
    if curr_course in path_taken:
        return True

    path_taken.add(curr_course)
    neighbor_courses = adjacency_list[curr_course]
    for neighbor_course in neighbor_courses:
        if detect_cycle(adjacency_list, visited, path_taken, neighbor_course):
            return True
        
    visited.add(curr_course)
    path_taken.remove(curr_course)
    return False

def build_adjacency_list(num_courses, prerequisites):
    output = dict()
    for course in range(num_courses):
        output[course] = []
        
    for course, required_course in prerequisites:
        output[course].append(required_course)
    return output

def can_finish(num_courses, prerequisites):
    adjacency_list = build_adjacency_list(num_courses, prerequisites)
    visited = set()
    for course in adjacency_list.keys():
        if course not in visited:
            has_cycle = detect_cycle(adjacency_list, visited, set(), course)
            if has_cycle:
                return False
    return True
