canWalk = {0: [1,0,1,1], 1:[0,1,1,1], 2:[1,1,1,0], 3:[1,1,0,1],
           4:[0,0,1,1], 5:[0,1,1,0], 6:[1,1,0,0], 7:[1,0,0,1],
           8:[0,1,0,1], 9:[1,0,1,0], 10:[0,0,1,0], 11:[0,1,0,0],
           12:[1,0,0,0], 13:[0,0,0,1]}


class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None, type=None):
        self.parent = parent
        self.position = position
        self.type = type

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __str__(self) -> str:
        return str(self.position)+" ["+str(self.type)+"]"


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start, maze[start[0]][start[1]])
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end, maze[end[0]][end[1]])
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:
        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children
        children = []
        allDirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        availableDirs = []

        for p in range(4):
            if canWalk[current_node.type][p] == 1:
                availableDirs.append(allDirs[p])

        for new_position in availableDirs:  # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (
                    len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            """ if maze[node_position[0]][node_position[1]] == 0:
                continue """

            # Create new node
            new_node = Node(current_node, node_position, maze[node_position[0]][node_position[1]])

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:
            # Child is on the closed list
            if child in closed_list:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                        (child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


def main():

    mazes = [[[5, 8, 4, 5, 8, 13],
             [9, 5, 7, 6, 8, 4],
             [9, 6, 4, 5, 8, 0],
             [9, 11, 3, 7, 11, 0],
             [2, 8, 4, 5, 13, 9],
             [6, 13, 6, 7, 11, 7]],
             [[11, 1, 13, 5, 1, 13],
             [5, 7, 5, 7, 6, 4],
             [9, 5, 7, 5, 8, 0],
             [2, 7, 5, 7, 10, 9],
             [9, 10, 9, 5, 7, 9],
             [12, 6, 7, 6, 8, 7]],
             [[5, 8, 4, 9, 5, 4],
             [12, 10, 9, 6, 7, 9],
             [5, 0, 9, 5, 4, 9],
             [9, 9, 9, 9, 9, 9],
             [9, 6, 7, 9, 9, 9],
             [6, 8, 8, 7, 6, 7]],
             [[5, 4, 11, 8, 8, 4],
             [9, 9, 5, 8, 8, 0],
             [9, 6, 7, 5, 13, 9],
             [9, 11, 8, 3, 8, 0],
             [2, 8, 8, 8, 4, 9],
             [6, 8, 13, 11, 7, 12]],
             [[11, 8, 8, 8, 1, 4],
             [5, 8, 8, 1, 7, 12],
             [2, 4, 11, 7, 5, 4],
             [9, 6, 8, 4, 12, 9],
             [9, 5, 8, 3, 13, 9],
             [12, 6, 8, 8, 8, 7]],
             [[10, 5, 4, 11, 1, 4],
             [9, 9, 9, 5, 7, 9],
             [2, 7, 12, 9, 5, 7],
             [6, 4, 5, 0, 9, 10],
             [5, 7, 12, 9, 6, 0],
             [6, 8, 8, 7, 11, 7]],
             [[5, 8, 8, 4, 5, 4],
             [9, 5, 13, 6, 7, 9],
             [6, 7, 5, 13, 5, 7],
             [5, 4, 2, 8, 7, 10],
             [9, 12, 6, 8, 4, 9],
             [6, 8, 8, 8, 3, 7]],
             [[10, 5, 8, 4, 5, 4],
             [2, 3, 13, 6, 7, 9],
             [9, 5, 8, 8, 4, 9],
             [9, 6, 4, 11, 3, 7],
             [9, 10, 6, 8, 8, 13],
             [6, 3, 8, 8, 8, 13]],
             [[10, 5, 8, 8, 1, 4],
             [9, 9, 5, 13, 9, 9],
             [2, 3, 7, 5, 7, 9],
             [9, 10, 5, 7, 11, 0],
             [9, 9, 9, 5, 4, 12],
             [6, 7, 6, 7, 6, 13]]
             ]
    reperes = [[(0, 1), (5, 2)], [(1, 3), (4, 1)],
               [(3, 3), (5, 3)], [(0, 0), (0, 3)],
               [(4, 2), (3, 5)], [(2, 4), (4, 0)],
               [(1, 0), (1, 5)], [(3, 0), (2, 3)],
               [(0, 4), (2, 1)]]
    
    nMaze = None

    while nMaze == None:
        ptVert = input("Repere ? (x,y) ")
        for r in range(len(reperes)):
            if (int(ptVert[0]), int(ptVert[-1])) in reperes[r]:
                nMaze = r
                print("Found matching maze n°", r+1)
                break
        if nMaze == None: print("Green point not found.")
    
    

    startPt = input("White point (x,y) : ")
    start = (int(startPt[-1]), int(startPt[0]))

    endPt = input("Red triangle (x,y) : ")
    end = (int(endPt[-1]), int(endPt[0]))


    path = astar(mazes[nMaze], start, end)

    dirs = getDirectionsFromPath(path)
    print("Found path in", len(path)-1, "steps :\n")
    printMaze(mazes[nMaze], start, end, path, dirs)
    print()
    for d in dirs:
        _ = input(d)


def getDirectionsFromPath(path):
    directions = []
    for i in range(len(path)-1):
        diff = (path[i+1][0] - path[i][0], path[i+1][1] - path[i][1])
        match diff:
            case (0,1): # Droite
                directions.append("Droite")
            case (0,-1): # Gauche
                directions.append("Gauche")
            case (1, 0): # Bas
                directions.append("Bas")
            case (-1, 0): # Haut
                directions.append("Haut")
            case _:
                directions.append("?")
                pass
    
    return directions


def printMaze(maze, start, end, path, dirs):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if (i,j) == start:
                print('S', end='')
            elif (i,j) == end:
                print('E', end='')
            elif (i,j) in path:
                p = path.index((i,j))
                d = dirs[p]
                match d:
                    case "Droite":
                        print('>', end='')
                    case "Gauche":
                        print('<', end='')
                    case "Haut":
                        print('^', end='')
                    case "Bas":
                        print('v', end='')
                    case _:
                        print('+', end='')
            else:
                print('.', end='')
                    
        print()


if __name__ == '__main__':
    main()