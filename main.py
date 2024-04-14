import pygame as pg
import random
pg.init()

screen = pg.display.set_mode((800, 500))
pg.display.set_caption("Hangman")

images = []

guessedLetters = []
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



run = True
while run:
    
    screen.fill((255, 255, 255))

    for event in pg.event.get():

        if event.type == pg.QUIT:
            run = False
        
        if guessedLetterCounter >= 6:
            print("Congratulations, you failed to guess the word",randomChoice,".")
            run = False
        elif guessedLetterCounter <= 6 and guessedLetters == guessedWord:
            print("Congrats! You successfully guessed the word,",randomChoice,".")
            run = False
        
        if event.type == pg.KEYUP:
            key = event.unicode.lower()
            print(f'{key} pressed')
            
            if key in guessedLetters:
                print("You already guessed that letter")
            else:
                guessedLetters.append(key)
                if key not in randomChoice:
                    guessedLetterCounter += 1
                    print("Incorrect guess!")

        #mouse = pg.mouse.get_pos()
        #print(mouse)

    importImages()
    drawHangman()
    
    pg.display.update()
pg.quit()

