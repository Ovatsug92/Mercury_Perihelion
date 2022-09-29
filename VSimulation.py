import math

from vpython import *


def sliderprec(sp):
    global prec
    prec_text.text = 'Precesión = {:.3f}'.format(prec) + "\n\n"
    prec = prec_sp.value
    return  # is it necesarry?


def sliderex(ex):
    global E
    E_text.text = 'Excentricidad = {:.3f}'.format(E) + "\n\n"
    E = E_ex.value
    return  # is it necesarry?


Run = True


def run(pp):
    global Run, remember_d, d
    Run = not Run
    if Run:
        pp.text = "Pausar"
        d = remember_d
    else:
        pp.text = "Ejecutar"
        remember_d = d
        d = 0
    return


# scene.caption = """In VPython programs:
# To rotate "camera", drag with right button or Ctrl-drag.
# To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
#   On a two-button mouse, middle is left + right.
# To pan left/right and up/down, Shift-drag.
# Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""
# scene.width = 10
# scene.height = 10
scene.range = 36
scene.autoscale = 0  # Need to turn off autoscaling to prevent insanity.
scene.forward = vector(0, -.3, -1)
scene.title = "Simulación de la Precesión del perihelio de Mercurio\n\n"
button(text="Pausar", pos=scene.title_anchor, bind=run)
wtext(text='Seleccione la precesión, en radianes, de 0 a 0.1\n\n')
# Constansts (is G a natural or physical constant?)
G = 6.67435*(10**(-11))  # (6.674 35 ± 0.000 13)*10**(-11) m**3 kg−1 s**−2 with a relative uncertainty of 19 ppm.
c = 299792458  # m/s
# Data
# Sun
M = 1988500*(10**24)  # 10**24 kg
RvolM = 695700*10**3  # Volumetric mean radius (km)	695,700.    0.006*10**10
# Mercury
m = 0.330*(10**24)  # 10**24 kg
Rvolm = 2439.7*10**3  # Volumetric mean radius (km)	2439.7      0.00024*10**10
rp = 46.000 * (10 ** 9)  # meters (10**6 km) perihelion
# ra = 57.909 * (10 ** 9)  # meters (10**6 km) semi-major axis
# rb = ra * (1 - E ** 2) ** (1 / 2)  # semiminor
# Schwarzschild radius
rs_m = 2*m*G/(c**2)  # Mercury
rs_M = 2*M*G/(c**2)  # Sun
# rp = 46.000 * (10 ** 9)
# E = 0.206
# wp = (6 * math.pi * G * M) / (rp * c ** 2 * (1 - E ** 2))  # 5.018896261130917e-07
# prec = wp / (2 * math.pi)*10**5  # 0.010057470778005635
rvlogM = math.log((RvolM*10**32)/(c**4*rs_M), 10)  # 8.84242200335765       3.46
rvlogm = math.log((Rvolm*10**32)/(c**4*rs_M), 10)  # 6.387336426193336      1.01

E = 0.206
a = 1 / (1 - E ** 2)
c = E * a
b = (a ** 2 - c ** 2) ** (1 / 2)
# ro = 24.6 Should find again!
ro = rp/(2*10**9)
prec = 0
prec_sp = slider(bind=sliderprec, vertical=False, min=0, max=0.101, step=0.001, length=670, width=10)
prec_text = wtext(text='Precesión = {:.3f}'.format(prec) + "\n\n")
E_ex = slider(bind=sliderex, vertical=False, min=0, max=0.9, step=0.001, length=670, width=10)
E_text = wtext(text='Excentricidad= {:.2f}'.format(E) + "\n\n")
e_graph = gcurve(color=color.blue)

# roo = 1 / (1 + E * cos(0))  # If b=1
# print(roo)
# sun = sphere(pos=vector(0, 0, 0), radius=0.2, color=color.orange,
#              make_trail=True)
# mercury = sphere(pos=vector(0, 0, 0), radius=0.05, texture=textures.rock, color=color.gray(0.75),
#                  make_trail=True, trail_type='points', interval=10, retain=500)
sun = sphere(pos=vector(0, 0, 0), radius=rvlogM,
             texture="https://upload.wikimedia.org/wikipedia/commons/b/b4"
                     "/The_Sun_by_the_Atmospheric_Imaging_Assembly_of_NASA%27s_Solar_Dynamics_Observatory_-_20100819"
                     ".jpg")
mercury = sphere(pos=vector(0, 0, 0), radius=rvlogm,
                 texture="https://upload.wikimedia.org/wikipedia/commons/3/30/Mercury_in_color_-_Prockter07_centered"
                         ".jpg",
                 make_trail=True, trail_type='points', interval=10, retain=120)
d = 0.01
o = 0
while True:
    rate(500)
    # Up to now, a complete ellipse, without precession!
    # r = b/((1-(E*cos(o*(1-D)))**2)**(1/2))
    # rpos = vector(r * cos(o), r * sin(o), 0)
    # mercury.pos = r * rpos.hat
    r = ro / (1 + E * cos(o * (1 - prec)))  # Focus in the origin
    rpos = vector(r * cos(o), r * sin(o), 0)
    mercury.pos = r * rpos.hat
    o = o + d
