from random import randint

print("le juste prix")

price = randint(0, 1000)

guess = int(input("Devine le prix:-> "))

score = 100

while guess != price:
    if guess < price:
        guess = int(input("PLUS, réessaye-> "))
        score -= 10
    elif guess > price:
        score -= 10
        guess = int(input("MOINS, réessaye->"))
    
if guess == price:
    print("victoire, votre score est de: ", score, " sur 100")
