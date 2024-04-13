import pygame as pg
import random
pg.init()

screen = pg.display.set_mode((800, 500))
pg.display.set_caption("Hangman")

images = []

guessedLetters = []

words = ["banana", "merchant", "fund", "past", "quote", "fever", "mine", "principle", "stem", "mastermind", "main", "captivate", "judgement", "aluminum", 
         "generation", "pilot", "competition", "exceed", "bracket", "seperation", "outlet", "steep", "sleep", "imagine", "sight", "redundancy", "gun", "abdundant",
         "hierarchy", "place", "inside", "home", "insure", "detective", "hole", "agriculture", "dialouge", "recruit", "willpower", "sacrifice", "moving", 
         "bang", "quotation", "path", "mourning", "tight", "operational", "hill", "cabin", "wrestle", "peace"]

randomChoice = random.choice(words)
        
def importImages():
    for i in range(7):
        img = pg.image.load(f'images/hangman{i}.png')
        images.append(img)

guessedLetterCounter = 0

def drawHangman():
    
    screen.blit(images[0], (50, 85))

    if guessedLetterCounter == 1:
        screen.blit(images[1], (50, 85))
    elif guessedLetterCounter == 2:
        screen.blit(images[2], (50, 85))
    elif guessedLetterCounter == 3:
        screen.blit(images[3], (50, 85))
    elif guessedLetterCounter == 4:
        screen.blit(images[4], (50, 85))
    elif guessedLetterCounter == 5:
        screen.blit(images[5], (50, 85))
    elif guessedLetterCounter == 6:
        screen.blit(images[6], (50, 85))
    
def checkWin():
    if guessedLetterCounter > 6:
        print("Congratulations! You failed to guess the word.")
    elif guessedLetterCounter < 6 and randomChoice:
        print("Congratulations! You successfully guessed the word", randomChoice, ".")

def guessLetter():
    while not checkWin():
        ask = input("Guess a letter: ").lower()
        if ask in guessedLetters:
            print("You already guessed that letter.")
        else:
            guessedLetters.append(ask)
            if ask not in randomChoice:
                guessedLetterCounter += 1
                print("Incorrect guess!")


run = True
while run:
    
    screen.fill((255, 255, 255))

    for event in pg.event.get():

        if event.type == pg.QUIT:
            run = False
        
        #mouse = pg.mouse.get_pos()
        #print(mouse)

    importImages()
    drawHangman()
    guessLetter()

    pg.display.update()
pg.quit()

