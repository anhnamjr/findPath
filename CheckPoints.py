import fileMethod as file
import aStar
#import Draw

def aStartAlgorithm2(start, goal, map, method):

    G = {}  # chi phi thuc te di tu start -> current
    F = {}  # chi phi uoc tinh di tu current -> end
    G[start] = 0
    F[start] = method.heuristicFunc(map.start, map.end)
    closedSet = set()
    openSet = set([start])
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
        if current == goal:
            path = [current]
            while current in parent:
                current = parent[current]
                path.append(current)
            path.reverse()
            return path, F[goal]  # Done!

        # Dua vao tap dong
        openSet.remove(current)
        closedSet.add(current)

        # tinh chi phi cho nhung diem neighbour
        for neighbour in method.getNeighbours(current, map.space, map.obstacles):
            if neighbour in closedSet:
                continue  # khong can xet diem trong tap dong
            candidateG = G[current] + method.cost(current, neighbour)

            if neighbour not in openSet:
                openSet.add(neighbour)  # them diem moi vao tap dong de xet
            elif candidateG >= G[neighbour]:
                continue                # neu chi phi lon thi bo qua

            
            parent[neighbour] = current
            G[neighbour] = candidateG
            H = method.heuristicFunc(neighbour, goal)
            F[neighbour] = G[neighbour] + H
    return None, None

#Tìm thứ tự ưu tiên của các điểm đón
def findPriority(map, method):
	res = [map.end]
	index = 0
	checkPoints = []
	for j in map.checkPoints:
		checkPoints += [j]

	while(len(checkPoints) != 1):
		temp = []
		for value in checkPoints:
			path, cost = aStartAlgorithm2(res[index],value,map, method)
			if cost == None and path == None:
				return None
			temp += [cost]

		for i in range(0,len(temp)):
			if min(temp) == temp[i]:
				res.insert(0,checkPoints[i])
				checkPoints.remove(checkPoints[i])		
				break
	res.insert(0, checkPoints[0])
	res.insert(0, map.start)
	return res

#Tìm đường đi qua các điểm đón
def findPathPriority(map, method):
	PriorityPoint = findPriority(map, method)
	res = []
	sumCost = 0
	for i in range(len(PriorityPoint) - 1):
		tempRes, cost = aStartAlgorithm2(PriorityPoint[i], PriorityPoint[i+1], map, method)
		if tempRes == None:
			return None, None
		tempRes.pop()
		res.extend(tempRes)
		sumCost += cost

	res.append(map.end)
	return res, sumCost

