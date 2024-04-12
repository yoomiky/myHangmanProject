import pygame as pg
import random
pg.init()

screen = pg.display.set_mode((1080, 500))
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


def drawHangman():
    
    screen.blit(images[0], (50, 85))

    if guessedLetters == 1:
        screen.blit(images[1], (50, 85))
    elif guessedLetters == 2:
        screen.blit(images[2], (50, 85))
    elif guessedLetters == 3:
        screen.blit(images[3], (50, 85))
    elif guessedLetters == 4:
        screen.blit(images[4], (50, 85))
    elif guessedLetters == 5:
        screen.blit(images[5], (50, 85))
    elif guessedLetters == 6:
        screen.blit(images[6], (50, 85))
    
#def checkwin()
    


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
    #create the checkWin()

    pg.display.update()
pg.quit()

