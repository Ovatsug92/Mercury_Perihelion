import math
import os
import sys
import time
import timeit
import tracemalloc

import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.constants as constant
# import matplotlib as mpl
# import imageio.v2 as imageio
ax = fig = rad = rs = None


def plot_info():
    global ax, fig, rad, rs
    # plotting the orbits
    fig, ax = plt.subplots(figsize=(5, 5), subplot_kw={'projection': 'polar'})
    # Sun
    ax.plot(0, 0, '.', markersize=40, color=(1.0, 0.2, 0.1))
    # Changing polar labels
    ax.set_rmax(7.5 * (10 ** 10))
    ax.set_rticks([4 * (10 ** 10), 5 * (10 ** 10), 7 * (10 ** 10)])  # Less radial ticks
    rad = ['0', r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$', r'$\frac{5\pi}{4}$',
           r'$\frac{3\pi}{2}$', r'$\frac{7\pi}{4}$']
    rs = plt.xticks()[0]
    ax.grid(True)


def orbit_apsides(raps):
    # Array or  radian values
    theta = np.arange(0, 2 * np.pi, 0.01)
    # Circles
    r = raps * (theta ** 0)
    # Perihelion Circle
    if raps == rp:
        ax.plot(theta, r, 'r')
    # Aphelion Circle
    elif raps == raph:
        ax.plot(theta, r, 'y')


def forloop():
    plot_info()
    thetan = np.arange(0, 2 * np.pi, 0.01)
    rn = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(thetan)))
    ax.plot(thetan, rn, 'g')
    filenames = []
    p = 0
    orbit_apsides(rp)  # Perihelion circle
    orbit_apsides(raph)  # Aphelion circle
    # Newtonian orbit
    thetan = np.arange(0, 2 * np.pi, 0.01)
    rn = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(thetan)))
    ax.plot(thetan, rn, 'g')
    theta1 = np.arange(3 * thetapi4right + 0.1, 3 * thetapi4right + 2 * math.pi, 0.1)
    # Newtonian perihelion
    ax.plot(0, rp, '*', markersize=8, color=(0.3, 0.3, 0.3))
    # Relativistic perihelion
    ax.plot(3 * thetapi4right, rp, '*', markersize=8, color=(0.6, 0.6, 0.6))
    for theta in theta1:
        # theta = nanim * thetapi4right
        # while theta < nanim * thetapi4right + 2 * math.pi:
        p = p + 1
        rperprec = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(theta * (1 - D))))
        plt.xticks(rs, rad)  # Fewer labels for radius and change degrees to  multiples of pi/4 radians
        ax.set_rlabel_position(0)  # Move radial labels away from plotted line
        ax.plot(theta, rperprec, 'b.', markersize=3)
        # Relativistic perihelion
        # ax.plot(3 * thetapi4right, rp, '*', markersize=8, color=(0.6, 0.6, 0.6))
        filename = f'{p}.png'
        filenames.append(filename)
        plt.savefig(filename, dpi=1200)
    plt.close()


def whileloop():
    plot_info()
    orbit_apsides(rp)  # Perihelion circle
    orbit_apsides(raph)  # Aphelion circle
    # Newtonian orbit
    thetan = np.arange(0, 2 * np.pi, 0.01)
    rn = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(thetan)))
    ax.plot(thetan, rn, 'g')
    # Newtonian perihelion
    ax.plot(0, rp, '*', markersize=8, color=(0.3, 0.3, 0.3))
    # Relativistic perihelion
    ax.plot(3 * thetapi4right, rp, '*', markersize=8, color=(0.6, 0.6, 0.6))
    filenames = []
    p = 0
    theta = 3 * thetapi4right + 0.1
    while theta < 3 * thetapi4right + 2 * math.pi:
        p = p + 1
        rperprec = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(theta * (1 - D))))
        plt.xticks(rs, rad)  # Fewer labels for radius and change degrees to  multiples of pi/4 radians
        ax.set_rlabel_position(0)  # Move radial labels away from plotted line
        ax.plot(theta, rperprec, 'b.', markersize=3)
        # Relativistic perihelion
        # ax.plot(3 * thetapi4right, rp, '*', markersize=8, color=(0.6, 0.6, 0.6))
        filename = f'{p}.png'
        filenames.append(filename)
        plt.savefig(filename, dpi=1200)
        theta += 0.1
    plt.close()


# Constants (is G a natural or physical constant?)
G = scipy.constants.G
c = scipy.constants.c
# Data Sun
M = 1988500 * (10 ** 24)
RvolM = 695700 * 10 ** 3  # Volumetric mean radius (km)	695,700.    0.006*10**10
# Data Mercury
m = 0.330 * (10 ** 24)  # 10**24 kg
Rvolm = 2439.7 * 10 ** 3  # Volumetric mean radius (km)	2439.7      0.00024*10**10
Td = 87.969  # days
T = Td * 24 * 60 * 60  # seconds
rp = 46.000 * (10 ** 9)  # meters (10**6 km) perihelion
ra = 57.909 * (10 ** 9)  # meters (10**6 km) semi-major axis
raph = 69.818 * (10 ** 9)  # meters (10**6 km) aphelion
E = 0.20563069  # Eccentricity
# Array of Mercury data
Data_m = [m, Td, T, rp, raph, ra, E]
Data_list = [r'Masa', r'Periodo Orbital ', r'Periodo Orbital', r'perihelio ',
             r'afelio', r'Eje semi-mayor', r'Excentricidad']
Data_list_dim = ['Kg', 'años', 's', 'm', 'm', 'm', '']
# Computed quantities
rs_M = 2 * M * G / (c ** 2)  # Schwarzschild radius Sun 2953.4060640748576  0.0000002953406*10**10
rb = ra * (1 - E ** 2) ** (1 / 2)  # semiminor
A = math.pi * (ra * rb)  # Area
h = (2 * A) / T  # angular momemtum per unit mass
wp = (6 * math.pi * G * M) / (ra * c ** 2 * (1 - E ** 2))  # 5.018896261130917e-07
# rad/rev this is the precession of 43"/C
D = wp / (2 * math.pi)  # 7.987821488244173e-08 The perturbation in radians
# D = wp/(2*math.pi*0.2408*365*24*3600)  # 1.0518777317095832e-14 This goes to (1-D) in the Eq.
thetapi = 2 * math.pi / (1 - D)  # For new perihelion
wpp = wp ** (-1) * 2 * math.pi
thetapi4 = wpp * thetapi / 8
algo = math.floor(4 * thetapi4 * (1 - D) / math.pi)
thetapi4right = algo * math.pi / 4
# print(algo, thetapi4right, thetapi4)
r0 = (h ** 2 / (G * M))
# Array of computed quantities
Data_calc = [rb, A, h, wp, D, thetapi, algo, 'falta']
Data_calc_list = ['Eje semi-menor', 'Área', 'Momentum angular por unidad de masa', 'Preecesión', 'Precesión',
                  'Ángulo entre perihelios', 'Número de revoluciones', 'Tiempo entre ángulos pi/4']
Data_calc_list_units = ['m', r'$m^2$', r'$m^2/s$', 'rad/rev', 'rad', 'rad', '', 'siglos']
list_tablecalc = [Data_calc_list, Data_calc_list_units, Data_calc]

print('forloop:', timeit.timeit(forloop, number=1))
tracemalloc.start()
forloop()
print(tracemalloc.get_traced_memory())
tracemalloc.stop()
print('whileloop:', timeit.timeit(whileloop, number=1))
tracemalloc.start()
whileloop()
print(tracemalloc.get_traced_memory())
tracemalloc.stop()
