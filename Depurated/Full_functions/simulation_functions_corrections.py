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
from moviepy.video.io.VideoFileClip import VideoFileClip

# Variables definition (global at module level)
save_all = save_graph = c_main = c_sub = c_sub_sub = global_quality = 0
graph_type, save_name, graph_name, filename = (str,) * 4
cartesian_graph_boolean: None
fig, ax = plt.subplots()
plt.close()
# Dictionaries
language_1 = {"language_main_1": "Escoger una opción que le gustaría realizar de la siguiente lista:"}
language_2 = {"language_main_1": "Escoger una opción que le gustaría realizar de la siguiente lista:"}
language_3 = {"language_main_1": "Escoger una opción que le gustaría realizar de la siguiente lista:"}
language_4 = {"language_main_1": "Escoger una opción que le gustaría realizar de la siguiente lista:"}
language_5 = {"language_main_1": "Escoger una opción que le gustaría realizar de la siguiente lista:"}
# Lists
languages = [language_1, language_2, language_3, language_4, language_5]  # List from dictionaries
language_list = ['English', 'Español', 'Português', 'Italiano', 'Deutsch']  # List for the languages
names = ['simulación newtoniana de la órbita de Mercurio',
         'simulación relativista de la órbita de Mercurio comprendida entre dos ángulos',
         'simulación relativista de la órbita de Mercurio precesada en un múltiplo de \u03C0/4 radianes']
sub_names = ['cartesiana', 'polar']
filenames = []
# For latex text on plots
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
mpl.rcParams['agg.path.chunksize'] = 10000


# Functions
def main_menu():
    """Main menu: Choose only one option between 0-7"""
    global c_main
    l = 0
    print(f"{languages[l]['language_main_1']}:")
    # print('Escoger una opción que le gustaría realizar de la siguiente lista:')
    time.sleep(1.5)
    i = 0
    while i < len(names):
        print(f'{i + 1}. Realizar la {names[i]}.')
        i += 1
    print('4. Mostrar las gráficas de las órbitas precesadas en múltiplos de \u03C0/4 radianes.')
    print('5. Mostrar los datos usados en este programa.')
    print('6. Salir del programa.\n')
    time.sleep(3)
    c_main = int(input('Escribir el número de la opción elegida y presionar enter, por favor:\n'))
    while (c_main < 1) or (c_main > 6):
        print(f'El número correspondiente a la opción debe ser entero y debe estrar entre  entre 0 y 9\n')
        time.sleep(1)
        c_main = int(input('Escribir el número de la opción elegida y presionar enter, por favor:\n'))


def sub_menu():
    """Sub menu: After choosing one option of the main menu, choose only one option between 0-4"""
    global c_sub
    print('Escoger una opción que le gustaría realizar de la siguiente lista:')
    time.sleep(1.5)
    i = 0
    while i < len(sub_names):
        print(f"{i + 1}. Mostrar la gráfica {sub_names[i]} 'r vs \u03C6' de la simulación.")
        i += 1
    print('3. Mostar la simulación.')
    print('4. Guardar la simulación.')
    time.sleep(3)
    c_sub = int(input('Escribir el número de la opción elegida y presionar enter, por favor:\n'))
    while (c_sub < 1) or (c_sub > 4):
        print(f'El número correspondiente a la opción debe ser entero y debe estrar entre  entre 0 y 4\n')
        time.sleep(1)
        c_sub = int(input('Escribir el número de la opción elegida y presionar enter, por favor:\n'))


def sub_sub_menu():
    """Sub, sub menu: After choosing one option of the main menu, and the option of the sub menu was 'save simulation',
    choose only one option for saving: '.gif' or '.mp4' extension"""
    global c_sub_sub
    # Menu for saving
    print('Escoger una opción que le gustaría realizar de la siguiente lista:')
    time.sleep(1.5)
    print('1. Gif: Para guardar la simulación en animación ".gif" escriba 1 y presione enter.')
    print('2. Mp4: Para guardar la simulación en video ".mp4" escriba 2 y presione enter.')
    time.sleep(1)
    c_sub_sub = int(input('Escriba su opción, por favor:\n'))
    while (c_sub_sub < 1) or (c_sub_sub > 3):
        print(f'El número correspondiente a la opción debe ser entero y debe estrar entre  entre 0 y 3')
        time.sleep(1)
        c_sub_sub = int(input('Escribir el número de la opción elegida y presionar enter, por favor:\n'))


def quality():
    """Quality: This saves the user required quality for saving images. Each number is normalized to 120 dpi."""
    global global_quality
    local_quality = input('Escriba por favor la calidad de imágenes que desea en una escala del 1 al 10:\n')
    while int(local_quality) not in range(1, 11):
        print(f'El número correspondiente a la opción debe ser natural y debe estar entre 0 y 11 \n')
        time.sleep(1)
        local_quality = input('Escriba por favor la calidad de imágenes que desea en una escala del 1 al 10:\n')
    global_quality = int(local_quality) * 120


def graph_save():
    """Saving Graphs: For graphs options (not simulation),choose only one option for saving:
     '.pdf' or '.png' extension"""
    global save_graph, save_all
    if c_main == 1 or c_main == 2 or c_main == 3:
        print('¿Desea guardar esta gráfica?')
    elif c_main == 4:
        print('¿Desea guardar las órbitas indivudales?')
    save_graph = input('De ser así escriba "s" y presione enter, caso contrario escriba cualquier otra tecla'
                       ' y/o presione enter:\n')
    if save_graph == 's':
        print('1. pdf: Para guardar en formato ".pdf" escriba 1 y presione enter.')
        print('2. png: Para guardar en formato ".png" escriba 2 y presione enter.')
        time.sleep(1)
        save_all = int(input('Escriba su opción, por favor:\n'))
        while save_all not in range(1, 3):
            print(f'El número correspondiente a la opción debe ser natural y debe estar entre 0 y 3 \n')
            time.sleep(1)
            save_all = input('Escriba su opción, por favor:\n')
        quality()


def save_names():
    """Saving file's name: Assign names to the graphs to create the files."""
    global save_name, graph_type, graph_name
    if c_main == 1:
        save_name = 'Newtonian'
    if c_main == 2:
        save_name = 'Relativistic'
    if c_main == 3:
        save_name = f'Precession{n4}pi4'
    if c_sub == 1:
        graph_type = 'Cartesian'
    if c_sub == 2:
        graph_type = 'Polar'
    if save_all == 1:
        graph_name = f'{graph_type}_{save_name}.pdf'
    if save_all == 2:
        graph_name = f'{graph_type}_{save_name}.png'


def orbit_apsides(r_apsides, phi_i, phi_f):
    """Orbits of apsides: Plot the orbtits of the perihelion and aphelion, both cartesian and polar."""
    # Array of radian values
    phi = np.arange(phi_i, phi_f, 0.01)
    # Circles
    r = r_apsides * (phi ** 0)
    # Perihelion Circle
    if r_apsides == r_perihelion:
        ax.plot(phi, r, 'r')
    # Aphelion Circle
    elif r_apsides == r_aphelion:
        ax.plot(phi, r, 'y')


def point_perihelion(d_d, phi_i, phi_f):
    """Perihelion points: On the interval [phi_i, phi_f], plots the newtonian perihelion as a dark gray star and the
    relativistic perihelion as a light gray star. For the latter: If phi_perihelion < phi_i, uses ceiling;
    if phi_perihelion < phi_i, floor. """
    # Newtonian perihelion
    n_2pi = math.ceil(phi_i / (2 * math.pi))  # Number of multiples of 2*pi on the interval [phi_i,phi_f]
    phi_2pi = n_2pi * (2 * math.pi)
    ax.plot(phi_2pi, r_perihelion, '*', markersize=10, color=(0.3, 0.3, 0.3))
    if d_d == 0:
        pass
    else:
        # Relativistic perihelion
        n_2pi = math.floor(phi_i / T_phi)
        phi_perihelion = n_2pi * T_phi
        if phi_perihelion < phi_i:
            n_2pi = math.floor(phi_f / T_phi)
            phi_perihelion = n_2pi * T_phi
        ax.plot(phi_perihelion, r_perihelion, '*', markersize=10, color=(0.6, 0.6, 0.6))


def graph_boolean(cartesian, phi_i, phi_f):
    """Graph with boolean variable: Main function for plots.
    If True, the plot is cartesian: Plots the apsides, formats and labels the axes.
    If False, the plot is polar: Plots the apsides, formats and labels the axes."""
    global fig, ax
    if not cartesian:
        # plotting the orbits
        fig, ax = plt.subplots(figsize=(5, 5), subplot_kw={'projection': 'polar'})
        # Sun
        ax.plot(0, 0, '.', markersize=40, color=(1.0, 0.2, 0.1))
        ax.grid(True)
        # apsides
        orbit_apsides(r_perihelion, phi_i, phi_f)  # Perihelion circle
        orbit_apsides(r_aphelion, phi_i, phi_f)  # Aphelion circle
        # Changing polar labels
        ax.set_rmax(7.5 * (10 ** 10))
        ax.set_rticks([4 * (10 ** 10), 5 * (10 ** 10), 7 * (10 ** 10)])  # Less radial ticks
        radians = ['0', r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$', r'$\frac{5\pi}{4}$',
                   r'$\frac{3\pi}{2}$', r'$\frac{7\pi}{4}$']
        radii = plt.xticks()[0]
        plt.xticks(radii, radians)
    elif cartesian:
        # plotting the orbits
        fig, ax = plt.subplots(figsize=(6, 5))
        ax.grid(True)
        # apsides
        orbit_apsides(r_perihelion, phi_i, phi_f)  # Perihelion circle
        orbit_apsides(r_aphelion, phi_i, phi_f)  # Aphelion circle
        # Formatting axes
        plt.xticks(fontsize=11)
        plt.yticks(fontsize=11)
        plt.ylabel(r"$r$(m)", fontsize=12)
        plt.xlabel(r"$\varphi$(rad)", fontsize=12)
        ax.set_yticks([4 * (10 ** 10), 4.5 * (10 ** 10), 5 * (10 ** 10), 7 * (10 ** 10)])  # Less radial ticks


def cartesian_graph(d_d, phi_i, phi_f):
    """Cartesian graphs: Plots any option of the simulations in a cartesian graph.
    Uses function 'graph_save' for saving."""
    graph_save()
    print('Luego de obervar la gráfica, por favor cerrar la ventana.')
    time.sleep(1)
    if d_d == 0:
        graph_boolean(True, phi_i, phi_f)
        # Newtonian orbit
        phi_newtonian = np.arange(phi_i, phi_f, 0.01)
        # r_newtonian = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(phi_newtonian)))
        r_newtonian = r0 / (1 + E * np.cos(phi_newtonian))
        ax.plot(phi_newtonian, r_newtonian, 'g')
        point_perihelion(d_d, phi_i, phi_f)
        # Sun
        # r_s_sun = 0 * phi_newtonian
        # ax.plot(phi_newtonian, r_s_sun, '.', markersize=10, color=(1.0, 0.2, 0.1))
        plt.title(r"Gráfica " f'{sub_names[c_sub - 1]} ' r"$r$ vs $\varphi$", va='bottom', fontsize=16)
        if save_graph == 's':
            save_names()
            plt.savefig(graph_name, dpi=global_quality)
        plt.show()
    else:
        graph_boolean(True, phi_i, phi_f)
        # Newtonian orbit
        phi_newtonian = np.arange(phi_i, phi_f, 0.01)
        # r_newtonian = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(phi_newtonian)))
        r_newtonian = r0 / (1 + E * np.cos(phi_newtonian))
        ax.plot(phi_newtonian, r_newtonian, 'g')
        # Sun
        # r_s_sun = 0 * phi_newtonian
        # ax.plot(phi_newtonian, r_s_sun, '.', markersize=10, color=(1.0, 0.2, 0.1))
        # Relativistic orbit
        phi_relativistic = np.arange(phi_i, phi_f, 0.1)
        r_relativistic = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(phi_relativistic * (1 - D))))
        ax.plot(phi_relativistic, r_relativistic, 'b.', markersize=4)
        # Perihelion points
        point_perihelion(d_d, phi_i, phi_f)
        plt.title(r"Gráfica " f'{sub_names[c_sub - 1]} ' r"$r$ vs $\varphi$", va='bottom', fontsize=16)
        if save_graph == 's':
            save_names()
            plt.savefig(graph_name, dpi=global_quality)
        plt.show()


def polar_graph(d_d, phi_i, phi_f):
    """Polar graphs: Plots any option of the simulations in a polar graph.
    Uses function 'graph_save' for saving."""
    graph_save()
    print('Luego de obervar la gráfica, por favor cerrar la ventana.')
    time.sleep(1)
    if d_d == 0:
        graph_boolean(False, phi_i, phi_f)
        phi_newtonian = np.arange(phi_i, phi_f, 0.01)
        # r_newtonian = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(phi_newtonian)))
        r_newtonian = r0 / (1 + E * np.cos(phi_newtonian))
        ax.plot(phi_newtonian, r_newtonian, 'g')
        point_perihelion(d_d, phi_i, phi_f)
        plt.title(r"Gráfica " f'{sub_names[c_sub - 1]} ' r"$r$ vs $\varphi$", va='bottom', fontsize=16)
        if save_graph == 's':
            save_names()
            plt.savefig(graph_name, dpi=global_quality)
        plt.show()
    else:
        graph_boolean(False, phi_i, phi_f)
        # Newtonian orbit
        phi_newtonian = np.arange(phi_i, phi_f, 0.01)
        # r_newtonian = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(phi_newtonian)))
        r_newtonian = r0 / (1 + E * np.cos(phi_newtonian))
        ax.plot(phi_newtonian, r_newtonian, 'g')
        # Relativistic orbit
        phi_relativistic = np.arange(phi_i + 0.1, phi_f, 0.1)
        r_relativistic = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(phi_relativistic * (1 - D))))
        ax.plot(phi_relativistic, r_relativistic, 'b.', markersize=3)
        # Perihelion points
        point_perihelion(d_d, phi_i, phi_f)
        plt.title(r"Gráfica " f'{sub_names[c_sub - 1]} ' r"$r$ vs $\varphi$", va='bottom', fontsize=16)
        if save_graph == 's':
            save_names()
            plt.savefig(graph_name, dpi=global_quality)
        plt.show()


def simulation(d_d, phi_i, phi_f):
    """Simulations: Shows the selected simulation as a while loop of plots."""
    if d_d == 0:
        graph_boolean(False, phi_i, phi_f)
        point_perihelion(d_d, phi_i, phi_f)
        plt.title(r"Simulación polar $r$ vs $\varphi$", va='bottom', fontsize=16)
        phi = phi_i + 0.1
        while phi < phi_f:
            # r_newtonian = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(phi)))
            r_newtonian = r0 / (1 + E * np.cos(phi))
            ax.plot(phi, r_newtonian, 'g.', markersize=3)
            plt.pause(0.1)
            phi += 0.1
        plt.show()
    else:
        graph_boolean(False, phi_i, phi_f)
        point_perihelion(d_d, phi_i, phi_f)
        # Newtonian orbit
        phi_newtonian = np.arange(phi_i + 0.01, phi_f, 0.01)
        # r_newtonian = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(phi_newtonian)))
        r_newtonian = r0 / (1 + E * np.cos(phi_newtonian))
        ax.plot(phi_newtonian, r_newtonian, 'g')
        # Relativistic orbit
        phi = phi_i + 0.1
        while phi < phi_f:
            r_relativistic = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(phi * (1 - D))))
            ax.plot(phi, r_relativistic, 'b.', markersize=3)
            plt.pause(0.1)
            phi += 0.1
        plt.show()


def build_gif(files):
    """Build gif animation: For a simulation, uses saved '.png' files to create the '.gif' animation """
    global filename
    save_names()
    # Building gif
    with imageio.get_writer(f'{save_name}.gif', mode='I') as writer:
        for filename in files:
            image = imageio.imread(filename)
            writer.append_data(image)


def save_simulation(d_d, phi_i, phi_f, save_sub_sub):
    """Save simulation: For specified newtonian or relativistic
    creates an animation '.gif' or a video '.mp4' as selected"""
    global filename
    quality()
    graph_boolean(False, phi_i, phi_f)
    point_perihelion(d_d, phi_i, phi_f)
    p = 0
    print('Por favor, espere unos segundos.')
    # Creating files
    print('Las imágenes procesadas son de muy buena calidad.')
    if d_d == 0:
        plt.title(r"Simulación polar $r$ vs $\varphi$", va='bottom', fontsize=16)
        phi = phi_i + 0.1
        while phi < phi_f:
            p += 1
            # r_newtonian = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(phi)))
            r_newtonian = r0 / (1 + E * np.cos(phi))
            ax.plot(phi, r_newtonian, 'g.', markersize=3)
            filename = f'{p}.png'
            filenames.append(filename)
            plt.savefig(filename, dpi=global_quality)
            phi += 0.1
        if save_sub_sub == 1:
            build_gif(filenames)
        if save_sub_sub == 2:
            build_gif(filenames)
            # Converting gif to mp4
            clip = VideoFileClip(f'Newtonian.gif')
            clip.write_videofile(f'Newtonian.mp4')
            clip.close()
            os.remove(f'{save_name}.gif')
        for filename in set(filenames):
            os.remove(filename)

    else:
        plt.title(r"Simulación polar $r$ vs $\varphi$", va='bottom', fontsize=16)
        # Newtonian orbit
        thetan = np.arange(phi_i + 0.01, phi_f, 0.01)
        # r_newtonian = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(thetan)))
        r_newtonian = r0 / (1 + E * np.cos(thetan))
        ax.plot(thetan, r_newtonian, 'g')
        # Relativistic orbit
        phi = phi_i + 0.1
        while phi < phi_f:
            p += 1
            rprec = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(phi * (1 - D))))
            ax.plot(phi, rprec, 'b.', markersize=3)
            filename = f'{p}.png'
            filenames.append(filename)
            plt.savefig(filename, dpi=global_quality)
            phi += 0.1
        if save_sub_sub == 1:
            build_gif(filenames)
        if save_sub_sub == 2:
            build_gif(filenames)
            # Coverting gif to mp4
            clip = VideoFileClip(
                f'{save_name}.gif')  # commented init and importing different worked, but won't do it
            clip.write_videofile(f'{save_name}.mp4')
            clip.close()
            os.remove(f'{save_name}.gif')
        for filename in set(filenames):
            os.remove(filename)


def orbits(n_orbits):
    """Plotting orbits: Plots all the orbits that shows the precessed perihelion in an angle that is an
    integer multiple of pi/4 on the interval [phi_i, phi_i +2*pi. """
    global save_all, filename
    graph_save()
    time.sleep(1)
    if save_graph == 's':
        for i in range(n_orbits):
            graph_boolean(False, 0, 2 * math.pi)
            # Newtonian orbit
            phi_newtonian = np.arange(0, 2 * math.pi, 0.01)
            # r_newtonian = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(phi_newtonian)))
            r_newtonian = r0 / (1 + E * np.cos(phi_newtonian))
            ax.plot(phi_newtonian, r_newtonian, 'g')
            # Relativistic orbit
            phi_relativistic = np.arange(i * phi_pi4_right + 0.1, i * phi_pi4_right + 2 * math.pi, 0.1)
            r_relativistic = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(phi_relativistic * (1 - D))))
            ax.plot(phi_relativistic, r_relativistic, 'b.', markersize=3)
            # Relativistic perihelion
            ax.plot(i * phi_pi4_right, r_perihelion, '*', markersize=8, color=(0.6, 0.6, 0.6))
            # Newtonian perihelion
            ax.plot(0, r_perihelion, '*', markersize=8, color=(0.3, 0.3, 0.3))
            # Saving
            if save_all == 1:
                filename = f'Orbit_precessed_{i}pi4.pdf'
            elif save_all == 2:
                filename = f'Orbit_precessed_{i}pi4.png'
            plt.savefig(filename, dpi=global_quality)
            plt.close()
    print('¿Desea guardar las órbitas juntas?')
    time.sleep(1)
    save_orbits = input('De ser así escriba "s" y presione enter, caso contrario escriba cualquier otra tecla'
                        ' y/o presione enter:\n')
    time.sleep(1)
    figs, ax_s = plt.subplots(3, 3, figsize=(8, 8), subplot_kw={'projection': 'polar'})
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.8)
    # Saving
    rs = plt.xticks()[0]
    for it in range(3):
        for j in range(3):
            # Array or  radian values
            phi = np.arange(0, 2 * np.pi, 0.01)
            # Circles
            r_perihelion_orbits = r_perihelion * (phi ** 0)  # Perihelion Circle
            r_aphelion_orbits = r_aphelion * (phi ** 0)  # Aphelion Circle
            ax_s[it, j].plot(phi, r_perihelion_orbits, 'r', linewidth=1.5)  # Perihelion Circle
            ax_s[it, j].plot(phi, r_aphelion_orbits, 'y', linewidth=1.5)  # Aphelion Circle
            # Changing polar labels
            ax_s[it, j].set_rmax(7.5 * (10 ** 10))
            ax_s[it, j].set_rticks([])  # Because the full labels were unnecessary and cumbersome to read!
            rad = ['0', r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$', r'$\frac{5\pi}{4}$',
                   r'$\frac{3\pi}{2}$', r'$\frac{7\pi}{4}$']
            ax_s[it, j].set_rlabel_position(0)  # Move radial labels away from plotted line
            ax_s[it, j].grid(True)
            plt.sca(ax_s[it, j])
            plt.xticks(rs, rad)
            # Sun
            ax_s[it, j].plot(0, 0, '.', markersize=20, color=[1.0, 0.2, 0.1])
            # Newtonian orbit
            phi_newtonian = np.arange(0, 2 * np.pi, 0.01)
            # r_newtonian = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(phi_newtonian)))
            r_newtonian = r0 / (1 + E * np.cos(phi_newtonian))
            ax_s[it, j].plot(phi_newtonian, r_newtonian, 'g', linewidth=1.5)
            if it == 0:
                # Title
                ax_s[it, j].set_title(f'Precesión {it + j} veces ' r'$\frac{\pi}{4}$')
                ax_s[it, j].title.set_size(8)
                # Precessed orbit
                phi = np.arange((it + j) * phi_pi_4_observed, (it + j) * phi_pi_4_observed + 2 * math.pi, 0.1)
                r_relativistic = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(phi * (1 - D))))
                ax_s[it, j].plot(phi, r_relativistic, 'b.', markersize=1.5)
                # Relativistic perihelion
                ax_s[it, j].plot((it + j) * phi_pi_4_observed, r_perihelion, '*', markersize=8, color=(0.6, 0.6, 0.6))
            elif it == 1:
                # Title
                ax_s[it, j].set_title(f'Precesión {it + 2 + j} veces ' r'$\frac{\pi}{4}$')
                ax_s[it, j].title.set_size(8)
                # Precessed orbit
                phi = np.arange((it + 2 + j) * phi_pi_4_observed, (it + 2 + j) * phi_pi_4_observed + 2 * math.pi, 0.1)
                r_relativistic = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(phi * (1 - D))))
                ax_s[it, j].plot(phi, r_relativistic, 'b.', markersize=1.5)
                # Relativistic perihelion
                ax_s[it, j].plot((it + 2 + j) * phi_pi_4_observed, r_perihelion, '*', markersize=8, color=(0.6, 0.6, 0.6))
            elif it == 2:
                # Title
                ax_s[it, j].set_title(f'Precesión {it + 4 + j} veces ' r'$\frac{\pi}{4}$')
                ax_s[it, j].title.set_size(8)
                # Precessed orbit
                phi = np.arange((it + 4 + j) * phi_pi_4_observed, (it + 4 + j) * phi_pi_4_observed + 2 * math.pi, 0.1)
                r_relativistic = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(phi * (1 - D))))
                ax_s[it, j].plot(phi, r_relativistic, 'b.', markersize=1.5)
                # Relativistic perihelion
                ax_s[it, j].plot((it + 4 + j) * phi_pi_4_observed, r_perihelion, '*', markersize=8, color=(0.6, 0.6, 0.6))
            # Newtonian perihelion
            ax_s[it, j].plot(0, r_perihelion, '*', markersize=8, color=(0.3, 0.3, 0.3))
    if save_orbits == 's':
        print('1. Pdf: Para guardar en formato ".pdf" escriba 1 y presione enter.')
        print('2. Png: Para guardar en formato ".png" escriba 2 y presione enter.')
        time.sleep(1)
        save_all = input('Escriba su opción, por favor:\n')
        while int(save_all) not in range(1, 3):
            print(f'El número correspondiente a la opción debe ser natural y debe estar entre 0 y 3 \n')
            time.sleep(1)
            save_all = input('Escriba su opción, por favor:\n')
        fig.tight_layout()
        if int(save_all) == 1:
            filename = f'Orbits_precessed_npi4.pdf'
            plt.savefig(filename, dpi=1200)
        elif int(save_all) == 2:
            filename = f'Orbits_precessed_npi4.png'
            plt.savefig(filename, dpi=1200)
    plt.show()


def data():
    """ Constants: Prints all data used in this program, observed and calculated
    """
    print('CONSTANTES:')
    # Array of constants
    constants_list = ['Constante Gravitacional', 'Velocidad de la luz']
    constants_u = [r'm³kg⁻¹s⁻²', r'ms⁻¹']
    constants_values_list = [G, c]
    dct = len(constants_list)
    for i in range(dct):
        print(f'{constants_list[i]}:', '  {:.3e}' f' {constants_u[i]}'.format(constants_values_list[i]))
    # List_constants = [constants_list, constants_list_units, Constants]
    # tableConstants = tabulate(List_constants, headers='firstrow', tablefmt='fancy_grid')
    # print(tableConstants)
    time.sleep(2)
    print('\nLa masa del sol es {:.4e} kg.\n'.format(M))
    print('DATOS DE MERCURIO:')
    # Array of Mercury data
    data_m = [m, Td, T, r_perihelion, r_aphelion, r_a, E]
    data_list_m = ['Masa', 'Periodo Orbital ', 'Periodo Orbital', 'Perihelio ',
                   'Afelio', 'Eje semi-mayor', 'Excentricidad']
    data_list_u_m = ['Kg', 'días', 's', 'm', 'm', 'm', '']
    # list_tablem = [Data_list, Data_list_dim, Data_m]
    # tableMercury = tabulate(list_tablem, headers='firstrow', tablefmt='fancy_grid')
    # print(tableMercury)
    dm = len(data_m)
    for i in range(dm):
        print(f'{data_list_m[i]}:' '  {:.3e}' f' {data_list_u_m[i]}'.format(data_m[i]))
    time.sleep(2)
    print('\nCANTIDADES CALCULADAS:')
    # Array of computed quantities
    data_c = [rb, A, h, dot_w_Vulcan, D, thetapi, algo, 0.21654]
    data_list_c = ['Eje semi-menor', 'Área', 'Momentum angular por unidad de masa', 'Preecesión', 'Precesión',
                   'Ángulo entre perihelios', 'Número de revoluciones', 'Tiempo entre ángulos \u03C6/4']
    data_list_u_c = ['m', r'm²', r'm²/s', 'rad/rev', 'rad', 'rad', '', 'siglos']
    # list_tablecalc = [Data_calc_list, Data_calc_list_units, Data_calc]
    # Table_calc= tabulate(list_tablecalc, headers='firstrow', tablefmt='fancy_grid')
    # print(Table_calc)
    dc = len(data_c)
    for i in range(dc):
        print(f'{data_list_c[i]}:' '  {:.3e}' f' {data_list_u_c[i]}'.format(data_c[i]))
    time.sleep(2)


def returning():
    """Returning: This is the last part of the program. It is needed to return to the main menu,
        all the boolean parameters are reset. If no more actions on the program are needed,
        then it exits the program."""
    global run_program, cartesian_graph_boolean, filenames
    plt.close()
    print('\n¿Desea realizar otra acción del menú principal del programa?')
    time.sleep(1)
    o1 = input('De ser así escriba "s" y presione enter, caso contrario escriba cualquier otra tecla'
               ' y/o presione enter:\n')
    if o1 == 's':
        run_program = True
        cartesian_graph_boolean = False
        filenames = []
    else:
        run_program = False
        print('¡Hasta luego!')
        time.sleep(4)
        sys.exit()


def returning_sub():
    """Returning sub menu: Returns to sub menu or exit the program."""
    plt.close()
    global run_subprogram, cartesian_graph_boolean, filenames
    print(f'¿Desea realizar otra acción del sub menú en la {names[c_main - 1]} .')
    time.sleep(1)
    sub1 = input('De ser así escriba "s" y presione enter, caso contrario escriba cualquier otra tecla'
                 ' y/o presione enter:\n')
    if sub1 == 's':
        run_subprogram = True
        cartesian_graph_boolean = False
        filenames = []
    else:
        run_subprogram = False
        returning()


# def timing():
#     timeit.timeit(forloop)
#     timeit.timeit(whileloop)


# Constants (is G a natural or physical constant?)
G = scipy.constants.G
c = scipy.constants.c
# Data Sun
M = 1988500 * (10 ** 24)
R_vol_M = 695700 * 10 ** 3  # Volumetric mean radius (km)	695,700.    0.006*10**10
# Data Mercury
m = 0.330 * (10 ** 24)  # 10**24 kg
R_vol_m = 2439.7 * 10 ** 3  # Volumetric mean radius (km)	2439.7      0.00024*10**10
Td = 87.969  # days
T = Td * 24 * 60 * 60  # seconds
r_perihelion = 46.000 * (10 ** 9)  # meters (10**6 km) perihelion
r_a = 57.909 * (10 ** 9)  # meters (10**6 km) semi-major axis
r_aphelion = 69.818 * (10 ** 9)  # meters (10**6 km) aphelion
E = 0.20563069  # Eccentricity
# Array of Mercury data
Data_m = [m, Td, T, r_perihelion, r_aphelion, r_a, E]
Data_list = [r'Masa', r'Periodo Orbital ', r'Periodo Orbital', r'perihelio ',
             r'afelio', r'Eje semi-mayor', r'Excentricidad']
Data_list_dim = ['Kg', 'años', 's', 'm', 'm', 'm', '']
# Computed quantities
rs_M = 2 * M * G / (c ** 2)  # Schwarzschild radius Sun 2953.4060640748576  0.0000002953406*10**10
rb = r_a * (1 - E ** 2) ** (1 / 2)  # semiminor
A = math.pi * (r_a * rb)  # Area
h = (2 * A) / T  # angular momemtum per unit mass
dot_w_Vulcan = (6 * math.pi * G * M) / (r_a * c ** 2 * (1 - E ** 2))  # 5.018896261130917e-07
# rad/rev this is the precession of 43"/C
D = dot_w_Vulcan / (2 * math.pi)  # 7.987821488244173e-08 The perturbation in radians
# D = wp/(2*math.pi*0.2408*365*24*3600)  # 1.0518777317095832e-14 This goes to (1-D) in the Eq.
thetapi = 2 * math.pi / (1 - D)  # TO ERASE For new perihelion
wpp = dot_w_Vulcan ** (-1) * 2 * math.pi  # TO ERASE
thetapi4 = wpp * thetapi / 8  # TO ERASE
algo = math.floor(4 * thetapi4 * (1 - D) / math.pi)  # TO ERASE
# phi_pi4_right = algo * math.pi / 4 # TO ERASE
dot_w_Vulcan = (6 * math.pi * G * M) / (r_a * c ** 2 * (1 - E ** 2))  # 5.018896261130917e-07
# rad/rev this is the precession of 43"/C
D = dot_w_Vulcan / (2 * math.pi)
# other
T_D_Vulcan = 2 * math.pi / (1 - D)  # For new perihelion
phi_pi4_right = (math.pi / 4) * (math.floor((2 * math.pi) / dot_w_Vulcan))
# print(algo, thetapi4right, thetapi4)
# r0 = (h ** 2 / (G * M))
r0 = r_a * (1 - E**2)
# For the angle of the pperihelion when precession

# Array of computed quantities
Data_calc = [rb, A, h, dot_w_Vulcan, D, thetapi, algo, 'falta']
Data_calc_list = ['Eje semi-menor', 'Área', 'Momentum angular por unidad de masa', 'Preecesión', 'Precesión',
                  'Ángulo entre perihelios', 'Número de revoluciones', 'Tiempo entre ángulos pi/4']
Data_calc_list_units = ['m', r'$m^2$', r'$m^2/s$', 'rad/rev', 'rad', 'rad', '', 'siglos']
list_tablecalc = [Data_calc_list, Data_calc_list_units, Data_calc]

# Precession
omega_sec_century = 43
omega_rad_rev = omega_sec_century * ((88 * 2 * math.pi) / (3600 * 360 * 100 * 365))  # 5.026e-07 rad/rev
phi_pi_4_observed = (math.pi / 4) * math.floor(2 * math.pi / omega_rad_rev)
# Precession
D_perturbation_observed = omega_rad_rev / (2 * math.pi)  # 7.999e-08
T_phi = (2 * math.pi) / (1 - D_perturbation_observed)
# Starts the algorithm
print('Este es un programa sobre la precesión de Mercurio.')
time.sleep(1.5)
print('Se trabaja con la gravitación newtoniana y la teoría general de la relatividad de Einstein.\n')
run_program = True  # Due to the possibility of returning to the main menu.
while run_program:
    main_menu()  # Displays the simulation options
    run_subprogram = True
    if c_main == 1:
        while run_subprogram:
            sub_menu()
            if c_sub == 1:
                cartesian_graph(0, 0, 2 * math.pi)
                returning_sub()
            if c_sub == 2:
                polar_graph(0, 0, 2 * math.pi)
                returning_sub()
            if c_sub == 3:
                print('Luego de obervar la simulación, por favor cerrar la ventana.')
                simulation(0, 0, 2 * math.pi)
                returning_sub()
            if int(c_sub) == 4:
                sub_sub_menu()
                save_simulation(0, 0, 2 * math.pi, c_sub_sub)
                returning_sub()
    if int(c_main) == 2:
        theta_i = float(input('Por favor ingrese el ángulo inicial en radianes:\n'))
        theta_f = float(input('Por favor ingrese el ángulo final en radianes:\n'))
        while theta_f < theta_i:
            print('El ángulo final debe ser mayor que el ángulo inicial')
            theta_i = float(input('Por favor ingrese el ángulo inicial en radianes:\n'))
            theta_f = float(input('Por favor ingrese el ángulo final en radianes:\n'))
        while run_subprogram:
            sub_menu()
            if c_sub == 1:
                print('Luego de obervar la gráfica, por favor cerrar la ventana.')
                cartesian_graph(D, theta_i, theta_f)
                returning_sub()
            if c_sub == 2:
                print('Luego de obervar la gráfica, por favor cerrar la ventana.')
                polar_graph(D, theta_i, theta_f)
                returning_sub()
            if c_sub == 3:
                print('Luego de obervar la simulación, por favor cerrar la ventana.')
                simulation(D, theta_i, theta_f)
                returning_sub()
            if int(c_sub) == 4:
                sub_sub_menu()
                save_simulation(D, theta_i, theta_f, c_sub_sub)
                returning_sub()
    if int(c_main) == 3:
        n4 = float(input('Ingrese por favor el múltiplo de pi/4 de precesión de la órbita, por favor:\n'))
        while int(n4) not in range(0, 9):
            print(f'El número correspondiente a la opción debe ser entero y debe estrar entre  entre 0 y 8\n')
            time.sleep(1)
            n4 = float(input('Ingrese por favor el múltiplo de pi/4 de precesión de la órbita, por favor:\n'))
        while run_subprogram:
            sub_menu()
            if c_sub == 1:
                print('Luego de obervar la gráfica, por favor cerrar la ventana.')
                cartesian_graph(D, n4 * phi_pi_4_observed, n4 * phi_pi_4_observed + 2 * np.pi)
                returning_sub()
            if c_sub == 2:
                print('Luego de obervar la gráfica, por favor cerrar la ventana.')
                polar_graph(D, n4 * phi_pi_4_observed, n4 * phi_pi_4_observed + 2 * np.pi)
                returning_sub()
            if c_sub == 3:
                print('Luego de obervar la simulación, por favor cerrar la ventana.')
                simulation(D, n4 * phi_pi_4_observed, n4 * phi_pi_4_observed + 2 * np.pi)
                returning_sub()
            if int(c_sub) == 4:
                sub_sub_menu()
                save_simulation(D, n4 * phi_pi_4_observed, n4 * phi_pi_4_observed + 2 * np.pi, c_sub_sub)
                returning_sub()
    if int(c_main) == 4:
        orbits(8)
        time.sleep(1)
        returning()
    if int(c_main) == 5:
        data()
        #    print(f'Luego de {nanim * gh} revoluciones')
        #    print(f'Luego de {nanim * gh * 0.2408 / 100} siglos')
        #    print(f'Luego de {nanim * thetapi4 * (1 - D) / (math.pi / 4)} revoluciones en tehetapi4')
        #    print(f'Luego de {(nanim * thetapi4 * (1 - D) / (math.pi / 4)) * 0.2408 / 100} siglos en tehetapi4')
        returning()
    elif int(c_main) == 6:
        print('Hasta luego.')
        sys.exit()
# Add Vpyhton?
