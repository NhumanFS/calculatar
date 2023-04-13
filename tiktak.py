import pygame
import random

color1 = (172, 255, 120)
color2 = (255, 120, 226)
color3 = (255, 217, 120)
color4 = (178, 255, 120)
color5 = (163, 120, 255)
speed = 15

width = 300
hight = 300
fps = 30
x = 80
y = 80
pygame.init()
screen = pygame.display.set_mode((width, hight))
pygame.display.set_caption("tiktak")
run = True
gameover = False
clock = pygame.time.Clock()


field = [["", "", ""], ["", "", ""], ["", "", ""]]


def draw_grid():
    pygame.draw.line(screen, color3, (100, 0), (100, 300), 3)
    pygame.draw.line(screen, color3, (200, 0), (200, 300), 3)
    pygame.draw.line(screen, color3, (0, 100), (300, 100), 3)
    pygame.draw.line(screen, color3, (0, 200), (300, 200), 3)


def draw_tiktak():
    for i in range(3):
        for j in range(3):
            if field[i][j] == "0":
                pygame.draw.circle(
                    screen, color5, (j * 100 + 50, i * 100 + 50), 45, 3)
            elif field[i][j] == "X":
                pygame.draw.line(screen, color5, (j * 100 + 5,
                                 i * 100 + 5), (j * 100 + 95, i * 100 + 95), 3)
                pygame.draw.line(screen, color5, (j * 100 + 95,
                                 i * 100 + 5), (j * 100 + 5, i * 100 + 95), 3)


def winchek(symbol):
    flag_win = False
    global win
    for line in field:
        if line.count(symbol) == 3:
            flag_win = True
            win = [[0, field.index(line)], [1, field.index(line)], [
                2, field.index(line)]]

    for i in range(3):
        if field[0][i] == field[1][i] == field[2][i] == symbol:
            flag_win = True
            win = [[i, 0], [i,  1], [i, 2]]

    if field[0][0] == field[1][1] == field[2][2] == symbol:
        flag_win = True
        win = [[0, 0], [1,  1], [2, 2]]

    if field[0][2] == field[1][1] == field[2][0] == symbol:
        flag_win = True
        win = [[0, 2], [1,  1], [2, 0]]

    return flag_win


while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and not gameover:
            pos = pygame.mouse.get_pos()
            if field[pos[1] // 100][pos[0] // 100] == "":
                field[pos[1] // 100][pos[0] // 100] = "X"
                x, y = random.randint(0, 2), random.randint(0, 2)
                while field[x][y] != "":
                    x, y = random.randint(0, 2), random.randint(0, 2)
                field[x][y] = "0"

        playerwin = winchek("X")
        botwin = winchek("0")
        result = field[0].count("X") + field[0].count("0") + field[1].count(
            "X") + field[1].count("0") + field[2].count("X") + field[2].count("0")
        if playerwin or botwin:
            gameover = True

            if playerwin == True:
                pygame.display.set_caption("you won")

            elif botwin == True:
                pygame.display.set_caption("you failed")

        elif result == 8:
            pygame.display.set_caption("no one won")

    screen.fill(color1)
    if gameover:
        pygame.draw.rect(
            screen, color2, (win[0][0] * 100, win[0][1] * 100, 100, 100))
        pygame.draw.rect(
            screen, color2, (win[1][0] * 100, win[1][1] * 100, 100, 100))
        pygame.draw.rect(
            screen, color2, (win[2][0] * 100, win[2][1] * 100, 100, 100))
    draw_grid()
    draw_tiktak()
    pygame.display.flip()

pygame.quit()
