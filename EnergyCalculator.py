from PIL import Image


class TheEnergyCalculator():
	"""What does this class do? 1.) It contains a function that when given an image it returns a matrix of doubles or integers? (idk Python doesn't care) that are the energies of each individual pixel within the image."""
    def DeltaSquared(self, tuple1, tuple2):
    	(r1, g1, b1, opac1) = tuple1
        (r2, g2, b2, opac2) = tuple2
        r_delta = r1 - r2
        g_delta = g1 - g2
        b_delta = b1 - b2
        return ((r_delta ** 2) + (g_delta ** 2) + (b_delta ** 2))

    def GetEnergies(self, givenImage):
        w = givenImage.size[0]
        h = givenImage.size[1]

        self.Matrix = [[0 for self.x in range(
            self.givenImage.size[0])] for self.y in range(0, self.givenImage.size[1])]

        pix = givenImage.load()
        for curX in range(0, self.w):
            for curY in range(0, self.h):
                """ Directions:
                            U - Up
                            D - Down
                            R - Right
                            L - Left"""
                x_energy = DeltaSquared(
                    pix[curX + 1, curY], pix[curX - 1, curY])
                y_energy = DeltaSquared(
                    pix[curX, curY + 1], pix[curX, curY - 1])
                self.Matrix[curX, curY] = x_energy + y_energy
        print self.Matrix


someEnergies = TheEnergyCalculator()
someEnergies.GetEnergies()
