
def lineLow(x0, y0, x1, y1, line):
    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    if (dy < 0):
        yi = -1
        dy = -dy
    
    d = 2*dy - dx
    y = y0

    for x in range(x0, x1):
        line.append((x, y))
        if d > 0:
            y = y + yi
            d = d - 2*dx
        d = d + 2*dy
    


def lineHigh(x0, y0, x1, y1, line):
    dx = x1 - x0
    dy = y1 - y0
    xi = 1;
    if dx < 0:
        xi = -1
        dx = -dx
    
    d = 2*dx - dy
    x = x0

    for y in range(y0, y1):
        line.append((x, y))
        if d > 0:
            x = x + xi
            d = d - 2*dy
        d = d + 2*dx
    

def drawLine(x0, y0, x1, y1):
    line = []
    if abs(y1 - y0) < abs(x1 - x0):
        if x0 > x1:
            lineLow(x1, y1, x0, y0, line)
        else:
            lineLow(x0, y0, x1, y1, line)
        
    else:
        if y0 > y1:
            lineHigh(x1, y1, x0, y0, line)
        else:
            lineHigh(x0, y0, x1, y1, line)
    return line

    # ve hinh tu cac dinh, tra ve mang toa do cac diem tren canh
def pointToSharp(obstacles):
    sharp = []
    for obstacle in obstacles:
        i = 0
        while i < len(obstacle) - 1:    # ve duong thang tu diem dau den cac diem sau
            sharp.extend(drawLine(obstacle[i][0], obstacle[i][1], obstacle[i + 1][0], obstacle[i + 1][1]))
            i += 1
        # ve duong thang tu diem cuoi den diem dau tien
        sharp.extend(drawLine(obstacle[len(obstacle) - 1][0], obstacle[len(obstacle) - 1][1], obstacle[0][0], obstacle[0][1]))
        for point in obstacle:
            if sharp.count(point) == 0:
                sharp.append(point)
            
    return sharp


class aStarMethod():
    def __init__(self, obstacles):
        self.obstacles = []
        for i in obstacles:
            self.obstacles.append(i)

    def heuristicFunc(self, pos, end):
        H = 1
        H2 = 1
        dx = abs(pos[0] - end[0])
        dy = abs(pos[1] - end[1])
        return H * (dx + dy) + (H2 - 2 * H) * min(dx, dy)

    def getNeighbours(self, pos, space, obstacles):  # lay toa do 8 diem ben canh diem hien tai
        neighbours = []
        for dx, dy in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
            x = pos[0] + dx
            y = pos[1] + dy
            if x < 1 or x >= space[0] or y < 1 or y >= space[1]:
                continue
            elif obstacles.count((x, y)) != 0:      # neighbour trung voi vat can
                continue
            neighbours.append((x, y))
        return neighbours

    def cost(self, currentPos, newPos):
        distance = abs(newPos[0] - currentPos[0]) + abs(newPos[1] - currentPos[1])
        if(distance == 1):   # di thang
            return 1
        return 1.5      # di cheo


def aStartAlgorithm(map, method):

    G = {}  # chi phi thuc te di tu start -> current
    F = {}  # chi phi uoc tinh di tu current -> end
    G[map.start] = 0
    F[map.start] = method.heuristicFunc(map.start, map.end)
    closedSet = set()
    openSet = set([map.start])
    parent = {}

    while len(openSet) > 0:
        # lay dinh trong tap mo voi chi phi thap nhat
        current = None
        currentFcost = None
        for pos in openSet:
            if current is None or F[pos] < currentFcost:
                currentFcost = F[pos]
                current = pos

        # Kiem tra co phai la dich (end)
        if current == map.end:
            path = [current]
            while current in parent:
                current = parent[current]
                path.append(current)
            path.reverse()
            return path, F[map.end]  # Done!

        # Dua vao tap dong
        openSet.remove(current)
        closedSet.add(current)

        # tinh chi phi cho nhung diem neighbour
        for neighbour in method.getNeighbours(current, map.space, map.obstacles):
            if neighbour in closedSet:
                continue  # khong can xet diem trong tap dong
            candidateG = G[current] + method.cost(current, neighbour)

            if neighbour not in openSet:
                openSet.add(neighbour)  # them diem moi vao tap mo
                
            elif candidateG >= G[neighbour]:
                continue  # bo qua neu chi phi lon

            parent[neighbour] = current
            G[neighbour] = candidateG
            H = method.heuristicFunc(neighbour, map.end)
            F[neighbour] = G[neighbour] + H
    return None, None