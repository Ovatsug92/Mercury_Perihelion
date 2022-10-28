import math
import os
import sys
import time
import timeit

import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.constants as constant
import matplotlib as mpl
import imageio.v2 as imageio
# import moviepy.editor as mp  #This was changed to call directly VideoFileClip because of .exe file
# from tabulate import tabulate
from moviepy.video.io.VideoFileClip import VideoFileClip

# For latex text
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
mpl.rcParams['agg.path.chunksize'] = 10000

c0 = csub = csubsub = qqlty = 0
savename: str


def orbit_apsides(raps, th_i, th_f):
    # Array or  radian values
    theta = np.arange(th_i, th_f, 0.01)
    # Circles
    r = raps * (theta ** 0)
    # Perihelion Circle
    if raps == rp:
        ax.plot(theta, r, 'r')
    # Aphelion Circle
    elif raps == raph:
        ax.plot(theta, r, 'y')


def quality():
    global qqlty
    qlty = input('Escriba por favor la calidad de imágenes que desea en una escala del 1 al 10:\n')
    while int(qlty) not in range(1, 11):
        print(f'El número correspondiente a la opción debe ser natural y debe estar entre 0 y 11 \n')
        time.sleep(1)
        qlty = input('Escriba por favor la calidad de imágenes que desea en una escala del 1 al 10:\n')
    qqlty = int(qlty) * 120


#    gh = math.floor(algo / (2 * math.pi))
#    print(f'Luego de {nanim * gh} revoluciones')
#    print(f'Luego de {nanim * gh * 0.2408 / 100} siglos')
#    print(f'Luego de {nanim * thetapi4 * (1 - D) / (math.pi / 4)} revoluciones en tehetapi4')
#    print(f'Luego de {(nanim * thetapi4 * (1 - D) / (math.pi / 4)) * 0.2408 / 100} siglos en tehetapi4')


def orbits(norbs):
    """
    This function plots the orbit from a start angle to that angle + 2*math.pi
    In this case, multiples of thetapi4
    :param norbs:
    :return:
    """
    quality()
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
            plt.savefig(filename, dpi=qqlty)
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


def main_menu():
    """Main menu: Choose only one option between 0-4"""
    global c0
    # Main menu
    print('Escoger una opción que le gustaría realizar de la siguiente lista:')
    time.sleep(1.5)
    print('1. Realizar la simulación newtoniana de la órbita de Mercurio.')
    print('2. Realizar la simulación de la órbita de Mercurio precesada comprendida entre dos ángulos \u03C6')
    print('3. Realizar la simulación de la órbita de Mercurio precesada en un múltiplo de \u03C0/4 radianes.')
    print('4. Mostrar las gráficas de las órbitas precesadas en múltiplos de \u03C0/4 radianes.')
    print('5. Mostrar los datos usados en este programa.')
    print('6. Salir del programa.\n')
    time.sleep(3)
    c0 = int(input('Escribir el número de la opción elegida y presionar enter, por favor:\n'))
    while (c0 < 1) or (c0 > 6):
        print(f'El número correspondiente a la opción debe ser entero y debe estrar entre  entre 0 y 9\n')
        time.sleep(1)
        c0 = int(input('Escribir el número de la opción elegida y presionar enter, por favor:\n'))


def sub_menu():
    """Main menu: Choose only one option between 0-4"""
    global csub
    # Sub menu
    print('Escoger una opción que le gustaría realizar de la siguiente lista:')
    time.sleep(1.5)
    print("1. Mostrar la gráfica cartesiana 'r vs \u03C6' de la simulación .")
    print("2. Mostrar la gráfica polar 'r vs \u03C6' de la simulación .")
    print('3. Mostar la simulación.')
    print('4. Guardar la simulación.')
    time.sleep(3)
    csub = int(input('Escribir el número de la opción elegida y presionar enter, por favor:\n'))
    while (csub < 1) or (csub > 4):
        print(f'El número correspondiente a la opción debe ser entero y debe estrar entre  entre 0 y 4\n')
        time.sleep(1)
        csub = int(input('Escribir el número de la opción elegida y presionar enter, por favor:\n'))


def sub_sub_menu():
    """Main menu: Choose only one option between 0-4"""
    global csubsub
    # Menu for saving
    print('Escoger una opción que le gustaría realizar de la siguiente lista:')
    time.sleep(1.5)
    print('1. Gif: Para guardar la simulación en animación ".gif" escriba 1 y presione enter.')
    print('2. Mp4: Para guardar la simulación en video ".mp4" escriba 2 y presione enter.')
    time.sleep(1)
    csubsub = int(input('Escriba su opción, por favor:\n'))
    while (csubsub < 1) or (csubsub > 3):
        print(f'El número correspondiente a la opción debe ser entero y debe estrar entre  entre 0 y 3')
        time.sleep(1)
        csubsub = int(input('Escribir el número de la opción elegida y presionar enter, por favor:\n'))


def save_simulation(dd, th_i, th_f, savecsubsub):
    quality()
    polar_background(rp, th_i, th_f)
    filenames = []
    p = 0
    print('Por favor, espere unos segundos.')
    # Creating files
    print('Las imágenes procesadas son de muy buena calidad.')
    if dd == 0:
        plt.title(r"Simulación polar $r$ vs $\varphi$", va='bottom', fontsize=16)
        theta = th_i + 0.1
        while theta < th_f:
            p += 1
            rn = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(theta)))
            ax.plot(theta, rn, 'g.', markersize=3)
            filename = f'{p}.png'
            filenames.append(filename)
            plt.savefig(filename, dpi=qqlty)
            theta += 0.1
        if savecsubsub == 1:
            build_gif(filenames)
        if savecsubsub == 2:
            build_gif(filenames)
            # Coverting gif to mp4
            clip = VideoFileClip(
                f'Newtonian.gif')  # commented init and importing different worked, but won't do it
            clip.write_videofile(f'Newtonian.mp4')
            clip.close()
        for filename in set(filenames):
            os.remove(filename)
    else:
        plt.title(r"Simulación polar $r$ vs $\varphi$", va='bottom', fontsize=16)
        # Newtonian orbit
        thetan = np.arange(th_i + 0.01, th_f, 0.01)
        rn = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(thetan)))
        ax.plot(thetan, rn, 'g')
        # Relativistic perihelion
        ax.plot(th_i, rp, '*', markersize=8, color=(0.6, 0.6, 0.6))
        # Relativistic orbit
        theta = th_i + 0.1
        while theta < th_f:
            p += 1
            rprec = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(theta * (1 - D))))
            ax.plot(theta, rprec, 'b.', markersize=3)
            filename = f'{p}.png'
            filenames.append(filename)
            plt.savefig(filename, dpi=qqlty)
            theta += 0.1
        if savecsubsub == 1:
            build_gif(filenames)
        if savecsubsub == 2:
            build_gif(filenames)
            # Coverting gif to mp4
            clip = VideoFileClip(
                f'{savename}.gif')  # commented init and importing different worked, but won't do it
            clip.write_videofile(f'{savename}.mp4')
            clip.close()
        for filename in set(filenames):
            os.remove(filename)


def savenames():
    global savename, graphtype, graphname
    if c0 == 1:
        savename = 'Newtonian'
    if c0 == 2:
        savename = 'Relativistic'
    if c0 == 3:
        savename = f'Precession{n4}pi4'
    if csub == 1:
        graphtype = 'Cartesian'
    if csub == 2:
        graphtype = 'Polar'
    if saveall == 1:
        graphname = f'{graphtype}_{savename}.pdf'
    if saveall == 2:
        graphname = f'{graphtype}_{savename}.png'


def build_gif(files, ):
    savenames()
    # build gif
    with imageio.get_writer(f'{savename}.gif', mode='I') as writer:
        for filename in files:
            image = imageio.imread(filename)
            writer.append_data(image)


def cartesian_background(rpp, tph_i, tph_f):
    graph_boolean(True)
    # apsides
    orbit_apsides(rp, tph_i, tph_f)  # Perihelion circle
    orbit_apsides(raph, tph_i, tph_f)  # Aphelion circle
    # Newtonian perihelion
    ax.plot(tph_i, rpp, '*', markersize=10, color=(0.3, 0.3, 0.3))
    # Setting axis
    plt.xticks(fontsize=11)
    plt.yticks(fontsize=11)
    plt.ylabel(r"$r$(m)", fontsize=12)
    plt.xlabel(r"$\varphi$(rad)", fontsize=12)
    ax.set_yticks([4 * (10 ** 10), 4.5 * (10 ** 10), 5 * (10 ** 10), 7 * (10 ** 10)])  # Less radial ticks


def polar_background(rpp, tph_i, tph_f):
    graph_boolean(False)
    # apsides
    orbit_apsides(rp, tph_i, tph_f)  # Perihelion circle
    orbit_apsides(raph, tph_i, tph_f)  # Aphelion circle
    # Newtonian perihelion
    ax.plot(0, rpp, '*', markersize=8, color=(0.3, 0.3, 0.3))
    # Changing polar labels
    ax.set_rmax(7.5 * (10 ** 10))
    ax.set_rticks([4 * (10 ** 10), 5 * (10 ** 10), 7 * (10 ** 10)])  # Less radial ticks
    rad = ['0', r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$', r'$\frac{5\pi}{4}$',
           r'$\frac{3\pi}{2}$', r'$\frac{7\pi}{4}$']
    rs = plt.xticks()[0]
    plt.xticks(rs, rad)


def graph_save():
    global savegraph, saveall
    print('¿Desea guardar esta gráfica?')
    savegraph = input('De ser así escriba "s" y presione enter, caso contrario escriba cualquier otra tecla'
                       ' y/o presione enter:\n')
    if savegraph == 's':
        print('1. Pdf: Para guardar en formato ".pdf" escriba 1 y presione enter.')
        print('2. Png: Para guardar en formato ".png" escriba 2 y presione enter.')
        time.sleep(1)
        saveall = int(input('Escriba su opción, por favor:\n'))
        while saveall not in range(1, 3):
                print(f'El número correspondiente a la opción debe ser natural y debe estar entre 0 y 3 \n')
                time.sleep(1)
                saveall = input('Escriba su opción, por favor:\n')
        quality()


def simulation(dd, th_i, th_f):
    if dd == 0:
        polar_background(rp, th_i, th_f)
        plt.title(r"Simulación polar $r$ vs $\varphi$", va='bottom', fontsize=16)
        theta = th_i + 0.1
        while theta < th_f:
            rn = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(theta)))
            ax.plot(theta, rn, 'g.', markersize=3)
            plt.pause(0.1)
            theta += 0.1
        plt.show()
    else:
        polar_background(rp, th_i, th_f)
        # Newtonian orbit
        thetan = np.arange(th_i + 0.01, th_f, 0.01)
        rn = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(thetan)))
        ax.plot(thetan, rn, 'g')
        # Relativistic perihelion
        ax.plot(th_i, rp, '*', markersize=8, color=(0.6, 0.6, 0.6))
        # Relativistic orbit
        theta = th_i + 0.1
        while theta < th_f:
            rprec = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(theta * (1 - D))))
            ax.plot(theta, rprec, 'b.', markersize=3)
            plt.pause(0.1)
            theta += 0.1
        plt.show()


def graph_boolean(cartesian):
    global fig, ax
    if not cartesian:
        # plotting the orbits
        fig, ax = plt.subplots(figsize=(5, 5), subplot_kw={'projection': 'polar'})
        # Sun
        ax.plot(0, 0, '.', markersize=40, color=(1.0, 0.2, 0.1))
        ax.grid(True)
    else:
        # plotting the orbits
        fig, ax = plt.subplots(figsize=(6, 5))
        ax.grid(True)


def cartesian_graph(dd, th_i, th_f):
    global graphname
    graph_save()
    print('Luego de obervar la gráfica, por favor cerrar la ventana.')
    time.sleep(1)
    if dd == 0:
        cartesian_background(rp, th_i, th_f)
        # Newtonian orbit
        thetan = np.arange(th_i, th_f, 0.01)
        rn = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(thetan)))
        ax.plot(thetan, rn, 'g')
        # Sun
        rssun = 0 * thetan
        ax.plot(thetan, rssun, '.', markersize=10, color=(1.0, 0.2, 0.1))
        plt.title(r"Gráfica cartesiana $r$ vs $\varphi$", va='bottom', fontsize=16)
        if savegraph == 's':
            savenames()
            plt.savefig(graphname, dpi=qqlty)
        plt.show()
    else:
        cartesian_background(rp, th_i, th_f)
        # Newtonian orbit
        thetan = np.arange(th_i, th_f, 0.01)
        rn = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(thetan)))
        ax.plot(thetan, rn, 'g')
        # Sun
        rssun = 0 * thetan
        ax.plot(thetan, rssun, '.', markersize=10, color=(1.0, 0.2, 0.1))
        # Relativistic orbit
        thetar = np.arange(th_i, th_f, 0.1)
        rprec = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(thetar * (1 - D))))
        ax.plot(thetar, rprec, 'b.', markersize=4)
        nr = math.floor(th_f / (2 * math.pi))
        theta2pi = nr * (2 * math.pi)
        ax.plot(theta2pi, rp, '*', markersize=10, color=(0.6, 0.6, 0.6))
        plt.title(r"Gráficas cartesianas $r$ vs $\varphi$", va='bottom', fontsize=16)
        if savegraph == 's':
            savenames()
            plt.savefig(graphname, dpi=qqlty)
        plt.show()


def polar_graph(dd, th_i, th_f):
    global graphname
    graph_save()
    print('Luego de obervar la gráfica, por favor cerrar la ventana.')
    time.sleep(1)
    if dd == 0:
        polar_background(rp, th_i, th_f)
        thetan = np.arange(th_i, th_f, 0.01)
        rn = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(thetan)))
        ax.plot(thetan, rn, 'g')
        plt.title(r"Gráfica polar $r$ vs $\varphi$", va='bottom', fontsize=16)
        if savegraph == 's':
            savenames()
            plt.savefig(graphname, dpi=qqlty)
        plt.show()
    else:
        polar_background(rp, th_i, th_f)
        # Newtonian orbit
        thetan = np.arange(th_i, th_f, 0.01)
        rn = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(thetan)))
        ax.plot(thetan, rn, 'g')
        # Relativistic orbit
        thetar = np.arange(th_i + 0.1, th_f, 0.1)
        rprec = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(thetar * (1 - D))))
        ax.plot(thetar, rprec, 'b.', markersize=3)
        # Relativistic perihelion
        ax.plot(n4 * thetapi4right, rp, '*', markersize=8, color=(0.6, 0.6, 0.6))
        plt.title(r"Gráficas polares $r$ vs $\varphi$", va='bottom', fontsize=16)
        if savegraph == 's':
            savenames()
            plt.savefig(graphname, dpi=qqlty)
        plt.show()


def constants():
    print('CONSTANTES:')
    # Array of constants
    constants_list = ['Constante Gravitacional', 'Velocidad de la luz']
    constants_u = [r'm³kg⁻¹s⁻²', r'ms⁻¹']
    Constants = [G, c]
    Dct = len(Constants)
    for i in range(Dct):
        print(f'{constants_list[i]}:' '  {:.3e}' f' {constants_u[i]}'.format(Constants[i]))
    # List_constants = [constants_list, constants_list_units, Constants]
    # tableConstants = tabulate(List_constants, headers='firstrow', tablefmt='fancy_grid')
    # print(tableConstants)
    time.sleep(2)
    print('\nLa masa del sol es {:.4e} kg.\n'.format(M))
    print('DATOS DE MERCURIO:')
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
    print('\nCANTIDADES CALCULADAS:')
    # Array of computed quantities
    Data_c = [rb, A, h, wp, D, thetapi, algo, 0.21654]
    Data_list_c = ['Eje semi-menor', 'Área', 'Momentum angular por unidad de masa', 'Preecesión', 'Precesión',
                   'Ángulo entre perihelios', 'Número de revoluciones', 'Tiempo entre ángulos \u03C6/4']
    Data_list_u_c = ['m', r'm²', r'm²/s', 'rad/rev', 'rad', 'rad', '', 'siglos']
    # list_tablecalc = [Data_calc_list, Data_calc_list_units, Data_calc]
    # Table_calc= tabulate(list_tablecalc, headers='firstrow', tablefmt='fancy_grid')
    # print(Table_calc)
    Dc = len(Data_c)
    for i in range(Dc):
        print(f'{Data_list_c[i]}:' '  {:.3e}' f' {Data_list_u_c[i]}'.format(Data_c[i]))
    time.sleep(2)


def returning():
    """Returning: This is the last part of the program. It is needed to return to the main menu,
        all the boolean parameters are reset. If no more actions on the program are needed, then it exits the program."""
    global o1, run_program, cartesian_graph_boolean
    print('¿Desea realizar otra acción en el programa?')
    time.sleep(1)
    o1 = input('De ser así escriba "s" y presione enter, caso contrario escriba cualquier otra tecla'
               ' y/o presione enter:\n')
    if o1 == 's':
        run_program = True
        cartesian_graph_boolean = False
    else:
        run_program = False
        print('¡Hasta luego!')
        time.sleep(4)
        sys.exit()


# def timing():
#     timeit.timeit(forloop)
#     timeit.timeit(whileloop)


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
# Starts the algorithm
print('Este es un programa sobre la precesión de Mercurio')
time.sleep(1.5)
print('Se trabaja con la gravitación Newtoniana y la teoría general de la relatividad\n')
run_program = True  # Due to the possibility of returning to the main menu.

while run_program:
    main_menu()  # Displays the simulation options
    if c0 == 1:
        sub_menu()
        if csub == 1:
            cartesian_graph(0, 0, 2 * math.pi)
            returning()
        if csub == 2:
            polar_graph(0, 0, 2 * math.pi)
            returning()
        if csub == 3:
            print('Luego de obervar la simulación, por favor cerrar la ventana.')
            simulation(0, 0, 2 * math.pi)
            returning()
        if int(csub) == 4:
            sub_sub_menu()
            save_simulation(0, 0, 2 * math.pi, csubsub)
            returning()
    if int(c0) == 2:
        theta_i = float(input('Por favor ingrese el ángulo inicial en radianes:\n'))
        theta_f = float(input('Por favor ingrese el ángulo final en radianes:\n'))
        while theta_f < theta_i:
            print('El ángulo final debe ser mayor que el ángulo inicial')
            theta_i = float(input('Por favor ingrese el ángulo inicial en radianes:\n'))
            theta_f = float(input('Por favor ingrese el ángulo final en radianes:\n'))
        sub_menu()
        if csub == 1:
            print('Luego de obervar la gráfica, por favor cerrar la ventana.')
            cartesian_graph(D, theta_i, theta_f)
            returning()
        if csub == 2:
            print('Luego de obervar la gráfica, por favor cerrar la ventana.')
            polar_graph(D, theta_i, theta_f)
            returning()
        if csub == 3:
            print('Luego de obervar la simulación, por favor cerrar la ventana.')
            simulation(D, theta_i, theta_f)
            returning()
        if int(csub) == 4:
            sub_sub_menu()
            save_simulation(D, theta_i, theta_f, csubsub)
            returning()
    if int(c0) == 3:
        n4 = float(input('Ingrese por favor el múltiplo de pi/4 de precesión de la órbita, por favor:\n'))
        while int(n4) not in range(0, 9):
            print(f'El número correspondiente a la opción debe ser entero y debe estrar entre  entre 0 y 8\n')
            time.sleep(1)
            n4 = float(input('Ingrese por favor el múltiplo de pi/4 de precesión de la órbita, por favor:\n'))
        sub_menu()
        if csub == 1:
            print('Luego de obervar la gráfica, por favor cerrar la ventana.')
            cartesian_graph(D, n4 * thetapi4right, n4 * thetapi4right + 2 * np.pi)
            returning()
        if csub == 2:
            print('Luego de obervar la gráfica, por favor cerrar la ventana.')
            polar_graph(D, n4 * thetapi4right, n4 * thetapi4right + 2 * np.pi)
            returning()
        if csub == 3:
            print('Luego de obervar la simulación, por favor cerrar la ventana.')
            simulation(D, n4 * thetapi4right, n4 * thetapi4right + 2 * np.pi)
            returning()
        if int(csub) == 4:
            sub_sub_menu()
            save_simulation(D, n4 * thetapi4right, n4 * thetapi4right + 2 * np.pi, csubsub)
            returning()
    if int(c0) == 4:
        orbits(8)
        time.sleep(1)
        returning()
    if int(c0) == 5:
        constants()
        returning()
    elif int(c0) == 6:
        print('Hasta luego.')
        sys.exit()
# Add Vpyhton?
