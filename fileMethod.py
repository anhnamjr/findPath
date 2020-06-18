import aStar

class createMap():
    def __init__(self, space, start, end, checkPoints, obstacles):
        self.space = space
        self.start = start
        self.end = end
        self.checkPoints = checkPoints
        self.obstacles = obstacles

        
# Ham doc file lay data
def readFileData(filename):
    f = open(filename, "r")

    # lay gioi han khong gian space
    spaceRaw = f.readline().replace("\n", "").split(",")
    space = (int(spaceRaw[0]), int(spaceRaw[1]))
    # Lay toa diem diem dau va cuoi
    SEPoint = f.readline().replace("\n", "").split(",")
    startPoint = (int(SEPoint[0]), int(SEPoint[1]))
    endPoint = (int(SEPoint[2]), int(SEPoint[3]))
    
    # Lay toa do cac checkpoints
    checkPoints = []
    begin = 4
    while begin < len(SEPoint):
        checkPoints.append((int(SEPoint[begin]), int(SEPoint[begin + 1])))
        begin += 2
    #print(checkPoints)
    # Lay so luong vat can
    obstacleQuantity = int(f.readline().replace("\n", ""))

    # Lay toa do cac vat can
    number = 0
    obstaclesRaw = []   # chua dinh cac vat can
    while number < obstacleQuantity:
        toado = (f.readline().replace("\n", "").split(","))

        # Bien cac toa do vat can thanh cac node
        i = 0
        tempArray = []
        while i < len(toado):
            tempArray.append((int(toado[i]), int(toado[i+1])))
            i += 2
        obstaclesRaw.append(tempArray)
        number += 1

    # close file
    f.close()
    obstacles = aStar.pointToSharp(obstaclesRaw)
    map = createMap(space, startPoint, endPoint, checkPoints, obstacles)
    return map


def writeFile(map, path, cost):      # truyen map va path vao de ghi
    f = open("output.txt", "w")
    f.write(str(map.space[0]) + "," + str(map.space[1]) + "\n")           # ghi gioi han khong gian
    # ghi toa do diem dau, cuoi
    f.write(str(map.start[0]) + "," + str(map.start[1]) + "," + str(map.end[0]) + "," + str(map.end[1]) + "\n")
    for i in map.checkPoints:     # ghi toa do vat can
        if(i == map.checkPoints[len(map.checkPoints) - 1]):
            f.write(str(i[0]) + "," + str(i[1])) 
        else:
            f.write(str(i[0]) + "," + str(i[1]) + ",") 
    f.write("\n")
    for i in map.obstacles:     # ghi toa do vat can
        if(i == map.obstacles[len(map.obstacles) - 1]):
            f.write(str(i[0]) + "," + str(i[1])) 
        else:
            f.write(str(i[0]) + "," + str(i[1]) + ",") 
    f.write("\n")
    if path != None:
        for i in path:              # ghi toa do duong di
            if(i == path[len(path) - 1]):
                f.write(str(i[0]) + "," + str(i[1])) 
            else:
                f.write(str(i[0]) + "," + str(i[1]) + ",")    # ghi duong di
    if cost != None:
        f.write("\n" + str(cost))
    f.close()                       # dong file
