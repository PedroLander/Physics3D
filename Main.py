# static_plot.py

# import necessary packages
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# create ball object
class Ball():
    def __init__(self):
        self.radius = .2
        self.position = [50,1000]
        self.direction = 270  # Init with direction of gravity
        self.speed = 0
        self.acceleration = -9.8
        print ("New ball at "+str(self.position))

# create the ball object
b0 = Ball()

# create plane ( y = m*x + a )
a = 50 # origin
m = 1.5 # inclination
x = np.linspace(0, 100, 100)# length
y = [(i*m)+a for i in x] # elevation
surf = np.vstack((x, y)) # data points

# create the figure and axes objects
fig, ax = plt.subplots()
hz = ax.scatter(surf[0], surf[1])
sc = ax.scatter(b0.position[0], b0.position[1])
ax.set_xlim([0,100])
ax.set_ylim([-1,1500])

def collide(ball):
    limit = (ball.position[0]*m) + a
    next_pos = ball.position[1] + (ball.speed * -np.sin((2*np.pi)*(ball.direction/360)))
    if next_pos < limit:
        return limit+limit-next_pos
    else:
        return False

def accelerate(ball):
    ball.speed += ball.acceleration

# calculate ball position
def calculate_position(ball):
    accelerate(ball)
    
    collision = collide(ball)
    if collision:
        print ("COLLISION")
        ball.direction += 180
        ball.acceleration *= -1
        ball.speed *= .7
        ball.position[1] = collision
    else:
        ball.position[1] += ball.speed * -np.sin((2*np.pi)*(ball.direction/360))
    return ball

# function that draws each frame of the animation
def animate(i):
    ball = calculate_position(b0)
    
    # (for debugging) print ("t:"+str(i)+"\ty:"+str(ball.position[1])+"\tspeed:"+str(ball.speed))
    #sc = ax.scatter(b0.position[0], b0.position[1])

    sc.set_offsets([b0.position[0], b0.position[1]])
    

# run the animation
ani = FuncAnimation(fig, animate, frames=100, interval=100, repeat=False)
plt.show()
