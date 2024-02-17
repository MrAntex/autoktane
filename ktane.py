import keyboard

from data_ktane import *

state = -1
layers = 0

def echap():
    if state == 0: exit()
    else:
        mainMenu()

keyboard.add_hotkey("esc", echap)

def isSerieImpair(s):
    for n in range(len(s)-1, -1, -1):
        if s[n] in chiffres:
            return int(s[n])%2 != 0
    return False

def setup():
    print("= = Setup = =")
    global serie
    global impair
    global isVoyelle
    serie = input("Numéro de série : ").upper()
    impair = isSerieImpair(serie)
    isVoyelle = any(char in voyelles for char in serie)

    global piles
    piles = int(input("Nombre de piles : "))

    global parallele
    parallele = input("Port parallèle ? ").upper() == "O"

    global frk
    frk = input("FRK ? ").upper() == "O"
    global car
    car = input("CAR ? ").upper() == "O"

    print("= =")
    global mistakes
    mistakes = 0
    state = 0
    mainMenu()

def mainMenu():
    state = 0
    print("= = Main menu = =")
    if layers > 0: print("[", layers, "LAYER(S) DEEP]")
    print("Série : ", serie, " | ", piles, " pile(s) | ", mistakes, " erreur(s)")
    print("1. Fils Normaux")
    print("2. Bouton")
    print("3. Simon")
    print("4. Jeu de mots (6 mots)")
    print("5. Memory")
    print("6. Morse")
    print("7. Mot de passe (Rouleaux de lettres)")
    print("8. Fils compliqués")
    print("9. Séquence de fils")
    print("10. Labyrinthe")
    print("M. Ajout erreur /!\\")
    print("Esc. Exit")
    
    print("= =")

    match input("Option : "):
        case "1":
            state = 1
            fils()
        case "2":
            state = 2
            bouton()
        case "3":
            state = 3
            simon()
        case "4":
            state = 4
            jdm()
        case "5":
            state = 5
            memory()
        case "6":
            state = 6
            morse()
        case "7":
            state = 7
            password()
        case "8":
            state = 8
            complique()
        case "9":
            state = 9
            sequence()
        case "10":
            state = 10
            labyrinthe()
        case "M":   
            mistakes+=1
            print("Erreur ajoutée. ", mistakes, " erreur(s) au total.")
            mainMenu()
        case _:
            print("Mauvaise option")
            mainMenu()



def fils():
    print("= = Fils Normaux = =")
    print("/!\\ R = ROUGE\n    B = BLEU\n    L = BLANC\n    J = JAUNE\n")

    fils = input("Fils : ").upper()
    toCut = 0

    match(len(fils)):
        case 3:
            if 'R' not in fils:
                toCut = 2
            elif fils[-1] == 'L':
                toCut = 3
            elif fils.count("B") > 1:
                toCut = fils.rfind("B")+1
            else:
                toCut = len(fils)
            pass
        case 4:
            if fils.count("R") > 1 and impair:
                toCut = fils.rfind("R")+1
            elif (fils[-1] == "J" and fils.count("R") == 0) or fils.count("B") == 1:
                toCut = 1
            elif fils.count("J") > 1:
                toCut = len(fils)
            else:
                toCut = 2
            pass
        case 5:
            if fils[-1] == "N" and impair:
                toCut = 4
            elif fils.count("R") == 1 and fils.count("J") > 1:
                toCut = 1
            elif fils.count("N") == 0:
                toCut = 2
            else:
                toCut = 1
            pass
        case 6:
            if fils.count("J") == 0 and impair:
                toCut = 3
            elif fils.count("J") == 1 and fils.count("L") > 1:
                toCut = 4
            elif fils.count("R") == 0:
                toCut = len(fils)
            else:
                toCut = 4
            pass

    print("Couper le fil n°", toCut)
    mainMenu()


def bouton():
    print("= = Bouton = =")
    print("/!\\ R = ROUGE\n    B = BLEU\n    L = BLANC\n    J = JAUNE\n")
    bouton = ""

    while len(bouton) != 2:
        bouton = input("Bouton : ").upper()

    if (piles > 1 and "E" in bouton) or (piles > 2 and frk) or bouton == "RM" or bouton == "MR":
        print("Appuyer et relâcher")
    else:
        print("Maintenir...")
        coul = ""
        while len(coul) != 1:
            coul = input("Couleur ? ").upper()[0]

        match(coul):
            case "B":
                print("Relâcher quand il y a un 4")
            case "J":
                print("Relâcher quand il y a un 5")
            case _:
                print("Relâcher quand il y a un 1")


def simon():
    suiteCoul = ""
    suiteReps = ""
    i = 0

    while True:
        newCoul = input("Input : " + suiteCoul).upper()
        if newCoul.upper() == "Q": break
        if newCoul == "":
            break
        suiteCoul += newCoul
        dic = correspVoyelleSimon if isVoyelle else correspNoVoyelleSimon
        suiteReps += dic[mistakes][listeBaseSimon.index(newCoul)] + " "
        print(suiteReps)


def jdm():
    print("= = Jeu de mots = =")
    while True:
        got = input("Mot affiché : ").upper()
        if got == "": break
        while got not in emplacementsALireJDM:
            got = input("Pas trouvé :/ Mot affiché : ").upper()
        
        emplacement = emplacementsALireJDM[got]
        deuxiemeMot = input(str(emplacement) + ("er" if emplacement == 1 else "eme") + " mot : ").upper()
        while deuxiemeMot not in listeMotsJDM:
            deuxiemeMot = input("Pas trouvé :/ " + str(emplacement) + ("er" if emplacement == 1 else "eme") + " mot : ").upper()

        for s in [0,7]:
            for i in range(7):
                print(listeMotsJDM[deuxiemeMot][s+i])
            input("")


def memory():

    suiteChiffres = []
    suitePositions = []

    for step in range(5):
    
        print(suitePositions)
        print(suiteChiffres)
        
        displayed = int(input("Numéro affiché : "))
        
        while displayed > 4 or displayed < 1:
            displayed = int(input("Mauvais numéro :/ Numéro affiché : "))
        
        action = instructionsMem[step][displayed]
        if action.upper() == action:
            aFaire = action
        else:
            if action[0] == "n": return "N" + str(suiteChiffres[int(action[1])-1])
            else: aFaire = "P" + str(suitePositions[int(action[1])-1])

        if aFaire[0] == "P":
            newChiffre = int(input("Appuyer sur le bouton en POSITION " + aFaire[1] + ". Dessus il y a le NUMÉRO : "))
            suiteChiffres.append(newChiffre)
            suitePositions.append(aFaire[1])
        else:
            newPos = int(input("Appuyer sur le bouton avec le NUMÉRO " + aFaire[1] + ". Il est en POSITION : "))
            suitePositions.append(newPos)
            suiteChiffres.append(aFaire[1])


def morse():
    print("= = Morse = =")
    print("Lettres : ")
    word = []

    for c in range(5):
        char = input()
        while char not in alphabetMorse:
            char = input("Mauvais caractère : ")
        word.append(alphabetMorse[char])
        print("".join(word))

    print("".join(word)," => ", frequencesMorse["".join(word)])


def password():
    toSuppr = []
    lettres = []
    for l in range(5):
        suite = input().upper()
        lettres.append([])
        lettres[l].append(suite)
        for w in wordsMdp:
            if w[l] not in suite:
                toSuppr.append(w)
        for sup in toSuppr:
            wordsMdp.remove(sup)
        toSuppr = []
        print(wordsMdp)
        if len(wordsMdp) <= 1:
            break


def complique():
    print("= = Fils compliqués = =")
    while True:
        combinaison = input("Combinaison : ")
        if combinaison == "": break
        score = 0
        doitCouper = False

        for c in combinaison:
            score += scoreCaracteristiquesCompl[c]

        match instructionsCompl[score]:
            case "C":
                doitCouper = True
            case "N":
                doitCouper = False
            case "S":
                doitCouper = not impair
            case "P":
                doitCouper = parallele
            case "B":
                doitCouper = (piles >= 2)

        print(("Couper " if doitCouper else "Ne PAS couper ") + "le fil.")


def sequence():
    print("= = Séquence de fils = =")
    nbFils = {"R": 0, "B": 0, "N": 0}

    while True:
        fil = input("Fil : ").upper()
        if fil == "": break
        if fil[1] in apparitionsSeq[fil[0]][nbFils[fil[0]]]:
            print("Coupe le fil")
        else:
            print("Ne PAS couper le fil.")
        nbFils[fil[0]] += 1
        

def labyrinthe():
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


if __name__ == '__main__':
    setup()


