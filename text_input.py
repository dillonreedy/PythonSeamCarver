# Frame - A widget
#		Used mainly as a geometry master between other widgets.
# columnconfigure():
# 		to give the columns in the middle some weight.
#		With more weight than the other columns, they will expand
#		and contract to fill any extra space you have.
from Tkinter import *
from PIL import Image, ImageTk
from image_resizer import the_image_resizer
from an_energy_calculator import the_energy_calculator
from a_path_calculator import the_path_calculator
import os


programDir = os.path.dirname(os.path.realpath(__file__))
imageName = raw_input()


class App(Frame):

  def resize(self):
    global root
    global imageName
    self.energyCalc = the_energy_calculator()
    self.pathCalc = the_path_calculator()
    self.w.pack_forget()
    new_h = int(self.e1.get())
    new_w = int(self.e2.get())
    # The (250, 250) is (height, width)

    an_image_resizer = the_image_resizer()
    self.currentImage = self.original
    if ((new_w - self.original.width) > 0):  # New Image Wider
      while (self.currentImage.width != new_w):
        self.energyMat = self.energyCalc.getEnergies(
            self.currentImage, self.currentImage.width, self.currentImage.height)
        print ("Done calculating energies.")
        self.somePath = self.pathCalc.getPath(
            self.energyMat, self.currentImage.width, self.currentImage.height)
        print ("Done getting the path.")
        self.somePath = self.pathCalc.transposePath90(self.somePath)
        self.currentImage = an_image_resizer.GetWidthStretchImage(
            self.currentImage, self.somePath)
        print ("Current image width: " + str(self.currentImage.width))

    elif ((new_w - self.original.width) < 0):  # New Image Narrower
      while (self.currentImage.width != new_w):
        self.energyMat = self.energyCalc.getEnergies(
            self.currentImage, self.currentImage.width, self.currentImage.height)
        print ("Done calculating energies.")
        self.somePath = self.pathCalc.getPath(
            self.energyMat, self.currentImage.width, self.currentImage.height)
        print ("Done getting the path.")
        self.somePath = self.pathCalc.transposePath90(self.somePath)
        self.currentImage = an_image_resizer.GetWidthShrinkImage(
            self.currentImage, self.somePath)
        print ("Current image width: " + str(self.currentImage.width))

    self.tCurrentImage = self.currentImage.transpose(Image.ROTATE_90)
    if ((new_h - self.original.height > 0)):  # New Image Taller
      while (self.tCurrentImage.width != new_h):
        self.energyMat = self.energyCalc.getEnergies(
            self.tCurrentImage, self.tCurrentImage.width, self.tCurrentImage.height)
        self.somePath = self.pathCalc.getPath(
            self.energyMat, self.tCurrentImage.width, self.tCurrentImage.height)
        self.somePath = self.pathCalc.transposePath90(self.somePath)
        self.tCurrentImage = an_image_resizer.GetWidthStretchImage(
            self.tCurrentImage, self.somePath)
        print ("Current image height: " + str(self.tCurrentImage.width))
    elif ((new_h - self.original.height < 0)):  # New Image Shorter
      while (self.tCurrentImage.width != new_h):
        self.energyMat = self.energyCalc.getEnergies(
            self.tCurrentImage, self.tCurrentImage.width, self.tCurrentImage.height)
        self.somePath = self.pathCalc.getPath(
            self.energyMat, self.tCurrentImage.width, self.tCurrentImage.height)
        self.tCurrentImage = an_image_resizer.GetWidthShrinkImage(
            self.tCurrentImage, self.somePath)
        print ("Current image height: " + str(self.tCurrentImage.width))

      # resize your heights here too
      # if ((new_h - self.original.height) > 0):  # New Image Taller
      # elif ((new_h - self.original.height) < 0):  # New Image Shorter

      # self.transposedImage = self.currentImage.transpose()

    self.original = self.tCurrentImage.transpose(Image.ROTATE_270)
    img = ImageTk.PhotoImage(self.original)

    self.w = Canvas(root, width=self.original.width,
                    height=self.original.height)
    self.w.grid(row=1, column=0)
    self.w.create_image(0, 0, image=img, anchor=NW, tags="IMG")
    self.w.img = img
    self.w.pack()

    self.l1.pack_forget()
    self.l1 = Label(root, text="Height:")
    self.l1.grid(row=2, column=0)
    self.l1.pack(side=LEFT)

    self.e1.pack_forget()
    self.e1 = Entry(root)
    self.e1.insert(0, str(self.original.height))
    self.e1.grid(row=2, column=1)
    self.e1.pack(side=LEFT)

    self.l2.pack_forget()
    self.l2 = Label(root, text="Width:")
    self.l2.grid(row=2, column=2)
    self.l2.pack(side=LEFT)

    self.e2.pack_forget()
    self.e2 = Entry(root)
    self.e2.insert(0, str(self.original.width))
    self.e2.grid(row=2, column=3)
    self.e2.pack(side=LEFT)

    self.b1.pack_forget()
    self.b1 = Button(root, text="Stretch", fg="blue", command=self.resize)
    self.b1.grid(row=2, column=4)
    self.b1.pack(side=LEFT)

    self.b2.pack_forget()
    self.b2 = Button(root, text="Save", fg="black", command=self.save)
    self.b2.grid(row=2, column=5)
    self.b2.pack(side=LEFT)

  def save(self):
    global programDir
    self.original.save("image_stretcher" + str(id(self.original)) + ".png", "PNG")

  def __init__(self, master):
    global imageName
    Frame.__init__(self, master)
    self.original = Image.open(imageName)
    image = ImageTk.PhotoImage(self.original)

    self.w = Canvas(master, width=self.original.width,
                    height=self.original.height)
    self.w.grid(row=1, column=0)
    self.w.create_image(0, 0, image=image, anchor=NW, tags="IMG")
    self.w.img = image
    self.w.pack()

    self.l1 = Label(master, text="Height:")
    self.l1.grid(row=2, column=0)
    self.l1.pack(side=LEFT)

    self.e1 = Entry(master)
    self.e1.insert(0, str(self.original.height))
    self.e1.grid(row=2, column=1)
    self.e1.pack(side=LEFT)

    self.l2 = Label(root, text="Width:")
    self.l2.grid(row=2, column=2)
    self.l2.pack(side=LEFT)

    self.e2 = Entry(master)
    self.e2.insert(0, str(self.original.width))
    self.e2.grid(row=2, column=3)
    self.e2.pack(side=LEFT)

    self.b1 = Button(master, text="Stretch", fg="blue", command=self.resize)
    self.b1.grid(row=2, column=4)
    self.b1.pack(side=LEFT)

    self.b2 = Button(root, text="Save", fg="black", command=self.save)
    self.b2.grid(row=2, column=5)
    self.b2.pack(side=LEFT)


root = Tk()  # Makes the window
# Makes the title that will appear in the top left
root.wm_title("Dillon Seam Carver")
root.config(background="#FFFFFF")  # sets background color to white

app = App(root)
app.mainloop()

# put widgets here

# start monitoring and updating the GUI. Nothing below here runs.
app.destroy()
