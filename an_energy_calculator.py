from PIL import Image


class the_energy_calculator():
  """What does this class do?
  1.) It contains a function that when given an image it returns a matrix of
  doubles or integers? (idk Python doesn't care) that are the energies of each individual pixel within the image."""

  def deltaSquared(self, tuple1, tuple2):
    if (len(tuple1) == 4):
      (r1, g1, b1, opac1) = tuple1
    elif (len(tuple1) == 3):
      (r1, g1, b1) = tuple1
    if (len(tuple2) == 4):
      (r2, g2, b2, opac2) = tuple2
    elif (len(tuple1) == 3):
      (r2, g2, b2) = tuple2
    r_delta = r1 - r2
    g_delta = g1 - g2
    b_delta = b1 - b2
    return ((r_delta ** 2) + (g_delta ** 2) + (b_delta ** 2))

  def getUp(self, givenX, givenY, w, h):
    if (givenY + 1 >= h):
      return (givenX, 0)
    return (givenX, givenY)

  def getDown(self, givenX, givenY, w, h):
    if (givenY - 1 < 0):
      return (givenX, h - 1)
    return (givenX, givenY)

  def getRight(self, givenX, givenY, w, h):
    if (givenX + 1 >= w):
      return (0, givenY)
    return (givenX, givenY)

  def getLeft(self, givenX, givenY, w, h):
    if (givenY - 1 < 0):
      return (w - 1, givenY)
    return (givenX, givenY)

  def getEnergies(self, givenImage, w, h):
    Matrix = [[0 for x in range(
        w)] for y in range(h)]

    pix = givenImage.load()
    for curX in range(w):
      for curY in range(h):
        """ Directions:
                    U - Up
                    D - Down
                    R - Right
                    L - Left"""
        x_energy = self.deltaSquared(
            pix[self.getRight(curX, curY, w, h)], pix[self.getLeft(curX, curY, w, h)])
        y_energy = self.deltaSquared(
            pix[self.getUp(curX, curY, w, h)], pix[self.getDown(curX, curY, w, h)])

        Matrix[curY][curX] = x_energy + y_energy
    return Matrix
