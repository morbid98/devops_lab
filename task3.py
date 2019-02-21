if __name__ == '__main__':
    canvasW = int(input("canvas width "))
    while canvasW <= 1:
        canvasW = int(input("wrong canvas width, try more "))
    canvasH = int(input("canvas height "))
    while canvasH >= 100:
        canvasH = int(input("wrong canvas height, try more "))
    canvasSize = canvasW*canvasH
    print("Canvas size: %d\n" % canvasSize)
    rectNum = int(input("number of rectangles\n"))
    while rectNum >= 5000 or rectNum < 0:
        print("wrong height, try again\n")
        rectNum = int(input("wrong rectangles' number, try more"))
    for coord in range(rectNum):
        print("Enter the coordinates for the rectangle number %d" % coord)
        a = "Input coords of the upper left corner (x first, y second)"
        b = "Input coords of the lower right corner (x first, y second)"
        coordULCx, coordULCy = [int(c) for c in input(a).split()]
        coordLRCx, coordLRCy = [int(c) for c in input(b).split()]
        height = coordLRCy-coordULCy
        width = coordLRCx-coordULCx
        square = width*height
        canvasSize -= square
    else:
        print("Empty space is %d" % canvasSize)
