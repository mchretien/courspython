import random
import requests

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
words = response.content.splitlines()
trashword = random.choice(words)
word = trashword.decode("utf-8") 
print("It's a ", len(word), " letters word")

c = len(word)
i = 0
j = 0
letters = []
while i < 7:
    guess = str(input("Guess a letter:-> "))
    if guess not in list(word):
        print("Soon to be dead, chances left: ", 5-i)
        i += 1
    else:
        j += 1
        letters.append(guess)
        if j == c:
            print("You've found the word, it was ", word, ", bravo")
            break
        else:    
            print("Wp, keep winning, you have the letters: ", letters)
        
    if i == 6:
        print("Game over, you were hanged ")
        break
