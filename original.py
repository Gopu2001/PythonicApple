#!/usr/bin/env python3

'''
This is the official Pythonic Apple game. Based off of the retro game snake,
you will find that this game is a bit different. I will let you find out
what is different. (Hint: only two buttons control the snake!)
'''

import pygame, sys, time, random, os
from pygame.locals import *

w,h = 500,500
WHITE = 255,255,255
BLACK = 0,0,0
RED = 255,0,0
BLUE = 0,255,0
GREEN = 0,0,255
RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3
apple_locs = None

pygame.init()
screen = pygame.display.set_mode((w,h+50))
pygame.display.set_caption('Pythonic Apple')
font = pygame.font.SysFont('comicsansms',20)

class Snake():
    def __init__(self, controlability = True):
        self.color = WHITE
        self.heading = RIGHT
        self.coors = [[50,50], [50,60], [60,60], [60,50]]
        self.key = None
        self.length = 1
        self.control = controlability
        self.start_heading = self.heading
        self.before_start_heading = self.start_heading
    def __update__(self):
        self.before_start_heading, self.start_heading = self.start_heading, self.heading
        added = False
        global apple_locs
        if apple_locs != None:
            if apple_locs[0] == self.coors[0][0] and apple_locs[1] == self.coors[0][1]:
                apple_locs = None
                added = True
        if self.control:
            key = pygame.key.get_pressed()
            if self.key != key:
                self.key = key
                if self.key[pygame.K_LEFT]:
                    self.heading = (self.heading+1)%4
                if self.key[pygame.K_RIGHT]:
                    self.heading = (self.heading-1)%4
        else:
            if apple_locs != None:
                #then go towards apple
                rand_num = random.randint(0,1)*2
                if self.coors[0][0] < apple_locs[0]:
                    if self.heading == LEFT:
                        #print('turning:', self.heading, ' ->', (rand_num+1))
                        self.heading = rand_num+1
                    else:
                        self.heading = RIGHT
                elif self.coors[0][0] > apple_locs[0]:
                    if self.heading == RIGHT:
                        #print('turning:', self.heading, ' ->', (rand_num+1))
                        self.heading = rand_num+1
                    else:
                        self.heading = LEFT
                elif self.coors[0][1] < apple_locs[1]:
                    if self.heading == UP:
                        #print('turning:', self.heading, ' ->', rand_num)
                        self.heading = rand_num
                    else:
                        self.heading = DOWN
                elif self.coors[0][1] > apple_locs[1]:
                    if self.heading == DOWN:
                        #print('turning:', self.heading, ' ->', rand_num)
                        self.heading = rand_num
                    else:
                        self.heading = UP
            test_condition_1 = (self.heading == RIGHT and self.coors[0][0]+10 == w) or (self.heading == LEFT and self.coors[0][0] == 0) or (self.heading == UP and self.coors[0][1] == 0) or (self.heading == DOWN and self.coors[0][1]+10 == h)
            temp = []
            #print(self.coors)
            for i in range(self.length):
                temp.append(self.coors[4*i])
            #print(temp)
            #print(self.heading == RIGHT and [temp[0][0]+10,temp[0][1]] in temp[1:])
            test_condition_2 = (self.heading == RIGHT and [temp[0][0]+10,temp[0][1]] in temp[1:len(temp)-1]) or (self.heading == LEFT and [temp[0][0]-10,temp[0][1]] in temp[1:len(temp)-1]) or (self.heading == UP and [temp[0][0],temp[0][1]-10] in temp[1:len(temp)-1]) or (self.heading == DOWN and [temp[0][0],temp[0][1]+10] in temp[1:len(temp)-1])
            if test_condition_1 or test_condition_2:
                rand = (random.randint(0,1)*2)-1
                test = (self.heading+(rand))%4
                if test == RIGHT and self.coors[0][0]+10 == w or test == LEFT and self.coors[0][0] == 0 or test == UP and self.coors[0][1] == 0 or test == DOWN and self.coors[0][1]+10 == h:
                    '''if rand == -1:
                        self.heading = (self.heading+1)%4
                    if rand == 1:
                        self.heading = (self.heading-1)%4'''
                    if self.start_heading == (self.before_start_heading+1)%4:
                        self.heading = (self.start_heading-1)%4
                    if self.start_heading == (self.start_heading-1)%4:
                        self.heading = (self.start_heading+1)%4
                else:
                    self.heading = test
                
            '''if self.start_heading == (self.heading+2)%4:
                self.heading = (self.heading+((random.randint(0,1)*2)-1))%4'''
            #print(self.heading)
        temp = self.coors.copy()
        if added:
            self.length += 1
            self.coors.extend(temp[len(self.coors)-4:])
        for i in range(int(len(self.coors)/4),1,-1):
            self.coors[(4*i)-4:(4*i)] = self.coors[(4*(i-1))-4:(4*(i-1))]
        if self.heading == RIGHT:
            self.coors[0:4] = [ [x+10,y] for x,y in self.coors[0:4]]
        if self.heading == LEFT:
            self.coors[0:4] = [ [x-10,y] for x,y in self.coors[0:4]]
        if self.heading == UP:
            self.coors[0:4] = [ [x,y-10] for x,y in self.coors[0:4]]
        if self.heading == DOWN:
            self.coors[0:4] = [ [x,y+10] for x,y in self.coors[0:4]]
        for x,y in self.coors:
            if x < 0 or y < 0 or x > w or y > h:
                game_over_script()
        temp = []
        for i in range(self.length):
            temp.append(self.coors[4*i:4*(i+1)])
            if temp.count(self.coors[4*i:4*(i+1)]) > 1:
                game_over_script()
    def draw(self):
        self.__update__()
        for i in range(self.length):
            pygame.draw.polygon(screen, self.color, self.coors[(4*i):(4*i)+4], 0)
        # Uncomment below to slow down the game
        #if snake.length > 8:
        #    time.sleep(0.1)
        #time.sleep(1)
        time.sleep(0.05)

def game_over_script():
    #print('Game Over!\n\tYour Score:', (snake.length-1))
    if (snake.length-1) > int(open('/usr/lib/python3/dist-packages/pythonicapple/high_score.txt', 'r').readline().split('\n')[0]):
        edit_high_score(snake.length-1)
    elif not snake.control:
        #print('restarting ai')
        os.execv(sys.argv[0], sys.argv)
    counter = 0
    while True:
        screen.blit(font.render('hit F5 to restart', True, (0,255,255)), (0,400))
        screen.blit(font.render('hit Q to quit', True, (255,255,0)), (0,450))
        score_text = font.render('Score: ' + str(snake.length-1), True, (0,255,255))
        high_score_text = open('/usr/lib/python3/dist-packages/pythonicapple/high_score.txt', 'r')
        high_score_info = font.render('High Score: ' + high_score_text.readline().split('\n')[0] + ' by ' + high_score_text.readline().split('\n')[0], True, (0,255,255))
        screen.blit(score_text, (0,500))
        screen.blit(high_score_info, (0,520))
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F5:
                os.execv(sys.argv[0], sys.argv)
            if event.key == pygame.K_q:
                break
        if event.type == pygame.QUIT:
            break
        pygame.display.update()
    pygame.quit()
    sys.exit()

def edit_high_score(score):
    name = ''
    while True:
        if not snake.control:
            name = 'AI score'
            break
        screen.fill(BLACK)
        screen.blit(font.render('Type your name to submit your score', True, (0,255,255)), (0,0))
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                name += event.unicode
            elif event.key == K_BACKSPACE:
                name = name[:-1]
            elif event.key == K_RETURN:
                break
        screen.blit(font.render(name, True, (0,255,255)), (25,300))
        pygame.display.update()
    with open('/usr/lib/python3/dist-packages/pythonicapple/high_score.txt', 'r+') as high_score_text:
        previous_high_score_data = high_score_text.read()
        high_score_text.seek(0,0)
        high_score_text.write(str(score) + '\n' + name.rstrip('\r\n') + '\n' + previous_high_score_data)

if len(sys.argv) > 1:
    #print(sys.argv)
    #print(bool(sys.argv[1]))
    snake = Snake(bool(int(sys.argv[1])))
else:
    while True:
        screen.fill(BLACK)
        event = pygame.event.poll()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                snake = Snake(False)
                break
            if event.button == 1:
                snake = Snake(True)
                break
        pygame.display.update()

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            #print('You Quit!\n\tYour Score:', (snake.length-1))
            time.sleep(5)
            pygame.quit()
            sys.exit()
    screen.fill(BLACK)
    snake.draw()
    if apple_locs == None:
        apple_locs = [random.randint(0,(w/10)-1)*10, random.randint(0,(h/10)-1)*10]
    pygame.draw.polygon(screen, RED, [ apple_locs, [apple_locs[0]+10, apple_locs[1]], [apple_locs[0]+10,apple_locs[1]+10], [apple_locs[0],apple_locs[1]+10]])
    pygame.draw.line(screen, WHITE, (0,500),(w,500),1)
    score_text = font.render('Score: ' + str(snake.length-1), True, (0,255,255))
    high_score_text = open('/usr/lib/python3/dist-packages/pythonicapple/high_score.txt', 'r')
    high_score_info = font.render('High Score: ' + high_score_text.readline().split('\n')[0] + ' by ' + high_score_text.readline().split('\n')[0], True, (0,255,255))
    screen.blit(score_text, (0,500))
    screen.blit(high_score_info, (0,520))
    pygame.display.update()
