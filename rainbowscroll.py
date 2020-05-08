from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

sense.clear()

sleep(1)

#sense.set_pixel(0,0,(255,0,0))

r = (255, 0, 0)
o = (255, 128, 0)
y = (255, 255, 0)
g = (0, 255, 0)
c = (0, 255, 128)
b = (0, 0, 255)
p = (255, 0, 255)
n = (255, 128, 255)

colours = [r,o,y,g,c,b,p,n]
copy = [r,o,y,g,c,b,p,n]

index = 0

while True:
    for x in range(8):
        for y in range(8):
            index = (x+y) % len(colours)
            sense.set_pixel(x,y,colours[index])
    
    for i in range(8):
        colours[i] = copy[(i+1)%len(copy)]
        
    for i in range(8):
        copy[i] = colours[i]
    
    sleep(0.1)
        