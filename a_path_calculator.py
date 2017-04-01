from point import Point
import sys

"""
What this class should do?
Given a matrix of integers, the height (indexing from 0 to h-1), and width (indexing from 0 to w-1)
return back a list of points [point1, point2..., point_h]
This path is a path of minimum energy difference.
The edges may only move left-down, down, and right-down.
"""

"""
There are 3 things we have to maintain to get our path:
1. Our matrix of given energies:
[1, 2, 10, 11]
[3, 4, 14, 12]
[0, 1, 13, 15]

2. Our dynamically programmed summed up graphs:
At initialization:
[1, 2, 10, 11]
[0, 0, 0, 0]
[0, 0, 0, 0]
Starting on the 1st row, 0th column:
[1, 2, 10, 11]
[4, 0, 0, 0]
[0, 0, 0, 0]
After doing the entire 2nd row:
[1, 2, 10, 11]
[4, 5, 16, 22]
[0, 0, 0, 0]
After doint the 3rd row:
[1, 2, 10, 11]
[4, 5, 16, 22]
[4, 5, 18, 31]

3. A matrix of points that tell you what path to take:
At initialization:
[(-1, -1), (-1, -1), (-1, -1), (-1, -1)]
[(-1, -1), (-1, -1), (-1, -1), (-1, -1)]
[(-1, -1), (-1, -1), (-1, -1), (-1, -1)]
After the summation gets put in on 1st row, 0th column, we then put in the point that we chose at the 1st row, 0th column:
[(-1, -1), (-1, -1), (-1, -1), (-1, -1)]
[(0, 0), (-1, -1), (-1, -1), (-1, -1)]
[(-1, -1), (-1, -1), (-1, -1), (-1, -1)]
After doing the entire 2nd row:
[(-1, -1), (-1, -1), (-1, -1), (-1, -1)]
[(0, 0), (0, 0), (1, 0), (2, 0)]
[(-1, -1), (-1, -1), (-1, -1), (-1, -1)]
After doing the entire 3rd row:
[(-1, -1), (-1, -1), (-1, -1), (-1, -1)]
[(0, 0), (0, 0), (1, 0), (2, 0)]
[(0, 1), (0, 1), (1, 1), (2, 1)]

4. We now need the point of the minimum
  4.1 Get the last row
  4.2 Get the minimum value of the last row
  4.3 Iterate through and return the first value equal to the minimum (at i)
    A point (ith, row num)

5.

"""


class the_path_calculator():

  def getPointsAbove(self, givenPt, w, h):
    ptsLis = []
    ptsLis.append(Point(givenPt.x - 1, givenPt.y))
    if (givenPt.y + 1 < w):
      ptsLis.append(Point(givenPt.x - 1, givenPt.y + 1))
    if (givenPt.y - 1 > -1):
      ptsLis.append(Point(givenPt.x - 1, givenPt.y - 1))
    return ptsLis

  def getMinVal(self, givenLis):
    minVal = sys.maxint
    for curVal in givenLis:
      if (curVal < minVal):
        minVal = curVal
    return minVal

  def getStartPt(self, givenLis, givenMin, w, h):
    for i in range(w):
      if (givenLis[i] == givenMin):
        return Point(h - 1, i)
    return Point(-1, -1)

  def transposePath90(self, givenPath):
    # Flippint the x and y values, because I legitimately don't know why
    flippedPath = []
    for pt in givenPath:
      flippedPath.append(Point(pt.y, pt.x))
    return flippedPath

  def getPath(self, givenEnergyMatrix, w, h):
    dynamicMat = [[givenEnergyMatrix[0][x] if (y == 0) else 0 for x in range(
        w)] for y in range(h)]

    pointsMat = [[Point(-1, -1) for x in range(
        w)] for y in range(h)]

    """Matrix[r][c]"""
    for curRow in range(1, h):
      for curCol in range(w):
        curPtsLis = self.getPointsAbove(Point(curRow, curCol), w, h)
        minVal = sys.maxint
        for pt in curPtsLis:
          if (dynamicMat[pt.x][pt.y] < minVal):
            minVal = dynamicMat[pt.x][pt.y]

        for pt in curPtsLis:
          if (minVal == dynamicMat[pt.x][pt.y]):
            dynamicMat[curRow][curCol] = givenEnergyMatrix[
                curRow][curCol] + dynamicMat[pt.x][pt.y]
            pointsMat[curRow][curCol] = pt

    leastPathVal = self.getMinVal(dynamicMat[h - 1])
    curPt = self.getStartPt(dynamicMat[h - 1], leastPathVal, w, h)

    thePath = []
    thePath.append(Point(curPt.x, curPt.y))
    while (curPt.x != -1 and curPt.y != -1):
      curPt = pointsMat[curPt.x][curPt.y]
      if (curPt.x != -1 and curPt.y != -1):
        thePath.append(curPt)
    return thePath
