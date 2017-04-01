from Tkinter import *
from PIL import Image, ImageTk
from point import Point
from an_energy_calculator import the_energy_calculator
from a_path_calculator import the_path_calculator
import time

class PathDrawer():
  """A path being a series of points"""

  def drawOnPath(self, Image, Path):
    pix = Image.load()
    for somePt in Path:
      pix[somePt.x, somePt.y] = (255, 0, 0, 255)
    return Image


class App(Frame):

  def __init__(self, master):
    Frame.__init__(self, master)
    self.columnconfigure(0, weight=1)
    self.rowconfigure(0, weight=1)
    self.original = Image.open('example.png')
    self.image = ImageTk.PhotoImage(self.original)
    self.display = Canvas(self, bd=0, highlightthickness=0)
    self.display.create_image(0, 0, image=self.image, anchor=NW, tags="IMG")
    self.display.grid(row=0, sticky=W + E + N + S)
    self.pack(fill=BOTH, expand=1)
    self.bind("<Configure>", self.resize)

  def resize(self, event):
    self.energyCalc = the_energy_calculator()
    self.pathCalc = the_path_calculator()
    self.size = (event.width, event.height)
    self.the_w = event.width
    self.the_h = event.height
    self.resized = self.original.resize(self.size, Image.ANTIALIAS)

    if (self.the_w is not None and self.the_h is not None):
        self.energyMat = self.energyCalc.getEnergies(self.resized, self.the_w, self.the_h)
        self.somePath = self.pathCalc.getPath(self.energyMat, self.resized.size[0], self.resized.size[1])
        self.somePath = self.pathCalc.transposePath90(self.somePath)
        pd = PathDrawer()
        self.someImage = pd.drawOnPath(self.resized, self.somePath)
        print "Done with path drawer."

        self.transposed = self.resized.transpose(Image.ROTATE_90)
        self.tEnergyMat = self.energyCalc.getEnergies(self.transposed, self.transposed.width, self.transposed.height)
        self.tSomePath = self.pathCalc.getPath(self.tEnergyMat, self.transposed.width, self.transposed.height)
        self.someImage = pd.drawOnPath(self.resized, self.tSomePath)
        print "Done with transposed path drawer."

        self.image = ImageTk.PhotoImage(self.someImage)
        self.display.delete("IMG")
        self.display.create_image(0, 0, image=self.image, anchor=NW, tags="IMG")

root = Tk()
app = App(root)
app.mainloop()
root.destroy()
