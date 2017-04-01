from point import Point
from PIL import Image, ImageTk


# Given the original image, and the path through that image, expand the
# original image by 1 pixel.


class the_image_resizer():

  def GetLeftPixel(self, currentLoc, w):
    if (currentLoc.x - 1 < 0):
      return Point(w - 1, currentLoc.y)
    return Point(currentLoc.x - 1, currentLoc.y)

  def GetRightPixel(self, currentLoc, w):
    if (currentLoc.x + 1 < w):
      return Point(currentLoc.x + 1, currentLoc.y)
    return Point(0, currentLoc.y)

  def GetAveragedPixel(self, leftPixel, rightPixel):
    if (len(leftPixel) == 4):
      (rL, gL, bL, opacL) = leftPixel
    elif (len(leftPixel) == 3):
      (rL, gL, bL) = leftPixel
    if (len(rightPixel) == 4):
      (rR, gR, bR, opacR) = rightPixel
    elif (len(leftPixel) == 3):
      (rR, gR, bR) = rightPixel
    avg_r = (rL + rR) / 2
    avg_g = (gL + gR) / 2
    avg_b = (bL + bR) / 2
    if (len(leftPixel) == 3):
      return (avg_r, avg_g, avg_b)
    elif (len(leftPixel) == 4):
      return (avg_r, avg_g, avg_b)

  def GetWidthShrinkImage(self, originalImage, Path):
    imageCopy = originalImage
    imageCopy = imageCopy.resize(
        (originalImage.width - 1, originalImage.height), Image.ANTIALIAS)

    pixOriginal = originalImage.load()
    pixCopy = imageCopy.load()

    for y in range(imageCopy.height):
      hitPathSkip = False
      for x in range(imageCopy.width):
        if (not self.InSkipPath(Path, Point(x, y))):
          if (hitPathSkip):
            pixCopy[x, y] = pixOriginal[x + 1, y]
          else:
            pixCopy[x, y] = pixOriginal[x, y]
        else:
          hitPathSkip = True

    return imageCopy

  def InSkipPath(self, skipPath, currentPt):
    for skipPt in skipPath:
      if (currentPt.x == skipPt.x and currentPt.y == skipPt.y):
        return True
    return False

  def GetWidthStretchImage(self, originalImage, Path):
    imageCopy = originalImage
    imageCopy = imageCopy.resize(
        (originalImage.width + 1, originalImage.height), Image.ANTIALIAS)

    pixOriginal = originalImage.load()
    pixCopy = imageCopy.load()

    for somePt in Path:
      leftPixelLoc = self.GetLeftPixel(somePt, originalImage.width)
      rightPixelLoc = self.GetRightPixel(somePt, originalImage.width)
      pixCopy[somePt.x, somePt.y] = self.GetAveragedPixel(pixOriginal[
          leftPixelLoc.x, leftPixelLoc.y], pixOriginal[rightPixelLoc.x, rightPixelLoc.y])

    for y in range(imageCopy.height):
      hitPathSkip = False
      for x in range(imageCopy.width):
        if (not self.InSkipPath(Path, Point(x, y))):
          if (hitPathSkip):
            pixCopy[x, y] = pixOriginal[x - 1, y]
          else:
            pixCopy[x, y] = pixOriginal[x, y]
        else:
          hitPathSkip = True

    return imageCopy
