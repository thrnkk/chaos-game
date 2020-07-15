import pygame
import random

# Pygame
pygame.init()
pygame.display.set_caption('Chaos Game')

# Screen 
screen = pygame.display.set_mode((700, 700))
screen.fill((255,255,255))

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (200, 200, 200)
WHITE = (255, 255, 255)

# Draw X-axis lines
for x in range(70):

    pygame.draw.line(screen, GRAY, (x * 10, 0), (x * 10, 700))

# Draw Y-axis lines
for y in range(70):

    pygame.draw.line(screen, GRAY, (0, y * 10), (700, y * 10))

# ====================================================================

# Triangle
points = [(350,  100), (50,  650), (650, 650)]
multiplier = 0.5
type = ""

# Square
# points = [(150, 150), (150, 550), (550, 550), (550, 150)]
# multiplier = 1/2
# type = "vertexPreviousNot2PlacesAway"

# Square
# points = [(150, 150), (150, 550), (550, 550), (550, 150)]
# multiplier = 1/2
# type = "vertexPreviousNotEqual"

# ====================================================================

# Variables
font = pygame.font.SysFont("Verdana", 18)
running = True
colors = []
actualPoint = points[0]
lastPointToGo = 0
total = 10000
counter = 0

# Create a blank square on top
s = pygame.Surface((700, 50)) 
s.fill(WHITE)

# Draw vertexes
for point in points:

    # For each point, assign a color
    colors.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    # For each point, draw a square with it index on top
    pygame.draw.rect(screen, colors[points.index(point)], (point[0] - 5, point[1] - 5, 10, 10))
    txt_surf = font.render(str(points.index(point)), 1, BLACK)
    txt_rect = txt_surf.get_rect(center=(point[0], point[1] - 30))
    screen.blit(txt_surf, txt_rect)


def updatePoints():

    txt_surf = font.render("Points: " + str(counter), 1, BLACK)
    txt_rect = txt_surf.get_rect(topleft=(20, 20))
    s.fill(WHITE)
    s.blit(txt_surf, txt_rect)
    screen.blit(s, (0,0))

# Principal loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw points
    if (counter <= total):

        pointToGo = random.randint(0, len(points) - 1)

        if (type == 'vertexPreviousNotEqual'):

            if (lastPointToGo == pointToGo):

                pointToGo = (lastPointToGo + 1) % len(points)

        if (type == 'vertexPreviousNot2PlacesAway'):

            if points[lastPointToGo][0] != points[pointToGo][0] and points[lastPointToGo][1] != points[pointToGo][1]:

                pointToGo = (lastPointToGo + 1) % len(points)

        newPoint = ((abs(points[pointToGo][0] - actualPoint[0]) * multiplier) + min(points[pointToGo][0], actualPoint[0]), 
                    (abs(points[pointToGo][1] - actualPoint[1]) * multiplier) + min(points[pointToGo][1], actualPoint[1]))

        updatePoints()

        pygame.draw.rect(screen, colors[pointToGo], newPoint + (4, 4))
        actualPoint = newPoint
        lastPointToGo = pointToGo
        counter += 1

    pygame.display.update()

    
