import cv2
import numpy as np 
#vẽ hình chữ nhật không có fill
def box(img,p,color):
    cv2.rectangle(img,(31*p[0]+1,31*p[1]+1),(31*p[0]+30,31*p[1]+30),color,-1)

#vẽ hình chữ nhật có fill
def rect(img,p,color,m):
    box(img,(p[0],m-p[1]),color)

#Vẽ background
def Background(m,n,img):
    for i in range(n + 1):
        for j in range (m + 1):
            rect(img, (i, j), (255,255,255), m)
    for i in range(n+1):
        cv2.line(img,(31*i+31,0),(31*i+31,(m+2)*31),(0,0,0),1)
        box(img,(i,0),(100,100,100))
        box(img,(i,m),(100,100,100))
    for i in range(m+1):
        cv2.line(img,(0,31*i+31),(31*(n+2),31*i+31),(0,0,0),1)
        box(img,(0,i),(100,100,100))
        box(img,(n,i),(100,100,100))

#vẽ đồ thị và đường đi
def drawGraph(map, path):
    m = map.space[1]
    n = map.space[0]
    img=np.zeros(((m+1)*31,(n+1)*31,3), np.uint8)
    Background(m,n,img)

    #Vật cản màu vàng:
    for i in map.obstacles:
        rect(img,i,(41,128,185) , m)
    #Đường đi màu đỏ: 
    if path:
        for i in path:
            rect(img,i,(0,0,255),m)

    # Điểm start màu xanh lá cây:
    rect(img, map.start, (46,204,113), m)

    #Điềm goal màu 
    rect(img, map.end, (82,25,7), m)

    #Điểm đón màu xanh dương
    for i in map.checkPoints:
        rect(img,i,(241,196,15),m)


    cv2.imshow("Graph Path ",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()