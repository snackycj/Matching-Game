import Tkinter as tk
import time
from random import randint
from random import shuffle




win = tk.Tk()
canvas = tk.Canvas(win, width = 900, height = 550)
canvas.pack()
class Tile(object):
    def __init__(self, x, y, text):
        self.y = y
        self.x = x
        self.text = text
    def drawBack(self):
        canvas.create_rectangle(self.x, self.y, self.x + 70, self.y + 70, fill = "white")
        self.isFaceUp = False
    def drawFaceUp(self):
        canvas.create_rectangle(self.x, self.y, self.x + 70, self.y + 70, fill = "white")
        canvas.create_text(self.x + 35, self.y + 35, text = self.text, width = 70)
        self.isFaceUp = True
    def isUnderMouse(self, event):
        if(event.x > self.x and event.x < self.x + 70):
            if(event.y > self.y and event.y < self.y + 70):
                return True

tiles = []
colors = [ "Red",
           "Yellow",
           "Blue",
           "Purple",
           "Green",
           "Black",
           "Brown",
           "Gray",
           "Orange",
           "Pink",
           "Indigo",
           "White"]

selected = []
for i in range(10):
    randomInd = randint(0, len(colors) - 1)
    color = colors[randomInd]
    selected.append(color)
    selected.append(color)
    del colors[randomInd]
shuffle(selected)

flippedTiles = []
flippedThisTurn = 0
def tileSelected(event):
    global flippedTiles
    global flippedThisTurn
    for tile in tiles:
        if tile.isUnderMouse(event):
            if (not(tile.isFaceUp)) :
                tile.drawFaceUp()
                flippedTiles.append(tile)
                flippedThisTurn += 1

            if (flippedThisTurn == 2):
                win.after(1000, checkTiles)
                flippedThisTurn = 0


def checkTiles():
    if not(flippedTiles[-1].text == flippedTiles[-2].text): #check last two elements
        flippedTiles[-1].drawBack() #facedown last two elements
        flippedTiles[-2].drawBack()
        del flippedTiles[-2:] #remove last two elements
NUM_COLS = 5
NUM_ROWS = 4

for x in range(0,NUM_COLS):
    for y in range(0,NUM_ROWS):
            tiles.append(Tile(x * 78 + 10, y * 78 + 40, selected.pop()))

for i in range(len(tiles)):
    tiles[i].drawBack()



win.bind("<Button-1>", tileSelected)



win.mainloop()


    




