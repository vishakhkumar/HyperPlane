import math
import time


def matmult(Y,X):

    result = [[0],[0],[0],[0]]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] = result[i][j] + (X[i][k]*Y[k][j])
    return result


def rotationHelp():
    string =( "\n"
     "+-             -+     +-              -+     +-              -+\n"
     "| cosT sinT 0 0 |     | 1   0    0   0 |     | cosT 0 -sinT 0 |\n"
     "|-sinT cosT 0 0 |     | 0  cosT sinT 0 |     |  0   1   0   0 |\n"
     "|  0    0   1 0 |     | 0 -sinT cosT 0 |     | sinT 0  cosT 0 |\n"
     "|  0    0   0 1 |     | 0   0    0   1 |     |  0   0   0   1 |\n"
     "+-             -+     +-              -+     +-              -+\n"
     "    XY Plane               YZ Plane                ZX Plane\n"
     "\n"
     "\n"
    "+-             -+     +-              -+     +-              -+\n"
    "| cosT 0 0 sinT |     | 1  0   0   0   |     | 1 0  0     0   |\n"
    "|  0   1 0  0   |     | 0 cosT 0 -sinT |     | 0 1  0     0   |\n"
    "|  0   0 1  0   |     | 0  0   1   0   |     | 0 0 cosT -sinT |\n"
    "|-sinT 0 0 cosT |     | 0 sinT 0  cosT |     | 0 0 sinT  cosT |\n"
    "+-             -+     +-              -+     +-              -+\n"
    "    XW Plane               YW Plane                ZW Plane\n")
    print string


def distance(x,y):
    if len(x)!=len(y):
        return
        # ensuring that the vectors are of the same dimension. If not, returns None.
        
    sum = 0
    for i in range(len(x)):
        sum = sum + ((x[i]-y[i]))**2
    return math.sqrt(sum)
    # sum is the distance between.

def rotateMatrix(x,gauss,plane): #O is the gauss
    gauss = gauss*math.pi/180
    rotationMatrix ={
    'XY' : lambda gauss : [[math.cos(gauss),math.sin(gauss),0,0],[-math.sin(gauss),math.cos(gauss),0,0],[0,0,1,0],[0,0,0,1]],
    'YZ' : lambda gauss : [[1,0,0,0],[0,math.cos(gauss),math.sin(gauss),0],[0,-math.sin(gauss),math.cos(gauss),0],[0,0,0,1]],
    'ZX' : lambda gauss : [[math.cos(gauss),0,-math.sin(gauss),0],[0,1,0,0],[math.sin(gauss),0,math.cos(gauss),0],[0,0,0,1]],
    'XW' : lambda gauss : [[math.cos(gauss),0,0,math.sin(gauss)],[0,1,0,0],[0,0,1,0],[-math.sin(gauss),0,0,math.cos(gauss)]],
    'YW' : lambda gauss : [[1,0,0,0],[0,math.cos(gauss),0,-math.sin(gauss)],[0,0,1,0],[0,math.sin(gauss),0,math.cos(gauss)]],
    'ZW' : lambda gauss : [[1,0,0,0],[0,1,0,0],[0,0,math.cos(gauss),-math.sin(gauss)],[0,0,math.sin(gauss),math.cos(gauss)]]
    }[plane](gauss)
    pikapika=matmult(x,rotationMatrix)
    return pikapika

def reduce(vector):
    
    pw = 3
    
    vector = [vector[0]*pw/(pw-vector[3]),
              vector[1]*pw/(pw-vector[3]),
              vector[2]*pw/(pw-vector[3])]


    k = len(vector)

    return vector[0:k]


def whichLines(minDistance, listing):
    for i in range(len(listing)):
        for j in range(len(listing)):
            if (i!=j)and(distance(listing[i],listing[j])<=2.1):
                has = reduce(listing[i])
                ash = reduce(listing[j])


                stroke(102, 204, 0);
                pushMatrix()
                translate(has[0]*101,has[1]*101,has[2]*101)    
                box(5)
                popMatrix()
                
                stroke(204, 102, 0);
                pushMatrix()
                translate(ash[0]*100,ash[1]*100,ash[2]*100)
                box(5)
                popMatrix()
                
                line(has[0]*101,has[1]*101,has[2]*101,ash[0]*100,ash[1]*100,ash[2]*100)
    
    return

#global variables - do not fuck up!!!!!
# listPoints = [[-100,-100,-100,-100],[-100,-100,-100,100],[-100,-100,100,-100],[-100,-100,100,100],[-100,100,-100,-100],[-100,100,-100,100],[-100,100,100,-100],[-100,100,100,100],[100,-100,-100,-100],[100,-100,-100,100],[100,-100,100,-100],[100,-100,100,100],[100,100,-100,-100],[100,100,-100,100],[100,100,100,-100],[100,100,100,100]]
# listPoints = [[100,100,100,100],[-100,-100,-100,-100],[40,-40,40,40]]
# listPoints = [[100,100,100,100],[100,100,100,300],[100,100,300,100],[100,100,300,300],[100,300,100,100],[100,300,100,300],[100,300,300,100],[100,300,300,300],[300,100,100,100],[300,100,100,300],[300,100,300,100],[300,100,300,300],[300,300,100,100],[300,300,100,300],[300,300,300,100],[300,300,300,300]]
listPoints = [[-1,-1,-1,-1],[-1,-1,1,-1],[-1,1,-1,-1],[-1,1,1,-1],[1,-1,-1,-1],[1,-1,1,-1],[1,1,-1,-1],[1,1,1,-1],[-1,-1,-1,1],[-1,-1,1,1],[-1,1,-1,1],[-1,1,1,1],[1,-1,-1,1],[1,-1,1,1],[1,1,-1,1],[1,1,1,1]]       
angle = 0.4
mika = True

def setup():
    #rotationHelp()
    size(700, 700, P3D);
    background(255);
    angle = 5

def draw():
    background(255);
    maty=listPoints
    global angle
    global listPoints
    global mika
    for i in range(len(listPoints)):
        pikachu = [[listPoints[i][0]],[listPoints[i][1]],[listPoints[i][2]],[listPoints[i][3]]]
        #pikachu = rotateMatrix(pikachu,angle,'XY')
        # pikachu = rotateMatrix(pikachu,angle,'ZX')
        pikachu = rotateMatrix(pikachu,angle,'XW')
        # pikachu = rotateMatrix(pikachu,angle,'XY')
        # pikachu = rotateMatrix(pikachu,angle,'YZ')
        pikachu = rotateMatrix(pikachu,angle,'ZW')
        for g in range(len(listPoints[0])):
            maty[i][g]=pikachu[g][0]
    print "\n"
    listPoints=maty
    '''
    if mika:
        angle = angle + 0.01
    else:
        angle = angle - 0.01
    if (angle<-1)or(angle>1):
        mika=not mika
    '''
    pushMatrix()

    translate(300,300,-500)
    whichLines(200,maty)
    popMatrix()

    '''
