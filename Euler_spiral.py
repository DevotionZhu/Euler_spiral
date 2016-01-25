import pygame
import sys
import time
import math
import random

pygame.init()

screen_w = 700
screen_h = 700
size = [screen_w, screen_h]

black = (0, 0, 0)
blue = (5,5,255)
red = (255,5,5)
green = (5,255,5)
yellow = (255,255,5)

screen = pygame.display.set_mode(size)

class menu():
    items = []
    title = ""

    def set_items(self,items):
        self.items = items

    def set_title(self,title):
        self.title = title

    def run(self):
        menu = 0
        item_strings = []
        title_font = pygame.font.Font(None,100)
        item_font = pygame.font.Font(None,75)

        title_str = title_font.render(self.title,1,green)

        title_size = title_font.size(self.title)

        for item in self.items:
            item_str = item_font.render(item,1,green)
            item_strings.append(item_str)

        while menu == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        return 1
                    if event.key == pygame.K_2:
                        return 2
                    if event.key == pygame.K_3:
                        return 3
                    if event.key == pygame.K_4:
                        return 4
                        
            screen.fill(black)

            screen.blit(title_str, ((700 - title_size[0]) / 2 ,10))

            for num in range(len(self.items)):
                screen.blit(item_strings[num], (100, 10  + title_size[1] + 20 + 150 * num))

            pygame.display.flip()
            
            

def fact(x):
    if x == 1 or x == 0:
        return 1
    if x == 2:
        return 2

    return x * fact(x - 1)

def int_sin(x):
    ans = 0
    acc = 50
    rad = x % (2 * math.pi)

    for num in range(0,acc,2):
        ans += (x ** (4 * num + 3)) / (fact(2 * num + 1) * (4 * num + 3))

    for num in range(1,acc,2):
        ans -= (x ** (4 * num + 3)) / (fact(2 * num + 1) * (4 * num + 3))

    return 500 * ans
    
def int_cos(x):
    ans = 0
    acc = 50
    rad = x % (2 * math.pi)

    for num in range(0,acc,2):
        ans += (x ** (4 * num + 1)) / (fact(2 * num) * (4 * num + 1))

    for num in range(1,acc,2):
        ans -= (x ** (4 * num + 1)) / (fact(2 * num) * (4 * num + 1))

    return 500 * ans

counter = 0
delta = .002
x = 100
y = 600
points = [(x,y)]

menu= menu()

menu.set_title("Euler Spiral")
menu.set_items(["1. Integral components", "2. Euler spiral", "3. Circle approximation","4. Looping"])

## Define the functions
def integral():
    t = 0
    delta = .01
    counter = 0

    points = []
    points_2 = []

    text_sin = "Sin(x^2)"
    text_cos = "Cos(x^2)"

    text_font = pygame.font.Font(None,75)

    text_sin_str = text_font.render(text_sin,1,yellow)

    text_cos_str = text_font.render(text_cos,1,red)

    text_size = text_font.size(text_sin)

    while t <= 5.8:
        x = counter
        y = int_sin(t)
        points.append([x,y])

        screen.fill(black)

        screen.blit(text_sin_str, ((650 - (text_size[0] * 2)) / 2 ,10))
        screen.blit(text_cos_str, (((650 - text_size[0]) / 2) + text_size[0] ,10))

        for point in points:
            pygame.draw.circle(screen, yellow, (50 + point[0], int(650 - point[1])), 5)

        pygame.display.update()

        counter += 1
        t += delta

    t = 0
    counter = 0
    
    while t <= 5.8:
        x = counter
        y = int_cos(t)
        points_2.append([x,y])

        screen.fill(black)

        screen.blit(text_sin_str, ((650 - (text_size[0] * 2)) / 2 ,10))
        screen.blit(text_cos_str, (((650 - text_size[0]) / 2) + text_size[0] ,10))

        for point in points:
            pygame.draw.circle(screen, yellow, (50 + point[0], int(650 - point[1])), 5)

        for point in points_2:
            pygame.draw.circle(screen, red, (50 + point[0], int(650 - point[1])), 5)

        pygame.display.update()

        counter += 1
        t += delta

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return ""

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return ""
def spiral():
    counter = 0
    delta = .003
    x = 100
    y = 600
    points = [(x,y)]
    
    while True:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return ""
        
        point_x = int_cos(counter)
        point_y = int_sin(counter)

        points.append((int(x + point_x),int(y - point_y)))
        
        # draw
        screen.fill(black)

        pygame.draw.circle(screen, green, (int(100 + 250 * math.sqrt(math.pi / 2)), int(600 - 250 * math.sqrt(math.pi / 2))), 5)

        for point in points:
            pygame.draw.circle(screen, red, point, 4)
        
        pygame.display.update()

        counter += delta
        
        if counter >= 5.8:
            break

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return ""

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return ""

def circle():
    counter = 0
    delta = .003
    x = 100
    y = 600
    points = [(x,y)]

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
               
        point_x = int_cos(counter)
        point_y = int_sin(counter)

        points.append((int(x + point_x),int(y - point_y)))

        counter += delta
        
        # draw
        screen.fill(black)

        pygame.draw.circle(screen, green, (int(100 + 250 * math.sqrt(math.pi / 2)), int(600 - 250 * math.sqrt(math.pi / 2))), 5)

        for point in points:
            pygame.draw.circle(screen, red, point, 4)

        if counter >= 5.8:
            x = 500
            y = 300

            cont = True
            
            while cont:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            y -= 5
                        if event.key == pygame.K_DOWN:
                            y += 5
                        if event.key == pygame.K_LEFT:
                            x -= 5
                        if event.key == pygame.K_RIGHT:
                            x += 5
                        if event.key == pygame.K_RETURN:
                            cont = False
                            break

                screen.fill(black)
                
                pygame.draw.circle(screen, green, (int(100 + 250 * math.sqrt(math.pi / 2)), int(600 - 250 * math.sqrt(math.pi / 2))), 5)
                pygame.draw.circle(screen, yellow, (x,y), 200, 4)
                
                for point in points:
                    pygame.draw.circle(screen, red, point, 5)
                    
                pygame.display.update()
        
        pygame.display.update()

        if counter >= 5.8:
            break

def loop():
    while True:
        counter = 0
        delta = .003
        x = 100
        y = 600
        points = [(x,y)]
        
        while True:
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    break

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return ""
            
            point_x = int_cos(counter)
            point_y = int_sin(counter)

            points.append((int(x + point_x),int(y - point_y)))
            
            # draw
            screen.fill(black)

            pygame.draw.circle(screen, green, (int(100 + 250 * math.sqrt(math.pi / 2)), int(600 - 250 * math.sqrt(math.pi / 2))), 5)

            for point in points:
                pygame.draw.circle(screen, red, point, 4)
            
            pygame.display.update()

            counter += delta
            
            if counter >= 5.8:
                break

########## actual loop start ############

while True:
    ans = menu.run()

    if ans == 1:
        integral()

    if ans == 2:
        spiral()

    if ans == 3:
        circle()

    if ans == 4:
        loop()








    
