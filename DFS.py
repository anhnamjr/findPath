import BFS

def DFSFunc(map):
    parents = []           # bien luu lai cac diem truoc do
    for i in range(1, map.space[0]):
        for j in range(1, map.space[1]):
            parents.append(((i, j), None))
    parents = dict(parents)

    def DFSRecursion(start):  # de quy DFS
        neighbours = BFS.getNeighbours(start, map.space, map.obstacles)
        for neighbour in neighbours:        # xet cac diem xung quanh
            if parents[neighbour] == None:  # neu chua di qua diem nay
                parents[neighbour] = start  # luu lai duong di
                if neighbour == map.end:
                    return True
                elif DFSRecursion(neighbour):
                    return True
        return False

    if (DFSRecursion(map.start)):
        return BFS.drawPath(parents, map.start, map.end)
    else:
        return None, None
