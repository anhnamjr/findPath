import queue

def getNeighbours(pos, space, obstacles):  # lay toa do 8 diem ben canh diem hien tai
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

def drawPath(parents, start, end):
    path = []
    cost = 0
    currentPos = end
    while currentPos != start:
        currentPos = parents[currentPos]
        cost += moveCost(currentPos, parents[currentPos])
        path.append(currentPos)
    return path[::-1], cost

def moveCost(currentPos, newPos):
        if(newPos == None):
            return 0
        distance = abs(newPos[0] - currentPos[0]) + abs(newPos[1] - currentPos[1])
        if(distance == 1):   # di thang
            return 1
        return 1.5           # di cheo

def BFSFunc(map):
    all = queue.deque()       # khoi tao queue
    all.append(map.start)         # them start vao queue

    parents = []           # bien luu lai cac diem truoc do
    for i in range(1, map.space[0]):
        for j in range(1, map.space[1]):
            parents.append(((i, j), None))
    parents = dict(parents)

    while True:
        if(len(all) == 0):
            return None, None
        currentPos = all.popleft()
        neighbours = getNeighbours(currentPos, map.space, map.obstacles)
        for neighbour in neighbours:               # xet cac diem xung quanh
            if parents[neighbour] == None:         # chua di qua diem nay
                all.append(neighbour)
                parents[neighbour] = currentPos    # luu lai duong di
                if neighbour == map.end:
                    return drawPath(parents, map.start, map.end)
