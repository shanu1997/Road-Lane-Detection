import cv2
import numpy
def region(i,v):
    m=numpy.zeros_like(i)
    cv2.fillPoly(m,v,255)
    return cv2.bitwise_and(i,m)
def dl(i,l):
    i=numpy.copy(i)
    bi=numpy.zeros((i.shape[0],i.shape[1],3),dtype=numpy.uint8)
    for line in l:
        for x1,y1,x2,y2 in line:
            cv2.line(bi,(x1,y1),(x2,y2),(255,255,255),thickness=1)
    return cv2.addWeighted(i,0.5,bi,1,0)
def main(i):
    print('shape=',i.shape,'length=',len(i))
    return dl(
        i,cv2.HoughLinesP(
        region(
        cv2.Canny(
            cv2.cvtColor
            (i,cv2.COLOR_RGB2GRAY),100,150),
        numpy.array(
            [
                [
                    (0,i.shape[0]),(i.shape[1]/2,i.shape[0]/2),(i.shape[1],i.shape[0])
                ]
            ],numpy.int32
        )
    ),rho=1,theta=numpy.pi/180,threshold=80,lines=numpy.array([]),minLineLength=100,maxLineGap=100
    )
              )

#_______________________________________________________________add name of youre video file here_____________________________________________________________________
v=cv2.VideoCapture('# Name of MP4 file #.mp4')
#_____________________________________________________________________________________________________________________________________________________________________
while v.isOpened():
    r,f=v.read()
    f=main(f)
    cv2.imshow('Road Lane Detection',f)
    if cv2.waitKey(0)&0xFF==ord(' '):
        break
