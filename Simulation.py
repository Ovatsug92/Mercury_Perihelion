import math
import os
import sys
import time

import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.constants as constant
import matplotlib as mpl
import imageio.v2 as imageio
# import moviepy.editor as mp  #This was changed to call directly VideoFileClip because of .exe file
# from tabulate import tabulate
import matplotlib.backends.backend_pdf  # This is because of .exe Errors.
from moviepy.video.io.VideoFileClip import VideoFileClip

# For latex text
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
mpl.rcParams['agg.path.chunksize'] = 10000


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


def orbit_classicalstatic(d):
    """
    Plot newtonian Mercury orbit
    :param d:
    :return:
    """
    print('¿Desea guardar la órbita newtoniana?')
    time.sleep(1)
    savenewtst = input('De ser así escriba "s" y presione enter, caso contrario escriba cualquier otra tecla'
                       ' y/o presione enter:\n')
    # Newtonian orbit
    theta = np.arange(0, 2 * np.pi, 0.01)
    r = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(theta * (1 - d))))
    ax.plot(theta, r, 'g')
    # Newtonian perihelion
    ax.plot(0, rp, '*', markersize=8, color=(0.3, 0.3, 0.3))
    # Changing polar labels
    ax.set_rmax(7.5 * (10 ** 10))
    ax.set_rticks([4 * (10 ** 10), 5 * (10 ** 10), 7 * (10 ** 10)])  # Less radial ticks
    rad = ['0', r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$', r'$\frac{5\pi}{4}$',
           r'$\frac{3\pi}{2}$', r'$\frac{7\pi}{4}$']
    rs = plt.xticks()[0]
    plt.xticks(rs, rad)  # less labels for radius and change degrees to  multipli of pi/4 radians
    ax.set_rlabel_position(0)  # Move radial labels away from plotted line
    ax.grid(True)
    # Saving
    if savenewtst == 's':
        print('1. Pdf: Para guardar en formato ".pdf" escriba 1 y presione enter.')
        print('2. Png: Para guardar en formato ".png" escriba 2 y presione enter.')
        time.sleep(1)
        saveall = input('Escriba su opción, por favor:\n')
        while int(saveall) not in range(1, 3):
            print(f'El número correspondiente a la opción debe ser natural y debe estar entre 0 y 3 \n')
            time.sleep(1)
            saveall = input('Escriba su opción, por favor:\n')
        fig.tight_layout()
        if int(saveall) == 1:
            filename = 'Orbit_newtonian.pdf'
            plt.savefig(filename, dpi=1200)

        elif int(saveall) == 2:
            filename = 'Orbit_newtonian.png'
            plt.savefig(filename, dpi=1200)
    print('Luego de obervar la gráfica, por favor cerrar la ventana.')
    time.sleep(1)
    plt.show()


def orbit_classicaldynamic(d):
    """
    This is a simulation of the newtonian Mercury orbit
    :param d:
    :return:
    """
    # apsides
    orbit_apsides(rp)  # Perihelion circle
    orbit_apsides(raph)  # Aphelion circle
    # Newtonian perihelion
    ax.plot(0, rp, '*', markersize=8, color=(0.3, 0.3, 0.3))
    # Changing polar labels
    ax.set_rmax(7.5 * (10 ** 10))
    ax.set_rticks([4 * (10 ** 10), 5 * (10 ** 10), 7 * (10 ** 10)])  # Less radial ticks
    rad = ['0', r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$', r'$\frac{5\pi}{4}$',
           r'$\frac{3\pi}{2}$', r'$\frac{7\pi}{4}$']
    rs = plt.xticks()[0]
    ax.grid(True)
    # Newtonian orbit simulation
    theta = np.arange(0, 2 * np.pi, 0.1)
    for thetac in theta:
        r = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(thetac * (1 - d))))
        plt.xticks(rs, rad)  # less labels for radius and change degrees to  multipli of pi/4 radians
        ax.set_rlabel_position(0)  # Move radial labels away from plotted line
        ax.plot(thetac, r, 'g.', markersize=2)
        plt.pause(0.1)
    plt.show()


def orbit(norb):
    """
    This function plots the orbit from a start angle to that angle + 2*math.pi
    In this case, multiples of thetapi4
    :param norb:
    :return:
    """
    print('¿Desea guardar la órbita precesada?')
    time.sleep(1)
    saverelstn = input('De ser así escriba "s" y presione enter, caso contrario escriba cualquier otra tecla'
                       ' y/o presione enter:\n')
    # apsides
    orbit_apsides(rp)  # Perihelion circle
    orbit_apsides(raph)  # Aphelion circle
    # Newtonian orbit
    thetan = np.arange(0, 2 * np.pi, 0.01)
    rn = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(thetan)))
    ax.plot(thetan, rn, 'g')
    # Newtonian perihelion
    ax.plot(0, rp, '*', markersize=8, color=(0.3, 0.3, 0.3))
    # Precessed orbit
    theta = np.arange(norb * thetapi4right, norb * thetapi4right + 2 * math.pi, 0.1)
    rperprec = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(theta * (1 - D))))
    ax.plot(theta, rperprec, 'b.', markersize=3)
    # Relativistic perihelion
    ax.plot(norb * thetapi4right, rp, '*', markersize=8, color=(0.6, 0.6, 0.6))
    # Newtonian perihelion
    ax.plot(0, rp, '*', markersize=8, color=(0.3, 0.3, 0.3))
    # Changing polar labels
    ax.set_rmax(7.5 * (10 ** 10))
    ax.set_rticks([4 * (10 ** 10), 5 * (10 ** 10), 7 * (10 ** 10)])  # Less radial ticks
    rad = ['0', r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$', r'$\frac{5\pi}{4}$',
           r'$\frac{3\pi}{2}$', r'$\frac{7\pi}{4}$']
    rs = plt.xticks()[0]
    plt.xticks(rs, rad)  # less labels for radius and change degrees to  multipli of pi/4 radians
    ax.set_rlabel_position(0)  # Move radial labels away from plotted line
    ax.grid(True)
    # Saving
    if saverelstn == 's':
        print('1. Pdf: Para guardar en formato ".pdf" escriba 1 y presione enter.')
        print('2. Png: Para guardar en formato ".png" escriba 2 y presione enter.')
        time.sleep(1)
        saveall = input('Escriba su opción, por favor:\n')
        while int(saveall) not in range(1, 3):
            print(f'El número correspondiente a la opción debe ser natural y debe estar entre 0 y 3 \n')
            time.sleep(1)
            saveall = input('Escriba su opción, por favor:\n')
        fig.tight_layout()
        if int(saveall) == 1:
            filename = 'Orbit_newtonian.pdf'
            plt.savefig(filename, dpi=1200)

        elif int(saveall) == 2:
            filename = 'Orbit_newtonian.png'
            plt.savefig(filename, dpi=1200)
    print('Luego de obervar la gráfica, por favor cerrar la ventana.')
    time.sleep(1)
    plt.show()


def orbit_sim(nsim):
    """
    This function plots the orbit from a start angle to that angle + 2*math.pi
    In this case, multiples of thetapi4
    :param nsim:
    :return:
    """
    # apsides
    orbit_apsides(rp)  # Perihelion circle
    orbit_apsides(raph)  # Aphelion circle
    # Newtonian orbit
    thetan = np.arange(0, 2 * np.pi, 0.01)
    rn = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(thetan)))
    ax.plot(thetan, rn, 'g')
    # Newtonian perihelion
    ax.plot(0, rp, '*', markersize=8, color=(0.3, 0.3, 0.3))
    # Relativistic perihelion
    ax.plot(nsim * thetapi4right, rp, '*', markersize=8, color=(0.6, 0.6, 0.6))
    # Changing polar labels
    ax.set_rmax(7.5 * (10 ** 10))
    ax.set_rticks([4 * (10 ** 10), 5 * (10 ** 10), 7 * (10 ** 10)])  # Less radial ticks
    rad = ['0', r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$', r'$\frac{5\pi}{4}$',
           r'$\frac{3\pi}{2}$', r'$\frac{7\pi}{4}$']
    rs = plt.xticks()[0]
    ax.grid(True)
    # Precessed orbit simulation
    theta1 = np.arange(nsim * thetapi4right, nsim * thetapi4right + 2 * math.pi, 0.1)
    for theta in theta1:
        rperprec = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(theta * (1 - D))))
        plt.xticks(rs, rad)  # less labels for radius and change degrees to  multipli of pi/4 radians
        ax.set_rlabel_position(0)  # Move radial labels away from plotted line
        # rpappa = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(n * thetapi4right * (1 - D))))
        ax.plot(theta, rperprec, 'b.', markersize=3)
        # Relativistic perihelion
        ax.plot(nsim * thetapi4right, rp, '*', markersize=8, color=(0.6, 0.6, 0.6))
        plt.pause(0.1)
    plt.show()


def orbit_anim(nanim):
    qlty = input('Escriba por favor la calidad de imágenes que desea en una escala del 1 al 10:\n')
    while int(qlty) not in range(1, 11):
        print(f'El número correspondiente a la opción debe ser natural y debe estar entre 0 y 11 \n')
        time.sleep(1)
        qlty = input('Escriba por favor la calidad de imágenes que desea en una escala del 1 al 10:\n')
    qqlty = int(qlty) * 120
    print('1. Gif: Para obtener una animación en formato ".gif" escriba 1 y presione enter.')
    print('2. Mp4: Para obtener una animación en video ".mp4" escriba 2 y presione enter.')
    time.sleep(1)
    anim = input('Escriba su opción, por favor:\n')
    while int(anim) not in range(1, 3):
        print(f'El número correspondiente a la opción debe ser natural y debe estar entre 0 y 3 \n')
        time.sleep(1)
        anim = input('Escriba su opción, por favor:\n')
    filenames = []
    if int(anim) == 1:
        print('Por favor, espere unos segundos.')
        # apsides
        orbit_apsides(rp)  # Perihelion circle
        orbit_apsides(raph)  # Aphelion circle
        # Newtonian orbit
        thetan = np.arange(0, 2 * np.pi, 0.01)
        rn = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(thetan)))
        ax.plot(thetan, rn, 'g')
        # Newtonian perihelion
        ax.plot(0, rp, '*', markersize=8, color=(0.3, 0.3, 0.3))
        # Relativistic perihelion
        ax.plot(nanim * thetapi4right, rp, '*', markersize=8, color=(0.6, 0.6, 0.6))
        # Changing polar labels
        ax.set_rmax(7.5 * (10 ** 10))
        ax.set_rticks([4 * (10 ** 10), 5 * (10 ** 10), 7 * (10 ** 10)])  # Less radial ticks
        rad = ['0', r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$', r'$\frac{5\pi}{4}$',
               r'$\frac{3\pi}{2}$', r'$\frac{7\pi}{4}$']
        rs = plt.xticks()[0]
        ax.grid(True)
        # Creating files
        print('Las imágenes procesadas son de muy buena calidad.')
        theta1 = np.arange(nanim * thetapi4right, nanim * thetapi4right + 2 * math.pi, 0.1)
        p = 0
        for theta in theta1:
            p = p + 1
            rperprec = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(theta * (1 - D))))
            plt.xticks(rs, rad)  # Fewer labels for radius and change degrees to  multiples of pi/4 radians
            ax.set_rlabel_position(0)  # Move radial labels away from plotted line
            ax.plot(theta, rperprec, 'b.', markersize=3)
            # Relativistic perihelion
            ax.plot(nanim * thetapi4right, rp, '*', markersize=8, color=(0.6, 0.6, 0.6))
            filename = f'{p}.png'
            filenames.append(filename)
            plt.savefig(filename, dpi=qqlty)
        # build gif
        with imageio.get_writer(f'prec{nanim}pi4.gif', mode='I') as writer:
            for filename in filenames:
                image = imageio.imread(filename)
                writer.append_data(image)
    elif int(anim) == 2:
        print('Por favor, espere unos segundos.')
        # apsides
        orbit_apsides(rp)  # Perihelion circle
        orbit_apsides(raph)  # Aphelion circle
        # Newtonian orbit
        thetan = np.arange(0, 2 * np.pi, 0.01)
        rn = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(thetan)))
        ax.plot(thetan, rn, 'g')
        # Newtonian perihelion
        ax.plot(0, rp, '*', markersize=8, color=(0.3, 0.3, 0.3))
        # Relativistic perihelion
        ax.plot(nanim * thetapi4right, rp, '*', markersize=8, color=(0.6, 0.6, 0.6))
        # Changing polar labels
        ax.set_rmax(7.5 * (10 ** 10))
        ax.set_rticks([4 * (10 ** 10), 5 * (10 ** 10), 7 * (10 ** 10)])  # Less radial ticks
        rad = ['0', r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$', r'$\frac{5\pi}{4}$',
               r'$\frac{3\pi}{2}$', r'$\frac{7\pi}{4}$']
        rs = plt.xticks()[0]
        ax.grid(True)
        # Creating files
        print('Las imágenes procesadas son de muy buena calidad.')
        filenames = []
        theta1 = np.arange(nanim * thetapi4right, nanim * thetapi4right + 2 * math.pi, 0.1)
        p = 0
        for theta in theta1:
            p = p + 1
            rperprec = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(theta * (1 - D))))
            plt.xticks(rs, rad)  # Fewer labels for radius and change degrees to  multiples of pi/4 radians
            ax.set_rlabel_position(0)  # Move radial labels away from plotted line
            ax.plot(theta, rperprec, 'b.', markersize=3)
            # Relativistic perihelion
            ax.plot(nanim * thetapi4right, rp, '*', markersize=8, color=(0.6, 0.6, 0.6))
            filename = f'{p}.png'
            filenames.append(filename)
            plt.savefig(filename, dpi=qqlty)
        # build gif
        with imageio.get_writer(f'prec{nanim}pi4.gif', mode='I') as writer:
            for filename in filenames:
                # Starting with ImageIO v3 the behavior of this function will switch to that of iio.v3.imread.
                # To keep the current behavior (and make this warning disappear) use `import imageio.v2 as imageio`
                # or call `imageio.v2.imread` directly.
                image = imageio.imread(filename)
                writer.append_data(image)
        # Coverting gif to mp4
        clip = VideoFileClip(f'prec{nanim}pi4.gif')  # commented init and importing different worked, but won't do it
        clip.write_videofile(f'prec{nanim}pi4.mp4')
        clip.close()
        # Remove files
    for filename in set(filenames):
        os.remove(filename)
    gh = math.floor(algo / (2 * math.pi))
    print(f'Luego de {nanim * gh} revoluciones')
    print(f'Luego de {nanim * gh * 0.2408 / 100} siglos')
    print(f'Luego de {nanim * thetapi4 * (1 - D) / (math.pi / 4)} revoluciones en tehetapi4')
    print(f'Luego de {(nanim * thetapi4 * (1 - D) / (math.pi / 4)) * 0.2408 / 100} siglos en tehetapi4')


def orbits(norbs):
    """
    This function plots the orbit from a start angle to that angle + 2*math.pi
    In this case, multiples of thetapi4
    :param norbs:
    :return:
    """
    print('¿Desea guardar las órbitas indivudales?')
    time.sleep(1)
    saveorbs = input('De ser así escriba "s" y presione enter, caso contrario escriba cualquier otra tecla'
                     ' y/o presione enter:\n')
    time.sleep(1)
    if saveorbs == 's':
        for i in range(norbs):
            # apsides
            orbit_apsides(rp)  # Perihelion circle
            orbit_apsides(raph)  # Aphelion circle
            # Newtonian orbit
            thetan = np.arange(0, 2 * np.pi, 0.01)
            rn = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(thetan)))
            ax.plot(thetan, rn, 'g')
            # Newtonian perihelion
            ax.plot(0, rp, '*', markersize=8, color=(0.3, 0.3, 0.3))
            # Precessed orbit
            theta = np.arange(i * thetapi4right, i * thetapi4right + 2 * math.pi, 0.1)
            rperprec = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(theta * (1 - D))))
            ax.plot(theta, rperprec, 'b.', markersize=3)
            # Relativistic perihelion
            ax.plot(i * thetapi4right, rp, '*', markersize=8, color=(0.6, 0.6, 0.6))
            # Newtonian perihelion
            ax.plot(0, rp, '*', markersize=8, color=(0.3, 0.3, 0.3))
            # Changing polar labels
            ax.set_rmax(7.5 * (10 ** 10))
            ax.set_rticks([4 * (10 ** 10), 5 * (10 ** 10), 7 * (10 ** 10)])  # Less radial ticks
            rad = ['0', r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$', r'$\frac{5\pi}{4}$',
                   r'$\frac{3\pi}{2}$', r'$\frac{7\pi}{4}$']
            rs = plt.xticks()[0]
            plt.xticks(rs, rad)  # less labels for radius and change degrees to  multipli of pi/4 radians
            ax.set_rlabel_position(0)  # Move radial labels away from plotted line
            ax.grid(True)
            # Saving
            filename = f'Orbit_precessed_{i}pi4.pdf'
            plt.savefig(filename, dpi=1200)
        # plotting the graphs
        plt.close()
    plt.close()
    print('¿Desea guardar las órbitas juntas?')
    time.sleep(1)
    saveorbsall = input('De ser así escriba "s" y presione enter, caso contrario escriba cualquier otra tecla'
                        ' y/o presione enter:\n')
    time.sleep(1)
    figs, axxs = plt.subplots(3, 3, figsize=(8, 8), subplot_kw={'projection': 'polar'})
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.8)
    # Saving
    rs = plt.xticks()[0]
    for it in range(3):
        for j in range(3):
            # Array or  radian values
            theta = np.arange(0, 2 * np.pi, 0.01)
            # Circles
            rpp = rp * (theta ** 0)  # Perihelion Circle
            raphp = raph * (theta ** 0)  # Aphelion Circle
            axxs[it, j].plot(theta, rpp, 'r', linewidth=1.5)  # Perihelion Circle
            axxs[it, j].plot(theta, raphp, 'y', linewidth=1.5)  # Aphelion Circle
            # Changing polar labels
            axxs[it, j].set_rmax(7.5 * (10 ** 10))
            axxs[it, j].set_rticks([])  # Because the full labels were unnecessary and cumbersome to read!
            rad = ['0', r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$', r'$\frac{5\pi}{4}$',
                   r'$\frac{3\pi}{2}$', r'$\frac{7\pi}{4}$']
            axxs[it, j].set_rlabel_position(0)  # Move radial labels away from plotted line
            axxs[it, j].grid(True)
            plt.sca(axxs[it, j])
            plt.xticks(rs, rad)
            # Sun
            axxs[it, j].plot(0, 0, '.', markersize=20, color=[1.0, 0.2, 0.1])
            # Newtonian orbit
            thetan = np.arange(0, 2 * np.pi, 0.01)
            rn = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(thetan)))
            axxs[it, j].plot(thetan, rn, 'g', linewidth=1.5)
            if it == 0:
                # Title
                axxs[it, j].set_title(f'Precesión {it + j} veces ' r'$\frac{\pi}{4}$')
                axxs[it, j].title.set_size(8)
                # Precessed orbit
                theta = np.arange((it + j) * thetapi4right, (it + j) * thetapi4right + 2 * math.pi, 0.1)
                rperprec = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(theta * (1 - D))))
                axxs[it, j].plot(theta, rperprec, 'b.', markersize=1.5)
                # Relativistic perihelion
                axxs[it, j].plot((it + j) * thetapi4right, rp, '*', markersize=8, color=(0.6, 0.6, 0.6))
            elif it == 1:
                # Title
                axxs[it, j].set_title(f'Precesión {it + 2 + j} veces ' r'$\frac{\pi}{4}$')
                axxs[it, j].title.set_size(8)
                # Precessed orbit
                theta = np.arange((it + 2 + j) * thetapi4right, (it + 2 + j) * thetapi4right + 2 * math.pi, 0.1)
                rperprec = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(theta * (1 - D))))
                axxs[it, j].plot(theta, rperprec, 'b.', markersize=1.5)
                # Relativistic perihelion
                axxs[it, j].plot((it + 2 + j) * thetapi4right, rp, '*', markersize=8, color=(0.6, 0.6, 0.6))
            elif it == 2:
                # Title
                axxs[it, j].set_title(f'Precesión {it + 4 + j} veces ' r'$\frac{\pi}{4}$')
                axxs[it, j].title.set_size(8)
                # Precessed orbit
                theta = np.arange((it + 4 + j) * thetapi4right, (it + 4 + j) * thetapi4right + 2 * math.pi, 0.1)
                rperprec = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(theta * (1 - D))))
                axxs[it, j].plot(theta, rperprec, 'b.', markersize=1.5)
                # Relativistic perihelion
                axxs[it, j].plot((it + 4 + j) * thetapi4right, rp, '*', markersize=8, color=(0.6, 0.6, 0.6))
            # Newtonian perihelion
            axxs[it, j].plot(0, rp, '*', markersize=8, color=(0.3, 0.3, 0.3))
    if saveorbsall == 's':
        print('1. Pdf: Para guardar en formato ".pdf" escriba 1 y presione enter.')
        print('2. Png: Para guardar en formato ".png" escriba 2 y presione enter.')
        time.sleep(1)
        saveall = input('Escriba su opción, por favor:\n')
        while int(saveall) not in range(1, 3):
            print(f'El número correspondiente a la opción debe ser natural y debe estar entre 0 y 3 \n')
            time.sleep(1)
            saveall = input('Escriba su opción, por favor:\n')
        fig.tight_layout()
        if int(saveall) == 1:
            filenames = f'Orbits_precessed_npi4.pdf'
            plt.savefig(filenames, dpi=1200)
        elif int(saveall) == 2:
            filenames = f'Orbits_precessed_npi4.png'
            plt.savefig(filenames, dpi=1200)
    plt.show()


# Constants (is G a natural or physical constant?)
G = scipy.constants.G
c = scipy.constants.c
# Data Sun
M = 1988500 * (10 ** 24)
RvolM = 695700*10**3  # Volumetric mean radius (km)	695,700.    0.006*10**10
# Data Mercury
m = 0.330 * (10 ** 24)  # 10**24 kg
Rvolm = 2439.7*10**3  # Volumetric mean radius (km)	2439.7      0.00024*10**10
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
rs_M = 2*M*G/(c**2)  # Schwarzschild radius Sun 2953.4060640748576  0.0000002953406*10**10
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
# Print
print('Este es un programa sobre la precesión de Mercurio')
time.sleep(1.5)
print('Se trabaja con la gravitación Newtoniana y la teoría general de la relatividad\n')
run_program = True
while run_program:
    # Principal list
    print('Escoger una opción que le gustaría realizar de la siguiente lista:\n')
    time.sleep(1.5)
    print('1. Mostrar la gráfica de la órbita Newtoniana.')
    print('2. Mostrar la simulación de la órbita Newtoniana. ')
    print('3. Mostrar la gráfica de la órbita precesada en un múltiplo de pi/4 radianes.')
    print('4. Mostrar la simulación de la órbita precesada en un múltiplo de pi/4 radianes.')
    print('5. Guardar las simulaciones en video o gif animado.')
    print('6. Mostrar las gráficas de las órbitas precesadas en múltiplos de pi/4 radianes.')
    print('7. Mostrar la tabla de datos usados en este programa.')
    print('8. Salir del programa.\n')
    time.sleep(3)
    c0 = input('Escribir el número de la opción elegida y presionar enter, por favor:\n')
    while int(c0) not in range(1, 9):
        print(f'El número correspondiente a la opción debe ser entero y debe estrar entre  entre 0 y 9\n')
        time.sleep(1)
        c0 = input('Escribir el número de la opción elegida y presionar enter, por favor:\n')
    # plotting the orbits
    fig, ax = plt.subplots(figsize=(5, 5), subplot_kw={'projection': 'polar'})
    # Sun
    ax.plot(0, 0, '.', markersize=40, color=(1.0, 0.2, 0.1))
    if int(c0) == 1:
        orbit_classicalstatic(0)
        print('\n¿Desea realizar otra acción en el programa?')
        time.sleep(1)
        o1 = input('De ser así escriba "s" y presione enter, caso contrario escriba cualquier otra tecla'
                   ' y/o presione enter:\n')
        if o1 == 's':
            run_program = True
        else:
            run_program = False
            print('¡Hasta luego!')
            time.sleep(4)
            sys.exit()
    elif int(c0) == 2:
        print('Luego de obervar la gráfica, por favor cerrar la ventana')
        orbit_classicaldynamic(0)
        print('\n¿Desea realizar otra acción en el programa?')
        time.sleep(1)
        o1 = input('De ser así escriba "s" y presione enter, caso contrario escriba cualquier otra tecla'
                   ' y/o presione enter:\n')
        if o1 == 's':
            run_program = True
        else:
            run_program = False
            print('¡Hasta luego!')
            time.sleep(4)
            sys.exit()
    elif int(c0) == 3:
        n3 = input('Ingrese por favor el múltiplo de pi/4 de precesión de la órbita, por favor:\n')
        while int(n3) not in range(0, 9):
            print(f'El número correspondiente a la opción debe ser entero y debe estrar entre  entre 0 y 8\n')
            time.sleep(1)
            n3 = input('Ingrese por favor el múltiplo de pi/4 de precesión de la órbita, por favor:\n')
        orbit(int(n3))
        print('\n¿Desea realizar otra acción en el programa?')
        time.sleep(1)
        o1 = input('De ser así escriba "s" y presione enter, caso contrario escriba cualquier otra tecla'
                   ' y/o presione enter:\n')
        if o1 == 's':
            run_program = True
        else:
            run_program = False
            print('¡Hasta luego!')
            time.sleep(4)
            sys.exit()
    elif int(c0) == 4:
        n4 = input('Ingrese por favor el múltiplo de pi/4 de precesión de la órbita, por favor:\n')
        while int(n4) not in range(0, 9):
            print(f'El número correspondiente a la opción debe ser entero y debe estrar entre  entre 0 y 8\n')
            time.sleep(1)
            n4 = input('Ingrese por favor el múltiplo de pi/4 de precesión de la órbita, por favor:\n')
        print('Luego de obervar la gráfica, por favor cerrar la ventana.')
        orbit_sim(int(n4))
        print('\n¿Desea realizar otra acción en el programa?')
        time.sleep(1)
        o1 = input('De ser así escriba "s" y presione enter, caso contrario escriba cualquier otra tecla'
                   ' y/o presione enter:\n')
        if o1 == 's':
            run_program = True
        else:
            run_program = False
            print('¡Hasta luego!')
            time.sleep(4)
            sys.exit()
    elif int(c0) == 5:
        n5 = input('Ingrese por favor el múltiplo de pi/4 de precesión de la órbita, por favor:\n')
        while int(n5) not in range(0, 9):
            print(f'El número correspondiente a la opción debe ser entero y debe estrar entre  entre 0 y 8\n')
            time.sleep(1)
            n5 = input('Ingrese por favor el múltiplo de pi/4 de precesión de la órbita, por favor:\n')
        orbit_anim(int(n5))
        print('\n¿Desea realizar otra acción en el programa?')
        time.sleep(1)
        o1 = input('De ser así escriba "s" y presione enter, caso contrario escriba cualquier otra tecla'
                   ' y/o presione enter:\n')
        if o1 == 's':
            run_program = True
        else:
            run_program = False
            print('¡Hasta luego!')
            time.sleep(4)
            sys.exit()
    elif int(c0) == 6:
        orbits(8)
        print('\n¿Desea realizar otra acción en el programa?')
        time.sleep(1)
        o1 = input('De ser así escriba "s" y presione enter, caso contrario escriba cualquier otra tecla'
                   ' y/o presione enter:\n')
        if o1 == 's':
            run_program = True
        else:
            run_program = False
            print('¡Hasta luego!')
            time.sleep(4)
            sys.exit()
    elif int(c0) == 7:
        print('CONSTANTES:\n')
        # Array of constants
        constants_list = ['Constante Gravitacional', 'Velocidad de la luz']
        constants_u = [r'm³kg⁻¹s⁻²', r'ms⁻¹']
        Constants = [G, c]
        Dct = len(Constants)
        for i in range(Dct):
            print(f'{constants_list[i]}:' '  {:.3e}' f' {constants_u[i]}'.format(Constants[i]))
        time.sleep(2)
        # List_constants = [constants_list, constants_list_units, Constants]
        # tableConstants = tabulate(List_constants, headers='firstrow', tablefmt='fancy_grid')
        # print(tableConstants)
        time.sleep(2)
        print('\nLa masa del sol es {:.4e} kg.\n'.format(M))
        print('DATOS DE MERCURIO:\n')
        # Array of Mercury data
        Data_m = [m, Td, T, rp, raph, ra, E]
        Data_list_m = ['Masa', 'Periodo Orbital ', 'Periodo Orbital', 'Perihelio ',
                       'Afelio', 'Eje semi-mayor', 'Excentricidad']
        Data_list_u_m = ['Kg', 'días', 's', 'm', 'm', 'm', '']
        # list_tablem = [Data_list, Data_list_dim, Data_m]
        # tableMercury = tabulate(list_tablem, headers='firstrow', tablefmt='fancy_grid')
        # print(tableMercury)
        Dm = len(Data_m)
        for i in range(Dm):
            print(f'{Data_list_m[i]}:' '  {:.3e}' f' {Data_list_u_m[i]}'.format(Data_m[i]))
        time.sleep(2)
        print('\nCANTIDADES CALCULADAS:\n')
        # Array of computed quantities
        Data_c = [rb, A, h, wp, D, thetapi, algo, 0.21654]
        Data_list_c = ['Eje semi-menor', 'Área', 'Momentum angular por unidad de masa', 'Preecesión', 'Precesión',
                       'Ángulo entre perihelios', 'Número de revoluciones', 'Tiempo entre ángulos pi/4']
        Data_list_u_c = ['m', r'm²', r'm²/s', 'rad/rev', 'rad', 'rad', '', 'siglos']
        # list_tablecalc = [Data_calc_list, Data_calc_list_units, Data_calc]
        # Table_calc= tabulate(list_tablecalc, headers='firstrow', tablefmt='fancy_grid')
        # print(Table_calc)
        Dc = len(Data_c)
        for i in range(Dc):
            print(f'{Data_list_c[i]}:' '  {:.3e}' f' {Data_list_u_c[i]}'.format(Data_c[i]))
        time.sleep(2)
        time.sleep(2)
        print('\n¿Desea realizar otra acción en el programa?')
        time.sleep(1)
        o1 = input('De ser así escriba "s" y presione enter, caso contrario escriba cualquier otra tecla'
                   ' y/o presione enter:\n')
        if o1 == 's':
            run_program = True
        else:
            run_program = False
            print('¡Hasta luego!')
            time.sleep(4)
            sys.exit()
    elif int(c0) == 8:
        print('Hasta luego.')
        sys.exit()
# Add Vpyhton?