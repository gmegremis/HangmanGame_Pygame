import time
import random
import pygame
from pygame.constants import MOUSEBUTTONDOWN

# game colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (150, 150, 150)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# game window
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# globals
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 'L', "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letters_pos = []
circlesX = []
circlesY = []
word_list = [
    "DEVELOPER",
    "CPU",
    "PROGRAMMING",
    "DEBUGGING",
    "PYTHON",
    "HACKATHON",
    "PYGAME",
    "LINUX", 
    "KALI LINUX",
    "HTML",
    "JAVASCRIPT",
    "TESTING",
    "GOOGLE",
    "UBUNTU",
    "ALGORITHM",
    "SOFTWARE",
    "HARDWARE",
    "OBJECT",
    "CLASS"
]

# gallows images
images = []
for i in range(7):
    image = pygame.image.load(r"C:\Users\user\Desktop\Giorgos\Python\VScode\hangman\Assets\hangman" + str(i) + ".png")
    image = pygame.transform.scale(image, (300, 300))
    images.append(image)

def screen_setup():
    pygame.display.update()
    win.fill(WHITE)
    background = pygame.image.load(r"C:\Users\user\Desktop\Giorgos\Python\VScode\hangman\Assets\background.png")
    background = pygame.transform.scale(background, (800, 600))
    win.blit(background, (0, 0))
    win.blit(images[img_num], (50, 100))

def display_letters():
    pygame.font.init()
    font = pygame.font.SysFont("comicsans", 30)

    for x in range(50, 800, 60):
        for y in range(500, 600, 50):
            letters_pos.append((x-12, y-20))
            circlesX.append(x)
            circlesY.append(y)

    for i in range(26):
        if activate_ltrs[i] == True:
            pygame.draw.circle(win, BLACK, (circlesX[i], circlesY[i]), 20)
            pygame.draw.circle(win, GREY, (circlesX[i], circlesY[i]), 17)
            ltr = font.render(alphabet[i], 3, BLACK)
            win.blit(ltr, letters_pos[i])

def display_word(letter):
    pygame.font.init()
    font = pygame.font.SysFont("comicsans", 50)

    x = 350
    for i in range(len(word)):
        if word[i] != " ":
            if letter != "_" and word[i] == letter:
                guess[i] = letter
                ltr = font.render(letter, 10, BLACK)
                win.blit(ltr, (x, 300))   
            else: 
                ltr = font.render(guess[i], 10, BLACK)  
                win.blit(ltr, (x, 300))
        else:
            guess[i] = " "
        x += 40

def check_if_game_over():
    flag = True 
    for i in range(len(word)):
        if guess[i] == "_":
            flag = False

    pygame.font.init()
    font = pygame.font.SysFont("comicsans", 70)
    if flag == True:
        msg = font.render("You won!!!", 10, GREEN)
        win.blit(msg, (WIDTH/2-150, 20))
        return True
    elif img_num == 6:
        msg = font.render("You lost!!!", 10, RED)
        win.blit(msg, (WIDTH/2-150, 20))
        return True
    else:
        return False

def display_off_letters():
    font1 = pygame.font.SysFont("comicsans", 35)
    font2 = pygame.font.SysFont("comicsans", 50)
    headln = font1.render("Letters not in word: ", 5, BLACK)
    win.blit(headln, (350, 100))

    x = 350
    for i in range(26):
        if off_letters[i] != "_":
            ltr = font1.render(off_letters[i], 5, BLACK)
            win.blit(ltr, (x, 130))
            y = font2.render("/", 20, RED)
            win.blit(y, (x, 125))
            x += 40

def main():
    FPS = 60
    clock = pygame.time.Clock()
    Run = True
    selected_l = "_"
    game_over = False

    while Run:
        screen_setup()

        display_letters()
        display_word(selected_l)
        display_off_letters()

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or check_if_game_over():
                Run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                for i in range(26):
                    if circlesX[i]-15 < mx and circlesX[i]+15 > mx and circlesY[i]-15 < my and circlesY[i]+15 > my:
                        activate_ltrs[i] = False 
                        selected_l = alphabet[i]

                        if selected_l not in word:
                            global img_num
                            img_num += 1 
                            off_letters[i] = selected_l

        check_if_game_over()
        
        if Run == False:
            time.sleep(2)
            return True


while True:
    pygame.display.update()

    # screen setup
    background = pygame.image.load(r"C:\Users\user\Desktop\Giorgos\Python\VScode\hangman\Assets\background.png")
    background = pygame.transform.scale(background, (800, 600))
    win.blit(background, (0, 0))

    # font setup
    pygame.font.init()
    main_menu_font = pygame.font.SysFont("comicsans", 30)
    start_game1 = main_menu_font.render("WELCOME TO THE HANGMAN GAME", 5, WHITE)
    start_game2 = main_menu_font.render("FOR DEVELOPERS!", 5, WHITE)
    start_game3 = main_menu_font.render("PRESS THE MOUSE TO START...", 5, WHITE)

    win.blit(start_game1, (100, 100))
    win.blit(start_game2, (220, 150))
    win.blit(start_game3, (150, 300))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            word = random.choice(word_list)
            guess = ["_" for i in range(len(word))]
            activate_ltrs = [True for i in range(26)]
            off_letters = ["_" for i in range(26)]
            img_num = 0

            main()

        elif event.type == pygame.QUIT:
            quit()