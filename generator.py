from tkinter import *
from math import *
from random import randint


class room:
    def __init__(self, x, y, width, height, parent):
        self.width = randint(0+round(width/10), width+1-round(width/10))
        self.height = randint(0+round(height/10), height+1-round(height/10))
        self.x = randint(x, x+width-self.width)
        self.y = randint(y, y+height-self.height)
        self.conectPoint = [
            randint(self.x, self.x+self.width), randint(self.y, self.y+self.height)]
        allRooms.append(self)
        parent.conectPoints.append(self.conectPoint)
        parent.render()

    def render(self):
        canvas.create_rectangle(self.x, self.y, self.x+self.width,
                                self.y+self.height, width=1, fill=rgb((0, 0, 255)))
        canvas.create_oval(self.conectPoint[0]-5, self.conectPoint[1]-5, self.conectPoint[0]+5,
                           self.conectPoint[1]+5, width=0, fill=rgb((255, 150, 0)))


class section:
    def __init__(self, x, y, width, height, devideAmount, inside, parent):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.devideAmount = devideAmount
        self.inside = inside
        self.conectPoints = []
        self.line = None
        self.parent = parent
        if self.inside < self.devideAmount:
            self.inside += 1
            self.devide()
        else:
            room(self.x, self.y, self.width, self.height, self)
            if self.parent != None:
                parent.addPoint(self.conectPoints[0])
        allSections.append(self)

    def addPoint(self, point):
        self.conectPoints.append(point)
        if len(self.conectPoints) == 2 and self.parent != None:
            self.parent.addPoint(self.conectPoints[randint(0, 1)])

    def devide(self):
        if self.width >= self.height:
            width = randint(0+round(self.width/5),
                            self.width+1-round(self.width/5))
            height = self.height
            section(self.x, self.y, width, height,
                    self.devideAmount, self.inside, self)
            section(self.x+width, self.y, self.width-width,
                    height, self.devideAmount, self.inside, self)
        else:
            height = randint(0+round(self.height/5),
                             self.height-round(self.height/5))
            width = self.width
            section(self.x, self.y, width, height,
                    self.devideAmount, self.inside, self)
            section(self.x, self.y+height, width, self.height -
                    height, self.devideAmount, self.inside, self)

    def render(self):
        # canvas.create_rectangle(self.x, self.y, self.x+self.width,
        #                       self.y+self.height, width=5, outline=rgb((0, 255, 0)))
        if len(self.conectPoints) != 2:
            return

        if randint(0, 1) == 0:
            if randint(0, 1) == 0:
                canvas.create_line(self.conectPoints[0][0], self.conectPoints[0][1],
                                   self.conectPoints[0][0], self.conectPoints[1][1],
                                   self.conectPoints[1][0], self.conectPoints[1][1], width=5, fill=rgb((255, 0, 0)))
                return
            canvas.create_line(self.conectPoints[0][0], self.conectPoints[0][1],
                               self.conectPoints[1][0], self.conectPoints[0][1],
                               self.conectPoints[1][0], self.conectPoints[1][1], width=5, fill=rgb((255, 0, 0)))
            return

        stop = 0
        if abs(self.conectPoints[0][0]-self.conectPoints[1][0]) > abs(self.conectPoints[0][1]-self.conectPoints[1][1]):
            if self.conectPoints[0][0] < self.conectPoints[1][0]:
                stop = randint(
                    self.conectPoints[0][0], self.conectPoints[1][0])
            else:
                stop = randint(
                    self.conectPoints[1][0], self.conectPoints[0][0])

            canvas.create_line(self.conectPoints[0][0], self.conectPoints[0][1],
                               stop, self.conectPoints[0][1],
                               stop, self.conectPoints[1][1],
                               self.conectPoints[1][0], self.conectPoints[1][1], width=5, fill=rgb((255, 0, 0)))
            return

        if self.conectPoints[0][1] < self.conectPoints[1][1]:
            stop = randint(
                self.conectPoints[0][1], self.conectPoints[1][1])
        else:
            stop = randint(
                self.conectPoints[1][1], self.conectPoints[0][1])

        canvas.create_line(self.conectPoints[0][0], self.conectPoints[0][1],
                           self.conectPoints[0][0], stop,
                           self.conectPoints[1][0], stop,
                           self.conectPoints[1][0], self.conectPoints[1][1], width=5, fill=rgb((255, 0, 0)))


def rgb(value):
    return "#%02x%02x%02x" % value


def create():
    global allSections, allRooms
    print("------------")
    allSections = []
    allRooms = []
    canvas.delete("all")
    section(0, 0, 800, 800, int(roomsNumber.get()), 0, None)
    for i in allSections:
        i.render()
    for i in allRooms:
        i.render()


window = Tk()
window.configure(bg=rgb((15, 15, 15)), width=800, height=900)
window.title("Generator")

canvas = Canvas(window, width=800, height=800, bg=rgb((30, 30, 30)))
roomsNumber = Entry(window, width=10, bd=0, justify='center')
roomsNumber.insert(END, "2")
resetbutton = Button(window, text="Reset", bd=0, width=10,
                     fg=rgb((0, 0, 0)), command=create)

canvas.grid(row=0, column=0, columnspan=2)
roomsNumber.grid(row=1, column=0)
resetbutton.grid(row=1, column=1)

allSections = []
allRooms = []

canvas.mainloop()
