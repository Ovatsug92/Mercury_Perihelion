# Import modules
import math
import time
import sys

from vpython import *

# Global variables definition
language: int
language_prec = language_ecc = language_pause = language_run = language_title = language_message = \
    language_bye = language_os = language_o1 = language_o2 = language_o3 = language_i1 = language_i2 = language_g = \
    language_del = language_f1 = language_f2 = language_io = language_if = canv = None
gr: str
ggraph: gcurve
ggrid: graph
E: float
prec: float
r_d: float
r_s: float
ro: float
E_ex: slider
e_graph = sun = mercury = None
prec_sp: slider
prec_text: wtext
b: button
scenes: canvas
E_text: wtext
wtexts: wtext
d: float
o: float
r: float
co = 0


# Functions definitions
def languagemenu():
    """Language menu: Choose only one option for the language, must be between 0-6"""
    global language
    print('Please select your language:')
    print("1. English")
    print("2. Español")
    print("3. Português")
    print("4. Italiano")
    print("5. Deutsch")
    time.sleep(2)
    language = int(input("Please type the number and press 'enter':\n"))
    while (language < 1) or (language > 5):
        language = int(input("Options: 1-5\n"))


def lang():
    """Vocabulary in 5 different languages"""
    global language_prec, language_ecc, language_pause, language_run, language_title, language_message, language_bye, \
        language_os, language_o1, language_o2, language_o3, language_i1, language_i2, language_g, language_del, \
        language_f1, language_f2, language_io, language_if
    if language == 1:
        language_prec = 'Precession'
        language_ecc = 'Eccentricity'
        language_pause = 'Pause'
        language_run = 'Run'
        language_title = "Simulation of Mercury's perihelion precession \n\n"
        language_message = 'Select the precession, in radians, from 0 to 0.1'
        language_bye = 'See you later!'
        language_os = 'Choose one option that you would like to perform from the following list'
        language_o1 = 'Perform the simulation with unbounded angle and with orbital slider parameters'
        language_o2 = 'Perform the simulation with bounded angle and with orbital slider parameters'
        language_o3 = 'Exit the program'
        language_i1 = 'Write the number of the chosen option and press enter, please'
        language_i2 = 'The number must be an integer between 0 and 4'
        language_g = "Would you like to show the graph 'R vs \u03C6' in real time simulation, also?"
        language_del = 'Would you like to erase the last canvas?'
        language_f1 = 'Do you want to perform another action in the program?'
        language_f2 = "If so, write 'y' and press 'enter'; otherwise write any other key and/or press 'enter'"
        language_io = "Please write the initial angle (in radians) and press 'enter'"
        language_if = "Please write the final angle (in radians) and press 'enter'"
    if language == 2:
        language_prec = 'Precesión'
        language_ecc = 'Excentricidad'
        language_pause = 'Pausar'
        language_run = 'Ejecutar'
        language_title = 'Simulación de la precesión del perihelio de Mercurio\n\n'
        language_message = 'Seleccione la precesión, en radianes, de 0 a 0.1'
        language_bye = '¡Hasta luego!'
        language_os = 'Escoja una opción que le gustaría realizar de la siguiente lista'
        language_o1 = 'Realizar la simulación con ángulo no acotado y con los parámetros orbitales deslizables'
        language_o2 = 'Realizar la simulación con ángulo acotado y con los parámetros orbitales deslizables'
        language_o3 = 'Salir del programa'
        language_i1 = 'Escriba el número de la opción elegida y presione enter, por favor'
        language_i2 = 'El número debe ser entero y estar entre 0 y 4'
        language_g = "Le gustaría también mostrar la gráfica 'R vs \u03C6' en simulación de tiempo real?"
        language_del = '¿Le gustaría eliminar el último canvas?'
        language_f1 = '¿Desea realizar otra acción en el programa?'
        language_f2 = "De ser así, escriba 'y' y presione 'enter'; caso contrario escriba cualquier otra tecla y/o " \
                      "presione 'enter'"
        language_io = "Por favor escriba el ángulo inicial (en radianes) y presione 'enter'"
        language_if = "Por favor escriba el ángulo final (en radianes) y presione 'enter'"
    if language == 3:
        language_prec = 'Precessão'
        language_ecc = 'Excentricidade'
        language_pause = 'Pausar'
        language_run = 'Executar'
        language_title = 'Simulação da precessão do periélio de Mercúrio\n\n'
        language_message = 'Selecione a precessão, em radianos, de 0 a 0,1'
        language_bye = 'Até logo!'
        language_os = 'Escolha uma opção que você gostaria de executar na lista seguente'
        language_o1 = 'Fazer a simulação com um ângulo sem limite e com os parâmetros orbitais deslizantes'
        language_o2 = 'Fazer a simulação com um ângulo com limite e com os parâmetros orbitais deslizantes'
        language_o3 = 'Sair do programa'
        language_i1 = 'Escreva o número da opção escolhida e pressione enter, por favor'
        language_i2 = 'O número deve ser um número inteiro e estar entre 0 e 4'
        language_g = "Também gostaria de exibir o gráfico 'R vs \u03C6' na simulação em tempo real?"
        language_del = 'Gostaria de apagar o último canvas?'
        language_f1 = 'Deseja executar outra ação no programa?'
        language_f2 = "Se é assim, digite 'y' e pressione enter; caso contrário digite qualquer outra tecla e/ou " \
                      "pressione 'enter' "
        language_io = "Por favor digite o ângulo inicial (em radianos) e pressione 'enter'"
        language_if = "Por favor digite o ângulo final (em radianos) e pressione 'enter'"
    if language == 4:
        language_prec = 'Precessione'
        language_ecc = 'Eccentricità'
        language_pause = 'Mettere in pausa'
        language_run = 'Eseguire'
        language_title = 'Simulazione della precessione del perielio di Mercurio\n\n'
        language_message = 'Seleziona la precessione, in radianti, da 0 a 0,1'
        language_bye = 'Arrivederci!'
        language_os = "Scegli un'opzione che desideri eseguire dall'elenco seguente"
        language_o1 = 'Fai la simulazione con un angolo illimitato e con i parametri orbitali scorrevoli'
        language_o2 = "Fai la simulazione con un angolo limitato e con i parametri orbitali scorrevoli"
        language_o3 = 'Uscire dal programma'
        language_i1 = "Scrivi il numero dell'opzione scelta e premi 'enter', per favore"
        language_i2 = 'Il numero deve essere un numero intero ed essere compreso tra 0 e 4'
        language_g = "Vuoi mostrare anche il grafico 'R vs \u03C6' in una simulazione in tempo reale?"
        language_del = "Vuoi cancellare l'ultimo canvas?"
        language_f1 = "Vuoi eseguire un'altra azione nel programma?"
        language_f2 = "In tal caso, digita 'y' e premi 'enter'; altrimenti digita un qualsiasi altro tasto e/o premi " \
                      "'enter' "
        language_io = "Per favore digita l'angolo iniziale (in radianti) e premi 'enter'"
        language_if = "Per favore digita l'angolo finale (in radianti) e premi 'enter'"
    if language == 5:
        language_prec = 'Präzession'
        language_ecc = 'Exzentrizität'
        language_pause = 'Pausieren'
        language_run = 'Ausführen'
        language_title = 'Simulation der Präzession des Merkurperihels\n\n'
        language_message = 'Wählen Sie die Präzession im Bogenmaß von 0 bis 0,1'
        language_bye = 'Bis gleich!'
        language_os = 'Wählen Sie eine Option zum Ausführen aus der folgenden Liste aus'
        language_o1 = 'Die Simulation mit einem unbeschränkte Winkel und mit den gleitenden Orbitalparametern Ausführen'
        language_o2 = 'Die Simulation mit einem beschränkte Winkel und mit den gleitenden Orbitalparametern Ausführen'
        language_o3 = 'Programm beenden'
        language_i1 = 'Schreiben Sie die Nummer der gewählten Option und drücken Sie bitte die Eingabetaste'
        language_i2 = 'Die Nummer muss eine Ganzzahl sein und zwischen 0 und 4 liegen'
        language_g = "Möchten Sie den Graphen 'R vs \u03C6' uch in Echtzeitsimulation anzeigen?"
        language_del = "Möchten Sie die letzte Leinwand löschen??"
        language_f1 = 'Möchten Sie eine andere Aktion im Programm ausführen?'
        language_f2 = "Wenn dies der Fall ist, geben Sie 'y' ein und drücken Sie die Eingabetaste; Geben Sie " \
                      "andernfalls eine andere Taste ein und/oder drücken Sie die Eingabetaste "
        language_io = "Bitte geben Sie den Startwinkel (im Bogenmaß) ein und drücken Sie die Eingabetaste"
        language_if = "Bitte geben Sie den Endwinkel (im Bogenmaß) ein und drücken Sie die Eingabetaste"
    return


def main_menu():
    """Main menu: Choose only one option between 0-4"""
    global co
    # Main menu
    print(f'{language_os}:\n')
    time.sleep(1.5)
    print(f'1. {language_o1}.')
    print(f'2. {language_o2}.')
    print(f'3. {language_o3}.\n')
    time.sleep(2)
    co = int(input(f'{language_i1}:\n'))
    while (co < 1) or (co > 3):
        print(f'{language_i2}.')
        time.sleep(1)
        co = int(input(f'{language_i1}:\n'))


def scene_data():
    """Scene data: This builds the canvas, on which the simulation will be done, also asks if the 2D-graph 'R vs
    angle' is wanted. All the data needed is here, it is shown the scale of distance and radius, also.. """
    global gr, ro, prec, E, E_ex, E_text, sun, mercury, prec_sp, prec_text, scenes, b, wtexts
    # Asking for 2-D graph R vs \u03C6 in real time simulation
    print(f'{language_g}')
    time.sleep(1)
    gr = input(f'{language_f2}:\n')
    # DATA
    g_constant = 6.67435 * (10 ** (-11))  # m**3 kg−1 s**−2 with a relative uncertainty of 19 ppm.
    c = 299792458  # m/s
    # Bulk parameters:  Sun
    m_sun = 1988500 * (10 ** 24)  # Mass:    kg
    rvolsun = 695700 * 10 ** 3  # Volumetric mean radius	m.
    # Bulk parameters:  Mercury
    # m_merc = 0.330 * (10 ** 24)  # mass  Order of 10**24 kg
    rvolmerc = 2439.7 * 10 ** 3  # Volumetric mean radius   m.
    rp = 46.000 * (10 ** 9)  # meters  perihelion
    # Schwarzschild radius of objets
    # rs_m = 2 * m_merc * g / (c ** 2)  # Mercury
    rs_sun = 2 * m_sun * g_constant / (c ** 2)  # Sun
    # Scaled radius of objects
    rvlogsun = math.log((rvolsun * 10 ** 32) / (c ** 4 * rs_sun), 10)  # 3.46   Scaled radius of Sun
    rvlogm = math.log((rvolmerc * 10 ** 32) / (c ** 4 * rs_sun), 10)  # 1.01   Scaled radius of Mercury
    # Orbital parameters
    E = 0.206
    ro = rp / (2 * 10 ** 9)
    prec = 0
    # Scene building
    scenes = canvas(title=f'<b>{language_title}<b>\n', range=36, autoscale=0, forward=vector(0, -.3, -1))
    # Button
    b = button(text=f'{language_run}', pos=scenes.title_anchor, bind=runpause)
    wtexts = wtext(text=f'{language_message}\n\n')
    # Precession slider
    prec_sp = slider(bind=sliderprec, vertical=False, min=0, max=0.101, step=0.001, length=670, width=10)
    prec_text = wtext(text=f'{language_prec} = ' '{:.3f}'.format(prec) + "\n\n")
    # Eccentricity slider
    E_ex = slider(bind=sliderecc, vertical=False, min=0, max=0.9, step=0.001, length=670, width=10)
    E_text = wtext(text=f'{language_ecc}= ' '{:.2f}'.format(E) + "\n\n")
    # 3D objects
    sun = sphere(pos=vector(0, 0, 0), radius=rvlogsun,
                 texture="https://upload.wikimedia.org/wikipedia/commons/b/b4"
                         "/The_Sun_by_the_Atmospheric_Imaging_Assembly_of_NASA%27s_Solar_Dynamics_Observatory_"
                         "-_20100819.jpg")
    mercury = sphere(pos=vector(0, 0, 0), radius=rvlogm,
                     texture="https://upload.wikimedia.org/wikipedia/commons/3/30/Mercury_in_color_"
                             "-_Prockter07_centered.jpg",
                     make_trail=True, trail_type='points', interval=10, retain=120)
    # Widget to stop simulation with mouse click
    scenes.bind('click', stop)


def simulation(oi, of):
    """Simulation: This is the main function that builds the 3-D plot."""
    global o, d, r, o_i, o_f, ggraph, ggrid
    # Making the Orbit: "While" iterations
    o = 0  # Angle variable definition and initial condition.
    d = 0.01  # Angle step size.
    o_i = oi
    o_f = of
    if gr == 'y':
        ggrid = graph(title='R vs \u03C6', xtitle='\u03C6', ytitle='R', scroll=True, fast=False, xmin=0, xmax=10)
        ggraph = gcurve(color=color.red)
    while o < o_f and brk == 1:
        if run and stopp and gr == 'y':
            rate(500)  # Number of iterations per second.
            r = ro / (1 + E * cos(o * (1 - prec)))  # Ellipse equation (polar coordinates, focus in the origin).
            # Prec: From slider
            pos = vector(r * cos(o), r * sin(o), 0)  # Definition of Mercury's position vector.
            mercury.pos = r * pos.hat  # New Mercury's position, replaces object's position.
            ggraph.plot(o, r)
            o = o + d  # Iteration process.
        if run and stopp and not gr == 'y':
            rate(500)  # Number of iterations per second.
            r = ro / (1 + E * cos(o * (1 - prec)))  # Ellipse equation (polar coordinates, focus in the origin).
            # Prec: From slider
            pos = vector(r * cos(o), r * sin(o),
                         0)  # Definition of Mercury's position vector. Angle "o" from iterations
            mercury.pos = r * pos.hat  # New Mercury's position, replaces object's position.
            o = o + d  # Iteration process.


def returning():
    """Returning: This is the last part of the program. It is needed to return to the main menu,
    all the boolean parameters are reset. If no more actions on the program are needed, then it exits the program."""
    global run_program, run, stopp, brk
    # Deleting last canvas
    print(f'{language_del}')
    time.sleep(1)
    del1 = input(f'{language_f2}:\n')
    if del1 == 'y':
        delall()
    # Return to menu or exit
    print(f'{language_f1}')
    time.sleep(1)
    o1 = input(f'{language_f2}:\n')
    if o1 == 'y':
        run_program = True
        # Returning to initial values of iteration
        run = False
        stopp = True
        brk = 1
    else:
        run_program = False
        print(f'{language_bye}')
        time.sleep(4)
        sys.exit()


def sliderprec():
    """Slider precession parameter: This is the text and variable displayed near the precession slider."""
    global prec
    prec_text.text = f'{language_prec} = ' '{:.3f}'.format(prec) + "\n\n"
    prec = prec_sp.value  # Replaces the precession in radial equation with the precession from slider.


def sliderecc():
    """Slider eccentricity parameter: This is the text and variable displayed near the eccentricity slider."""
    global E
    E_text.text = f'{language_ecc} = ' '{:.3f}'.format(E) + "\n\n"
    E = E_ex.value  # Replaces the eccentricity in radial equation with the eccentricity from slider.


run = False  # Boolean variable for run and pause function on button.


def runpause(pp):
    """Run and pause function: This shows the options to run and pause the program,
    but also indicates the action on the simulation with a temporal variable 'r_d'.
    The action works when clicking on the button."""
    global run, r_d, d
    run = not run
    if run:
        pp.text = f'{language_pause}'
        d = r_d
    else:
        pp.text = f'{language_run}'
        r_d = d
        d = 0


stopp = True  # Boolean variable for stop function on mouse.
brk = 1  # auxiliary variable for breaking the while loop on the simulation.


def stop():
    """Stop function: This is used to break the while loop when clicking on the simulation part of the canvas.
    Temporal variable r_s and auxiliary variable brk are needed."""
    global stopp, r_s, d, o, brk
    stopp = not stopp
    if stopp:
        d = r_s
    else:
        r_s = d
        brk = 0


def delall():
    """Delete all function: To delete all objects on the canvas, but text widgets -wtext."""
    scenes.delete()
    b.delete()
    wtexts.delete()
    prec_sp.delete()
    prec_text.delete()
    E_ex.delete()
    E_text.delete()
    if gr == 'y':
        ggrid.delete()
        ggraph.delete()


# Starts algorithm
languagemenu()  # Displays the languages menu.
lang()  # Replaces the words from the vocabulary of the selected language.
run_program = True  # Due to the possibility of returning to the main menu.
while run_program:
    main_menu()  # Displays the simulation options
    if co == 1:
        scene_data()  # Preparing the canvas
        simulation(0, 1000000)  # plotting the orbits
        returning()  # Returning to the main menu
    if co == 2:
        o_i = float(input(f'{language_io}:\n'))  # Asking for the initial angle
        o_f = float(input(f'{language_if}:\n'))  # Asking for the final angle
        scene_data()  # Preparing the canvas
        simulation(o_i, o_f)  # plotting the orbits
        returning()  # Returning to the main menu
    elif int(co) == 3:
        print(f'{language_bye}.')  # Print message
        sys.exit()  # Exiting program
