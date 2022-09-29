import math

from vpython import *

scene.caption = """In VPython programs:
To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""
scene.forward = vector(0, -.3, -1)

e_graph = gcurve(color=color.blue)
D = 0.1
E = 0.5
ro = 1
a = 1 / (1 - E ** 2)
c = E * a
b = (a ** 2 - c ** 2) ** (1 / 2)
roo = 1 / (1 + E * cos(0))
# print(roo)
# sun = sphere(pos=vector(0, 0, 0), radius=0.2, color=color.orange,
#              make_trail=True)
# mercury = sphere(pos=vector(0, 0, 0), radius=0.05, texture=textures.rock, color=color.gray(0.75),
#                  make_trail=True, trail_type='points', interval=10, retain=500)
un = sphere(pos=vector(0, 0, 0), radius=0.2,
            texture="https://upload.wikimedia.org/wikipedia/commons/b/b4"
                    "/The_Sun_by_the_Atmospheric_Imaging_Assembly_of_NASA%27s_Solar_Dynamics_Observatory_-_20100819"
                    ".jpg",
            make_trail=True)
mercury = sphere(pos=vector(0, 0, 0), radius=0.05,
                 texture="https://upload.wikimedia.org/wikipedia/commons/3/30/Mercury_in_color_-_Prockter07_centered"
                         ".jpg",
                 make_trail=True, trail_type='points', interval=10, retain=500)
d = 0.01
o = 0
while True:
    rate(500)
    # Up to now, a complete ellipse, without precession!
    # r = b/((1-(E*cos(o*(1-D)))**2)**(1/2))
    # rpos = vector(r * cos(o), r * sin(o), 0)
    # mercury.pos = r * rpos.hat
    r = ro / (1 + E * cos(o * (1 - D)))  # Focus in the origin
    rpos = vector(r * cos(o), r * sin(o), 0)
    mercury.pos = r * rpos.hat
    o = o + d
