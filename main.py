import pygame as pg
import random
pg.init()


screen = pg.display.set_mode((800, 500))
pg.display.set_caption("Hangman")



#Colors
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

font = pg.font.SysFont(None, 38)
text = font.render("text", False, blue)

images = []

guessedWord = []

words = ["banana", "merchant", "fund", "past", "quote", "fever", "mine", "principle", "stem", "mastermind", "main", "captivate", "judgement", "aluminum", 
         "generation", "pilot", "competition", "exceed", "bracket", "seperation", "outlet", "steep", "sleep", "imagine", "sight", "redundancy", "gun", "abdundant",
         "hierarchy", "place", "inside", "home", "insure", "detective", "hole", "agriculture", "dialouge", "recruit", "willpower", "sacrifice", "moving", 
         "bang", "quotation", "path", "mourning", "tight", "operational", "hill", "cabin", "wrestle", "peace"]

randomChoice = random.choice(words)
guessedWord.extend(randomChoice)
print(randomChoice)
        


def importImages():
    for i in range(7):
        img = pg.image.load(f'images/hangman{i}.png')
        images.append(img)

importImages()
background_img = pg.image.load(f'images/menu.png')


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


def winCondition():

    if guessedLetterCounter >= 6:
        print("Congratulations, you failed to guess the word", randomChoice, ".")
        pg.quit()
        exit()

    elif len(guessedWord) == 0:
        print("Congratulations! You successfully guessed the word", randomChoice, ".")
        pg.quit()
        exit()



run = True
while run:
    
    screen.blit(background_img, (0, 0))

    for event in pg.event.get():

        if event.type == pg.QUIT:
            run = False
        
        if event.type == pg.KEYDOWN:
            key = event.unicode.lower()
            print(f'{key} pressed')

            if event.key == pg.K_SPACE:
                screen.fill(white)
                drawHangman()
                
            if key in guessedWord:
                guessedWord.remove(key)
                print("Correct guess!")
            else:
                print("Incorrect guess")
                guessedLetterCounter += 1
        
              

        #mouse = pg.mouse.get_pos()
        #print(mouse)

    
    winCondition()
    pg.display.update()
pg.quit()