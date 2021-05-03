import random

choix = ["pierre", "ciseaux", "feuille"]
scoremax = 3
score = 0
botscore = 0

def computer():
    return random.choice(choix)

def checkplay():
    move = ""
    while move not in choix:
        move = str(input("pierre, feuille, ciseaux-> "))
    return move

def fight():
    move = checkplay()
    bot_move = computer()
    if bot_move == "pierre":
        if move == "pierre":
            print("pierre contre pierre")
            return "draw"
        elif move == "ciseaux":
            print("defaite, pierre bat ciseaux")
            return "defaite"
        elif move == "feuille":
            print("victoire, feuille recouvre pierre")
            return "victoire"
    if bot_move == "feuille":
        if move == "pierre":
            print("defaite, feuille recouvre pierre")
            return "defaite"
        elif move == "ciseaux":
            print("victoire, ciseaux coupe feuille")
            return "victoire"
        elif move == "feuille":
            print("feuille contre feuille")
            return "draw"
    if bot_move == "ciseaux":
        if move == "pierre":
            print("victoire, pierre bat ciseaux")
            return "victoire"
        elif move == "ciseaux":
            print("ciseaux contre ciseaux")
            return "draw"
        elif move == "feuille":
            print("defaite, ciseaux coupe feuille")
            return "defaite"


while score < scoremax or botscore < scoremax:
    partie = fight()
    if partie == "defaite":
        botscore += 1
    elif partie == "victoire":
        score += 1
    
    print("Le premier a 3 gagne.\nVous: ", score, "\nBot: ", botscore)
    if score == scoremax:
        print("Bravo")
        break
    elif botscore == scoremax:
        print("Defaite")
        break

