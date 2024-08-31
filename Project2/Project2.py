import sys
from collections import deque

def computePath(graph, possible_edges, dir_map, row,col):
    current_node = (row-1, col-1) # bulls eye
    path = []
    while current_node != (0,0):
        prev_node = possible_edges[current_node]
        if not prev_node:
            break
        path.append((prev_node, current_node)) #adding all the edges from bulls eye to source (0,0) to obtain a successful path
        current_node = prev_node
    result = []
    for pn,cn in path[::-1]:  # We use this loop to calculate the magnitude and directions and store in result array
        diff = cn[0]-pn[0], cn[1]-pn[1]
        if diff[0] == 0: #they are in the same row, Covers E and W
            if diff[1] > 0:
                dir = 'E'
            else:
                dir =  'W'
            scalar = abs(diff[1]) #only row-wise move
        elif diff[1] == 0: # they are in the same col, covers S and N
            if diff[0] > 0:
                dir = 'S'
            else:
                dir = 'N'
            scalar = abs(diff[0]) #only col-wise move
        else: #Covers NE, NW, SE, SW
            if diff[0] > 0:
                if diff[1] > 0:
                    dir = 'SE'
                else:
                    dir = 'SW'
            else:
                if diff[1] > 0:
                    dir = 'NE'
                else:
                    dir = 'NW'
            scalar = abs(diff[0]) #diagonal
        result.append(f'{scalar}{dir}')
    return result

#this dict is used for recording the direction values to move.
dir_map = {'N': (-1, 0), 'E': (0, 1), 
       'S': (1, 0), 'W': (0, -1),
       'NE': (-1, 1), 'SE': (1, 1), 
       'SW': (1, -1), 'NW': (-1, -1)}

possible_edges = {}

input_file = sys.argv[1]
output_file = sys.argv[2]
with open(input_file, 'r') as inp_f:
    lines = inp_f.readlines()
    r,c = map(int, lines[0].split())
    graph = [line.split() for line in lines[1:]]
    visit_array = [[False for __ in range(c)] for _ in range(r)]

que = deque()
#Start at (0,0)
que.append((0,0))
visit_array[0][0] = True

#Breadth First Search - We check with the length of the queue
while len(que) > 0:
    current_r,current_c = que.popleft()
    value = graph[current_r][current_c]
    #Once we reach the bulls eye
    if value == 'O' :
        success_path = computePath(graph, possible_edges,dir_map,r,c)
        success_path = ' '.join(success_path) # converting list to string
        with open(output_file, 'w') as out_f:
            out_f.write(success_path)
        break
    color = value[0]
    dir = value[2:]

    dim_r, dim_c = dir_map[dir]
    new_r, new_c = current_r + dim_r , current_c + dim_c
    while 0 <= new_r < r and 0 <= new_c < c:
        if graph[new_r][new_c][0]!= color and visit_array[new_r][new_c] == False:
            visit_array[new_r][new_c] = True
            que.append((new_r, new_c))
            possible_edges[(new_r,new_c)] = (current_r,current_c) #getting all the possible edges
        new_r=new_r+dim_r
        new_c=new_c+dim_c




