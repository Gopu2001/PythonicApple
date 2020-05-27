from org.transcrypt.stubs.browser import __pragma__
from com.fabricjs import fabric

__pragma__("alias", "S", "$")
__pragma__("noalias", "clear")

w, h = 500,500
inc = 20

enter, esc, space = 13, 27, 32

window.onkeydown = lambda event: event.keycode != space
player = apple = obstacle = mongoose = canvas = None

facing = [1, 2, 3, 4]
LEFT = 1
UP = 2
RIGHT = 3
DOWN = 4

class Snake:
    def __init__(self):
        self.alive = True
        self.past = []
        self.tail = []
        self.coords = []
        self.snake_length = 1
        self.loc = (5*inc, 5*inc)
        self.snake = __new__(fabric.Rect({
            'left': self.loc[0],
            'top': self.loc[1],
            'width': inc,
            'height': inc,
            'originX': 'left',
            'originY': 'top',
            'fill': 'green'
        }))
        self.facing = 3
    def update(self):
        canvas.remove(self.snake)
        for t_box in self.tail:
            canvas.remove(t_box)
        self.coords = []
        self.tail = []
        self.past.append(self.loc)
        if self.facing == 1:
            self.loc = (self.loc[0] - inc, self.loc[1])
        elif self.facing == 2:
            self.loc = (self.loc[0], self.loc[1] - inc)
        elif self.facing == 3:
            self.loc = (self.loc[0] + inc, self.loc[1])
        else:
            self.loc = (self.loc[0], self.loc[1] + inc)
        self.snake = __new__(fabric.Rect({
            'left': self.loc[0],
            'top': self.loc[1],
            'width': inc,
            'height': inc,
            'originX': 'left',
            'originY': 'top',
            'fill': 'green'
        }))
        self.coords.append(self.loc)
        self.snake.hasControls = False
        tail = []
        for i in range(self.snake_length-1):
            self.tail.append(__new__(fabric.Rect({
                'left': self.past[len(self.past) - (i+1)][0],
                'top': self.past[len(self.past) - (i+1)][1],
                'width': inc,
                'height': inc,
                'originX': 'left',
                'originY': 'top',
                'fill': 'green'
            })))
            self.coords.append(self.past[len(self.past) - (i+1)])
        for t_box in self.tail:
            canvas.add(t_box)
            if t_box.left == self.snake.left and t_box.top == self.snake.top:
                alert("You ate yourself! Click OK to continue.")
                self.die()
        canvas.add(self.snake)
    def turn(self, e):
        if e.keyCode == 37:
            if self.facing == 1:
                self.facing = 4
            else:
                self.facing = facing[facing.index(self.facing)-1]
        elif e.keyCode == 39:
            if self.facing == 4:
                self.facing = 1
            else:
                self.facing = facing[facing.index(self.facing)+1]
        elif e.keyCode == 80:
            alert("Game Paused. Click OK to continue.")
    def die(self):
        player.alive = False
        canvas.remove(self.snake)
        for t_box in self.tail:
            canvas.remove(t_box)
        gameOver()

class Apple:
    def __init__(self):
        self.spawn()
    def spawn(self):
        self.loc = (int(Math.random() * w / inc) * inc, int(Math.random() * h / inc) * inc)
        self.apple = __new__(fabric.Rect({
            'left': self.loc[0],
            'top': self.loc[1],
            'width': inc,
            'height': inc,
            'originX': 'left',
            'originY': 'top',
            'fill': 'red'
        }))
        self.apple.hasControls = False
        self.apple.evented = False
        self.apple.selectable = False
        canvas.add(self.apple)
    def eat(self):
        canvas.remove(self.apple)

class Obstacle:
    def __init__(self):
        self.in_place = False
        self.block = None
    def generate_obstacle(self, apple_loc):
        if self.block != None:
            canvas.remove(self.block)
        self.apple_loc = apple_loc
        self.spot = int(Math.random()*3)+1
        if self.spot == LEFT and apple_loc[0] == 0:
            self.spot = RIGHT
        if self.spot == RIGHT and apple_loc[0] == w-inc:
            self.spot = LEFT
        if self.spot == UP and apple_loc[1] == 0:
            self.spot = DOWN
        if self.spot == DOWN and apple_loc[1] == h-inc:
            self.spot = UP

        if self.spot == LEFT:
            self.locs = (self.apple_loc[0]-inc, self.apple_loc[1])
        elif self.spot == UP:
            self.locs = (self.apple_loc[0], self.apple_loc[1]-inc)
        elif self.spot == RIGHT:
            self.locs = (self.apple_loc[0]+inc, self.apple_loc[1])
        elif self.spot == DOWN:
            self.locs = (self.apple_loc[0], self.apple_loc[1]+inc)
    def draw_obstacle(self):
        if self.block != None:
            canvas.remove(self.block)
        self.block = __new__(fabric.Rect({
            'left': self.locs[0],
            'top': self.locs[1],
            'width': inc,
            'height': inc,
            'originX': 'left',
            'originY': 'top',
            'fill': 'black'
        }))
        self.block.hasControls = False
        self.block.evented = False
        self.block.selectable = False
        canvas.add(self.block)
        self.in_place = True

class Mongoose:
    def __init__(self):
        self.locs = [0,0]
        self.mongoose = None
    def generate_mongoose(self):
        self.direction = int(Math.random()*3)+1
        if self.direction == LEFT:
            self.locs[0] = w
            self.locs[1] = int(Math.random()*h/inc)*inc
        if self.direction == UP:
            self.locs[0] = int(Math.random()*w/inc)*inc
            self.locs[1] = h
        if self.direction == RIGHT:
            self.locs[0] = -1*inc
            self.locs[1] = int(Math.random()*h/inc)*inc
        if self.direction == DOWN:
            self.locs[0] = int(Math.random()*w/inc)*inc
            self.locs[1] = -1*inc
        self.hunting = True
    def draw(self):
        if self.mongoose != None:
            canvas.remove(self.mongoose)
        if self.hunting:
            if self.direction == LEFT:
                self.locs = [self.locs[0]-inc, self.locs[1]]
                if self.locs[0] <= 0:
                    self.die()
            if self.direction == UP:
                self.locs = [self.locs[0], self.locs[1]-inc]
                if self.locs[1] <= 0:
                    self.die()
            if self.direction == RIGHT:
                self.locs = [self.locs[0]+inc, self.locs[1]]
                if self.locs[0] >= w:
                    self.die()
            if self.direction == DOWN:
                self.locs = [self.locs[0], self.locs[1]+inc]
                if self.locs[1] >= h:
                    self.die()
            self.mongoose = __new__(fabric.Rect({
                'left': self.locs[0],
                'top': self.locs[1],
                'width': inc,
                'height': inc,
                'originX': 'left',
                'originY': 'top',
                'fill': 'yellow'
            }))
            self.mongoose.hasControls = False
            self.mongoose.evented = False
            self.mongoose.selectable = False
            canvas.add(self.mongoose)
    def die(self):
        self.hunting = False
        canvas.remove(self.mongoose)

def update():
    nonlocal slowdown
    nonlocal start
    nonlocal started
    if player != None:        
        moveCanvas()
        changeColor()
    if not started and start:
        startTheGame()
    if start and started and player != None:
        player.update()
        if player.loc[0] == apple.loc[0] and player.loc[1] == apple.loc[1]:
            apple.eat()
            apple.spawn()
            player.snake_length += 1
            changeScore(player.snake_length - 1)
            if player.snake_length-1 > 1:
                obstacle.generate_obstacle(apple.loc)
                if obstacle.locs not in player.coords:
                    obstacle.draw_obstacle()
        if mongoose.hunting and player.loc[0]==mongoose.locs[0] and player.loc[1]==mongoose.locs[1]:
            mongoose.die()
            player.snake_length += 2
            changeScore(player.snake_length - 1)
        index = 0
        for coordinate in player.coords:
            if mongoose.locs[0] == coordinate[0] and mongoose.locs[1] == coordinate[1] and mongoose.hunting:
                player.snake_length = len(player.coords)-index
                changeScore(player.snake_length - 1)
            index += 1
        if obstacle.in_place and player.loc[0]==obstacle.locs[0] and player.loc[1]==obstacle.locs[1]:
            alert("You ran into an obstacle! Click OK to continue.")
            player.die()
        if player.loc[0] < 0 or player.loc[0] >= w or player.loc[1] < 0 or player.loc[1] >= h:
            alert("You went out of bounds! Click OK to continue.")
            player.die()
        if player.alive:
            update_time = 150 - (10*(player.snake_length-1))
            if update_time <= 0:
                update_time = 1
            window.setTimeout(update, update_time)
    else:
        window.setTimeout(update, 500)
        #window.onblur = pauseGame

def pauseGame():
    alert("Game Paused. Click OK to continue.")

def startTheGame():
    nonlocal canvas
    canvas = __new__(fabric.Canvas("canvas", {'width': w, 'height': h}))
    nonlocal started
    nonlocal player
    nonlocal apple
    nonlocal obstacle
    nonlocal mongoose
    player = Snake()
    apple = Apple()
    obstacle = Obstacle()
    mongoose = Mongoose()
    window.addEventListener('keydown', player.turn, True)
    started = True
update()

def draw_mongoose():
    mongoose.draw()
    index = 0
    for coordinate in player.coords:
        if mongoose.locs[0] == coordinate[0] and mongoose.locs[1] == coordinate[1] and mongoose.hunting:
            player.snake_length = index+1
            changeScore(player.snake_length - 1)
            break
        index += 1
    if mongoose.hunting and player.loc[0]==mongoose.locs[0] and player.loc[1]==mongoose.locs[1]:
        mongoose.die()
        player.snake_length += 2
        changeScore(player.snake_length - 1)
    if mongoose.hunting:
        window.setTimeout(draw_mongoose, 250)

def genMongoose():
    if start and started:
        mongoose.generate_mongoose()
        draw_mongoose()
        window.setTimeout(genMongoose, 250*h/inc*2)

window.setTimeout(genMongoose, 2000)

cv_mv = 1
left = 0
top = 0

def moveCanvas():
    nonlocal start
    nonlocal started
    if start and started:
        if player.alive:
            nonlocal mv_right
            nonlocal mv_bottom
            cv = document.getElementById("canvas")
            if player.alive and (player.snake_length-1 >= 10):
                if left+w+20 < window.innerWidth and mv_right:
                    left += cv_mv
                    if left+w+20 >= window.innerWidth:
                        mv_right = False
                elif not mv_right:
                    left -= cv_mv
                    if left <= 0:
                        mv_right = True
                if top+h+160 < window.innerHeight and mv_bottom:
                    top += cv_mv
                    if top+h+160 >= window.innerHeight:
                        mv_bottom = False
                elif not mv_bottom:
                    top -= cv_mv
                    if top <= 0:
                        mv_bottom = True
            cv.style.left = ""+left+"px"
            cv.style.top = ""+top+"px"
            cv.style.border = '5px solid black'
    window.setTimeout(moveCanvas, 75)

mv_right = True
mv_bottom = True

def changeColor():
    if start and started and player.alive and (player.snake_length-1 >=5):
        nonlocal rd
        nonlocal gd
        nonlocal bd
        if r > 0 and rd:
            r -= 1
            if r == 0:
                rd = False
        elif not rd:
            r += 1
            if r == 255:
                rd = True
        if g > 0 and gd:
            g -= 1
            if g == 0:
                gd = False
        elif not gd:
            g += 1
            if g == 255:
                gd = True
        if b > 0 and bd:
            b -= 1
            if b == 0:
                bd = False
        elif not bd:
            b += 1
            if b == 255:
                bd = True
        canvas.backgroundColor = 'rgb('+r+','+g+','+b+')'
    window.setTimeout(changeColor, 100)

r, g, b = int(255*Math.random()), int(255*Math.random()), int(255*Math.random())
rd, gd, bd = True, True, True
