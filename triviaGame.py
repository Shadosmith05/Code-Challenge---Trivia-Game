import requests
import pygame
import pygame_widgets
from pygame_widgets.dropdown import Dropdown


response = requests.get("https://opentdb.com/api.php?amount=10&type=multiple")


# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
start = True


BORDER_COLOR = (0,0,0)


# starting screen
def startScreen():
    font = pygame.font.SysFont("Ariel", 30)
    welcome1 = font.render("Welcome to Trivia Game!!!", True, "black", "white")
    welcome2 = font.render("Select the difficulty and category", True, "black", "white")
    welcome3 = font.render("then press start to play.", True, "black", "white")
    start = font.render("Start Game", True, "black", "white")

    difficulty = Dropdown(screen, 50, 300, 200, 50, name="Select Difficulty", choices=["Easy", "Medium", "Hard"], values=["Easy", "Medium", "Hard"], colour=pygame.Color("white"))
    category = Dropdown(screen, 350, 300, 200, 50, name="Select Category", choices=["General Knowledge", "Entertainment: Books", "Entertainment: Film", "Entertainment: Music", "Entertainment: Musicals & Theatres", "Entertainment: Television", "Entertainment: Video Games", "Entertainment: Board Games", "Science & Nature", "Science: Computers", "Science: Mathematics", "Mythology", "Sports", "Geography", "History", "Politics", "Art", "Celebrities", "Animals", "Vehicles", "Entertainment: Comics", "Science: Gadgets", "Entertainment: Japanes Anime & Manga", "Entertainment: Cartoons & Animations"], values=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23], colour=pygame.Color("white"))

    screen.fill("white")
    pygame.draw.rect(screen, "white", (200, 450, 200, 50))

    # border for welcome text
    pygame.draw.lines(screen, "black", True, ((50,50),(50,210),(550,210),(550,50)))
    # border for start button
    pygame.draw.lines(screen, "black", True, ((200,450),(400,450),(400,500),(200,500)))

    screen.blit(welcome1, (170,75))
    screen.blit(welcome2, (75,125))
    screen.blit(welcome3, (75,150))
    screen.blit(start, (245, 465))

    pygame_widgets.update(pygame.event.get())
    # border for difficulty dropdown
    pygame.draw.lines(screen, "black", True, ((50,300),(50,350),(250,350),(250,300)))
    # border for category dropdown
    pygame.draw.lines(screen, "black", True, ((350,300),(350,350),(550,350),(550,300)))

# screen displayed with a question
def questionScreen(question, ans1, ans2, ans3, ans4, score):
    screen.fill("white")
    font = pygame.font.SysFont("Ariel", 20)
    question = font.render(question, True, "black", "white")
    answer1 = font.render(ans1, True, "black", "white")
    answer2 = font.render(ans2, True, "black", "white")
    answer3 = font.render(ans3, True, "black", "white")
    answer4 = font.render(ans4, True, "black", "white")
    scoreText = font.render(f"{score}/10", True, "black", "white")
    
    # border for question box
    pygame.draw.lines(screen, "black", True, ((50,50),(50,210),(550,210),(550,50)))
    # border for score
    pygame.draw.lines(screen,"black", True, ((550,0),(550,25),(600,25),(600,0)))

    # border for answer button 1
    pygame.draw.lines(screen, "black", True, ((75,260),(75,310),(525,310),(525,260)))
    # border for answer button 2
    pygame.draw.lines(screen, "black", True, ((75,340),(75,390),(525,390),(525,340)))
    # border for anser button 3
    pygame.draw.lines(screen, "black", True, ((75,420),(75,470),(525,470),(525,420)))
    # border for answer button 4
    pygame.draw.lines(screen, "black", True, ((75,500),(75,550),(525,550),(525,500)))

    screen.blit(question, (75, 75))
    screen.blit(answer1, (100,280))
    screen.blit(answer2, (100,360))
    screen.blit(answer3, (100,440))
    screen.blit(answer4, (100,520))
    screen.blit(scoreText, (565, 6))

# end of game screen
def endScreen(score):
    font = pygame.font.SysFont("Ariel", 30)
    ending = font.render(f"Your score: {score}/10", True, "black", "white")

    level = ""
    line = ""
    if score > 8:
        level = "Trivia Master"
        line = "Amazing job!!!"
    elif score > 5:
        level = "Pro"
        line = "Good job!"
    else:
        level = "Novice"
        line = "Better luck next time."
    
    rank = font.render(f"Your rank: {level}", True, "black", "white")
    message = font.render(line, True, "black", "white")
    replay = font.render("Play Again", True, "black", "white")
    quit = font.render("Quit", True, "black", "white")

    screen.fill("white")

    # border for message box
    pygame.draw.lines(screen, "black", True, ((50,50),(50,210),(550,210),(550,50)))
    # border for play again button
    pygame.draw.lines(screen, "black", True, ((100,450),(100,500),(250,500),(250,450)))
    # border for quit button
    pygame.draw.lines(screen, "black", True, ((350,450),(350,500),(500,500),(500,450)))

    screen.blit(ending, (75, 75))
    screen.blit(rank, (75, 120))
    screen.blit(message, (75, 165))
    screen.blit(replay, (125,465))
    screen.blit(quit, (400,465))


while start:
    i = 0
    score = 0
    questions = ["First", "Second", "Third", "Fourth", "Fifth"]
    running = True
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # check to see if start button is pressed
            if 200 <= mouse[0] <= 400 and 450 <= mouse[1] <= 500:
                while running:
                    # pygame.QUIT event means the user clicked X to close your window
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            start = False
                            running = False
        
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            # check to see if answer 1 is pressed
                            if 75 <= mouse[0] <= 525 and 260 <= mouse[1] <= 310:
                                i += 1
                            # check to see if answer 2 is pressed
                            elif 75 <= mouse[0] <= 525 and 340 <= mouse[1] <= 390:
                                i += 1
                            # check to see if answer 3 is pressed
                            elif 75 <= mouse[0] <= 525 and 420 <= mouse[1] <= 470:
                                i += 1
                            # check to see if answer 4 is pressed
                            elif 75 <= mouse[0] <= 525 and 500 <= mouse[1] <= 550:
                                i += 1
                            
                            if i >= len(questions):
                                while running:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            start = False
                                            running = False

                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            # check to see if quit button is pressed
                                            if 350 <= mouse[0] <= 500 and 450 <= mouse[1] <= 500:
                                                running = False
                                                start = False
                                                # check to see if play again button is pressed
                                            elif 100 <= mouse[0] <= 250 and 450 <= mouse[1] <= 500:
                                                running = False
                                                i = 0

                                    endScreen(score)
                                    pygame.display.update()
                                    mouse = pygame.mouse.get_pos()

                    questionScreen(questions[i],"Answer 1","Answer 2","Answer 3","Answer 4",score)
                    pygame.display.update()
                    mouse = pygame.mouse.get_pos()

    startScreen()
    pygame.display.update()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
