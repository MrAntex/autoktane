chiffres = "0123456789"
voyelles = ['A', 'E', 'I', 'O', 'U', 'Y']

# SIMON #
correspVoyelleSimon = [["Bleu", "Rouge", "Jaune", "Vert"],["Jaune", "Vert", "Bleu", "Rouge"],["Vert", "Rouge", "Jaune", "Bleu"]]

correspNoVoyelleSimon = [["Bleu", "Jaune", "Vert", "Rouge"],["Rouge", "Bleu", "Jaune", "Vert"],["Jaune", "Vert", "Bleu", "Rouge"]]

listeBaseSimon = "RBVJ"

# JDM #
emplacementsALireJDM = {"OUI": 3, "PREMIER": 2, "VERRE": 6,
                     "OK": 2, "MOTS": 6, "RIEN": 3,
                     "": 5, "VIDE": 4, "NON": 6, "MOT": 3,
                     "MAUX": 6, "BOUGE": 4, "ROUGE": 4,
                     "AU": 5, "EAU": 5, "ATTENDS": 6, "TES": 4,
                     "T'ES": 6, "TON": 4, "TONS": 4, "THON": 1,
                     "TU ES": 6, "HAUT": 5, "VERS": 4, "VERT": 3,
                     "C'EST": 6, "C": 2, "VER": 6}

listeMotsJDM = {"PRÊT":["OUI", "E", "EUX", "MILIEU", "GAUCHE", "APPUIE", "DROITE", "VIDE", "PRÊT", "NON", "PREMIER", "EUHHH", "RIEN", "ATTENDS"],
             "PREMIER":["GAUCHE", "E", "OUI", "MILIEU", "NON", "DROITE", "RIEN", "EUHHH", "ATTENDS", "PRÊT", "VIDE", "EUX", "APPUIE", "PREMIER"],
"NON":["VIDE", "EUHHH", "ATTENDS", "PREMIER", "EUX", "PRÊT", "DROITE", "OUI", "RIEN", "GAUCHE", "APPUIE", "E", "NON", "MILIEU"],
"VIDE":["ATTENDS", "DROITE", "E", "MILIEU", "VIDE", "APPUIE", "PRÊT", "RIEN", "NON", "EUX", "GAUCHE", "EUHHH", "OUI", "PREMIER"],
"RIEN":["EUHHH", "DROITE", "E", "MILIEU", "OUI", "VIDE", "NON", "APPUIE", "GAUCHE", "EUX", "ATTENDS", "PREMIER", "RIEN", "PRÊT"],
"OUI":["E", "DROITE", "EUHHH", "MILIEU", "PREMIER", "EUX", "APPUIE", "PRÊT", "RIEN", "OUI", "GAUCHE", "VIDE", "NON", "ATTENDS"],
"EUX":["EUHHH", "EUX", "GAUCHE", "RIEN", "PRÊT", "VIDE", "MILIEU", "NON", "E", "PREMIER", "ATTENDS", "OUI", "APPUIE", "DROITE"],
"EUHHH":["PRÊT", "RIEN", "GAUCHE", "EUX", "E", "OUI", "DROITE", "NON", "APPUIE", "VIDE", "EUHHH", "MILIEU", "ATTENDS", "PREMIER"],
"GAUCHE":["DROITE", "GAUCHE", "PREMIER", "NON", "MILIEU", "OUI", "VIDE", "EUX", "EUHHH", "ATTENDS", "APPUIE", "PRÊT", "E", "RIEN"],
"DROITE":["OUI", "RIEN", "PRÊT", "APPUIE", "NON", "ATTENDS", "EUX", "DROITE", "MILIEU", "GAUCHE", "EUHHH", "VIDE", "E", "PREMIER"],
"MILIEU":["VIDE", "PRÊT", "E", "EUX", "RIEN", "APPUIE", "NON", "ATTENDS", "GAUCHE", "MILIEU", "DROITE", "PREMIER", "EUHHH", "OUI"],
"E":["MILIEU", "NON", "PREMIER", "OUI", "EUHHH", "RIEN", "ATTENDS", "E", "GAUCHE", "PRÊT", "VIDE", "APPUIE", "EUX", "DROITE"],
"ATTENDS":["EUHHH", "NON", "VIDE", "E", "OUI", "GAUCHE", "PREMIER", "APPUIE", "EUX", "ATTENDS", "RIEN", "PRÊT", "DROITE", "MILIEU"],
"APPUIE":["DROITE", "MILIEU", "OUI", "PRÊT", "APPUIE", "E", "RIEN", "EUHHH", "VIDE", "GAUCHE", "PREMIER", "EUX", "NON", "ATTENDS"],
"TOI":["OK", "THON", "TON", "TONS", "SUIVANT", "AVANT", "T'ES", "MAINTIENS", "QUOI ?", "TOI", "QUOI", "COMME", "FAIT", "TES"],
"THON":["TON", "SUIVANT", "COMME", "AVANT", "QUOI ?", "FAIT", "QUOI", "MAINTIENS", "TOI", "TES", "TONS", "OK", "T'ES", "THON"],
"TON":["QUOI", "THON", "AVANT", "TON", "SUIVANT", "T'ES", "OK", "TES", "TONS", "TOI", "QUOI ?", "MAINTIENS", "COMME", "FAIT"],
"TONS":["TOI", "TONS", "T'ES", "SUIVANT", "QUOI", "THON", "TES", "TON", "QUOI ?", "AVANT", "OK", "FAIT", "COMME", "MAINTIENS"],
"T'ES":["FAIT", "TES", "T'ES", "AVANT", "QUOI ?", "OK", "TON", "MAINTIENS", "TONS", "COMME", "SUIVANT", "QUOI", "THON", "TOI"],
"TES":["AVANT", "OK", "SUIVANT", "QUOI ?", "TONS", "T'ES", "QUOI", "FAIT", "TES", "TOI", "COMME", "MAINTIENS", "THON", "TON"],
"AVANT":["AVANT", "TON", "THON", "TOI", "FAIT", "MAINTIENS", "QUOI", "SUIVANT", "OK", "COMME", "TONS", "T'ES", "TES", "QUOI ?"],
"QUOI":["T'ES", "TES", "THON", "TONS", "SUIVANT", "QUOI", "FAIT", "TOI", "AVANT", "COMME", "TON", "OK", "MAINTIENS", "QUOI ?"],
"QUOI ?":["TOI", "MAINTIENS", "TONS", "TON", "TES", "FAIT", "QUOI", "COMME", "THON", "AVANT", "T'ES", "SUIVANT", "QUOI ?", "OK"],
"FAIT":["OK", "AVANT", "SUIVANT", "QUOI ?", "TON", "T'ES", "TONS", "MAINTIENS", "COMME", "TOI", "TES", "THON", "QUOI", "FAIT"],
"SUIVANT":["QUOI ?", "AVANT", "QUOI", "TON", "MAINTIENS", "OK", "SUIVANT", "COMME", "FAIT", "THON", "T'ES", "TONS", "TES", "TOI"],
"MAINTIENS":["THON", "TES", "FAIT", "QUOI", "TOI", "T'ES", "OK", "QUOI ?", "TONS", "SUIVANT", "MAINTIENS", "AVANT", "TON", "COMME"],
"OK":["THON", "FAIT", "COMME", "TONS", "TOI", "MAINTIENS", "AVANT", "T'ES", "OK", "TES", "QUOI ?", "SUIVANT", "TON", "QUOI"],
"COMME":["TONS", "SUIVANT", "TES", "T'ES", "MAINTIENS", "FAIT", "QUOI", "QUOI ?", "AVANT", "TOI", "COMME", "OK", "THON", "TON"]}

# MEMORY #
instructionsMem = [{1: "P2", 2: "P2", 3: "P3", 4: "P4"},
                {1: "N4", 2: "p1", 3: "P1", 4: "p1"},
                {1: "n2", 2: "n1", 3: "P3", 4: "N4"}, 
                {1: "p1", 2: "P1", 3: "p2", 4: "p2"},
                {1: "n1", 2: "n2", 3: "n4", 4: "n3"}]

# MORSE #
alphabetMorse = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
                 "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
                 "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
                 ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
                 "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z"}

frequencesMorse = {"VITRE": 3.505, "VILLE": 3.515, "CHOSE": 3.522, "SIGNE": 3.532,
                    "LINGE": 3.535, "LIGNE": 3.542, "CHAMP": 3.545, "LITRE": 3.552,
                    "PHASE": 3.555, "CHAUD": 3.565, "BILLE": 3.572, "BALLE": 3.575,
                    "SINGE": 3.582, "PLUME": 3.592, "PLUIE": 3.595, "SALLE": 3.600}

# MDP #
wordsMdp = ["ABATS", "ABIME", "ABOIS", "ADIEU", "DELTA",
         "DENSE", "DEVIN", "DIVIN", "DRAME", "DROIT",
         "ENVOL", "ENVIE", "ENVOI", "ERRES", "ESSAI",
         "FLEUR", "FINIT", "FIOLE", "KILOS", "LITRE",
         "LIVRE", "MASSE", "MATCH", "MATIN", "MAUVE",
         "POSER", "PORTS", "POULE", "SALIR", "TAIRE",
         "TARIF", "TASSE", "VALVE", "VANNE", "VENTE"]

# FILS COMPLIQUES #
scoreCaracteristiquesCompl = {"R": 1, "B": 2, "E": 4, "L": 8}

instructionsCompl = ["C", "S", "S", "S", "C", "C",
                     "N", "P", "N", "B", "P",
                     "S", "B", "B", "P", "N"]

apparitionsSeq = {"R": ["C", "B", "A", "AC", "B", "AC", "ABC", "AB", "B"],
                  "B": ["B", "AC", "B", "A", "B", "BC", "C", "AC", "A"],
                  "N": ["ABC", "AC", "B", "AC", "B", "BC", "AB", "C", "C"]}

# LABYRINTHE #
canWalk = {0: [1,0,1,1], 1:[0,1,1,1], 2:[1,1,1,0], 3:[1,1,0,1],
           4:[0,0,1,1], 5:[0,1,1,0], 6:[1,1,0,0], 7:[1,0,0,1],
           8:[0,1,0,1], 9:[1,0,1,0], 10:[0,0,1,0], 11:[0,1,0,0],
           12:[1,0,0,0], 13:[0,0,0,1]}

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

