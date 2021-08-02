def solution(commands):
    visited_paths = set()
    cur_position = (0, 0)
    DELTAS = {'U': (1, 0), 'D': (-1, 0), 'L': (0, -1), 'R': (0, 1)}
    
    for command in commands:
        dx, dy = DELTAS[command]
        next_position = (cur_position[0] + dx, cur_position[1] + dy)
        if not valid_coord(*next_position):
            continue
            
        visited_paths.add((cur_position, next_position))
        visited_paths.add((next_position, cur_position))
            
        cur_position = next_position
    
    return len(visited_paths) // 2

def valid_coord(x, y):
    return -5 <= x <= 5 and -5 <= y <= 5