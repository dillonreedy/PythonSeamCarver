from point import Point
from PIL import Image, ImageTk

# Given the original image, and the path through that image, expand the
# original image by 1 pixel.


class the_image_expander():

  def GetLeftPixel(self, currentLoc, w):
    if (currentLoc.x - 1 < 0):
      return Point(w - 1, currentLoc.y)
    return Point(currentLoc.x - 1, currentLoc.y)

  def GetRightPixel(self, currentLoc, w):
    if (currentLoc.x + 1 >= w):
      return Point(0, currentLoc.y)
    return Point(currentLoc.x + 1, currentLoc.y)

  def GetAveragedPixel(self, leftPixel, rightPixel):
  	(rL, gL, bL, opacL) = leftPixel
    (rR, gR, bR, opacR) = rightPixel
    avg_r = (rL + rR) / 2
    avg_g = (gL + gR) / 2
    avg_b = (bL + bR) / 2
    return (avg_r, avg_g, avg_b, opacL)

  def GetWidthStretchImage(self, originalImage, path):
    # Make a copy of the original image
    # Resize the copy of the image to be size (width+1, height)
    # For each column in images pixels:
    #		foundPathThisRow = False
    #		For each row in images pixels:
    #			if (foundPathThisRow):
    imageCopy = originalImage
    imageCopy = imageCopy.resize(
        (originalImage.width + 1, originalImage.height), Image.ANTIALIAS)

    pixOriginal = originalImage.load()
    pixCopy = imageCopy.load()

    for somePt in Path:
    	leftPixelLoc = GetLeftPixel(somePt, originalImage.width)
    	rightPixelLoc = GetRightPixel(somePt, originalImage.width)
    	pixCopy[somePt.x, somePt.y] = GetAveragedPixel(pixOriginal[leftPixelLoc.x, leftPixelLoc.y], pixOriginal[rightPixelLoc.x, rightPixelLoc.y])

    Path.sort()
    for x in Range(imageCopy.width):
    	currentPathSkip = Path.pop()
    	hitPathSkip = False
    	for y in Range(imageCopy.height):
    		if (x!=currentPathSkip.x && y!=currentPathSkip):
    			if (hitPathSkip):
    				pixCopy[x, y] = pixOriginal[x - 1, y]
    			else:
    				pixCopy[x, y] = pixOriginal[x, y]
    		else:
    			hitPathSkip = True

    return imageCopy
