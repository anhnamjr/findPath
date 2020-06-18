
import matplotlib.pyplot as plt
import fileMethod as file
import aStar
import BFS
import DFS
import Draw
import CheckPoints as cp 


if __name__ == "__main__":
    # doc file lay thong tin ban do
    map = input("Choose map (1, 2, 3, 4): ")
    mapData = file.readFileData("map" + map + ".txt")
    mode = int(input("Choose Algorithm: \n1: A*\n2: BFS\n3: DFS\n4: Check Points\nYour choice: "))
    path = []
    cost = 0
    method = aStar.aStarMethod(mapData.obstacles)

    # A star
    if mode == 1:      
        path, cost = aStar.aStartAlgorithm(mapData, method)
        if path == None and cost == None:
            print("A* failed in find a path to end point")
        file.writeFile(mapData, path, cost)

    # BFS
    elif mode == 2:         
        path, cost = BFS.BFSFunc(mapData)
        if path == None and cost == None:
            print("BFS failed in find a path to end point")
        file.writeFile(mapData, path, cost)

    # DFS
    elif mode == 3:     
        path, cost = DFS.DFSFunc(mapData)
        if path == None and cost == None:
            print("DFS failed in find a path to end point")
        else:
            file.writeFile(mapData, path, cost)
    
    # A* checkpoints
    elif mode == 4:     
        path, cost = cp.findPathPriority(mapData, method)
        if path == None and cost == None:
            print("A* failed in find a path from start to check points and end point")
        file.writeFile(mapData, path, cost)
    # in cost ra man hinh
    print("cost: ", cost)
    # goi ham ve
    Draw.drawGraph(mapData, path)


