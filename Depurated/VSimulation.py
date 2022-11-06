import math
import time
import sys

from vpython import *

language_prec = language_ecc = language_pause = language_run = language_title = language_message = \
    language_bye = language_os = language_o1 = language_o2 = language_o3 = language_i1 = language_i2 = language_f1 = \
    language_f2 = language_io = language_if = None
E: float
prec: float
r_d: float
r_s: float
ro: float
E_ex: slider
e_graph = sun = mercury = None
prec_sp: slider
prec_text: wtext
E_text: wtext


def sliderprec():
    global prec
    prec_text.text = 'Precesión = {:.3f}'.format(prec) + "\n\n"
    prec = prec_sp.value
    return


def sliderecc():
    global E
    E_text.text = 'Excentricidad = {:.3f}'.format(E) + "\n\n"
    E = E_ex.value
    return


def lang():
    global language_prec, language_ecc, language_pause, language_run, language_title, language_message, language_bye, \
        language_os, language_o1, language_o2, language_o3, language_i1, language_i2, language_f1, language_f2, \
        language_io, language_if
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
        language_f1 = 'Möchten Sie eine andere Aktion im Programm ausführen?'
        language_f2 = "Wenn dies der Fall ist, geben Sie 'y' ein und drücken Sie die Eingabetaste; Geben Sie " \
                      "andernfalls eine andere Taste ein und/oder drücken Sie die Eingabetaste "
        language_io = "Bitte geben Sie den Startwinkel (im Bogenmaß) ein und drücken Sie die Eingabetaste"
        language_if = "Bitte geben Sie den Endwinkel (im Bogenmaß) ein und drücken Sie die Eingabetaste"
    return


run = False


def runpause(pp):
    global run, r_d, d
    run = not run
    if run:
        pp.text = f'{language_pause}'
        d = r_d
    else:
        pp.text = f'{language_run}'
        r_d = d
        d = 0
    return


def scene_data():
    global ro, prec, E, E_ex, E_text, e_graph, sun, mercury, prec_sp, prec_text
    # scene.caption = """In VPython programs:
    # To rotate "camera", drag with right button or Ctrl-drag.
    # To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
    #   On a two-button mouse, middle is left + right.
    # To pan left/right and up/down, Shift-drag.
    # Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""
    # scene.width = 10
    # scene.height = 10
    # Scene building
    scene.range = 36
    scene.autoscale = 0  # Need to turn off autoscaling to prevent insanity.
    scene.forward = vector(0, -.3, -1)
    scene.title = f'<b>{language_title}<b>\n'
    # Button
    button(text=f'{language_run}', pos=scene.title_anchor, bind=runpause)
    wtext(text=f'{language_message}\n\n')
    # Constants (is G a natural or physical constant?)
    g = 6.67435 * (
            10 ** (-11))  # (6.674 35 ± 0.000 13)*10**(-11) m**3 kg−1 s**−2 with a relative uncertainty of 19 ppm.
    c = 299792458  # m/s
    # Data
    # Bulk parameters:  Sun
    m_sun = 1988500 * (10 ** 24)  # Mass:   Order of 10**24 kg
    rvolsun = 695700 * 10 ** 3  # Volumetric mean radius	695,700 km.    0.006*10**10
    # Bulk parameters:  Mercury
    # m_merc = 0.330 * (10 ** 24)  # mass  Order of 10**24 kg
    rvolmerc = 2439.7 * 10 ** 3  # Volumetric mean radius  2439.7 km.      0.00024*10**10
    rp = 46.000 * (10 ** 9)  # meters (10**6 km) perihelion
    # Schwarzschild radius of objets
    # rs_m = 2 * m_merc * g / (c ** 2)  # Mercury
    rs_sun = 2 * m_sun * g / (c ** 2)  # Sun
    # Scaled radius of objects
    rvlogsun = math.log((rvolsun * 10 ** 32) / (c ** 4 * rs_sun), 10)  # 3.46   Scaled radius of Sun
    rvlogm = math.log((rvolmerc * 10 ** 32) / (c ** 4 * rs_sun), 10)  # 1.01   Scaled radius of Mercury
    # Orbital parameters
    E = 0.206
    ro = rp / (2 * 10 ** 9)
    prec = 0
    # Precession slider
    prec_sp = slider(bind=sliderprec, vertical=False, min=0, max=0.101, step=0.001, length=670, width=10)
    prec_text = wtext(text=f'{language_prec} = ' '{:.3f}'.format(prec) + "\n\n")
    # Eccentricity slider
    E_ex = slider(bind=sliderecc, vertical=False, min=0, max=0.9, step=0.001, length=670, width=10)
    E_text = wtext(text=f'{language_ecc}= ' '{:.2f}'.format(E) + "\n\n")
    e_graph = gcurve(color=color.blue)
    sun = sphere(pos=vector(0, 0, 0), radius=rvlogsun,
                 texture="https://upload.wikimedia.org/wikipedia/commons/b/b4"
                         "/The_Sun_by_the_Atmospheric_Imaging_Assembly_of_NASA%27s_Solar_Dynamics_Observatory_"
                         "-_20100819.jpg")
    mercury = sphere(pos=vector(0, 0, 0), radius=rvlogm,
                     texture="https://upload.wikimedia.org/wikipedia/commons/3/30/Mercury_in_color_"
                             "-_Prockter07_centered.jpg",
                     make_trail=True, trail_type='points', interval=10, retain=120)
    scene.bind('click', stop)
    return


stopp = True


def stop():
    global stopp, r_s, d, o
    stopp = not stopp
    if stopp:
        d = r_s
    else:
        r_s = d
        o = o_f


# Language menu
print('Please select your language:')
print("1. English")
print("2. Español")
print("3. Português")
print("4. Italiano")
print("5. Deutsch")
time.sleep(2)
language = int(input("Please type the number and press 'enter':\n"))
while (language < 0) or (language > 5):
    language = int(input("Options: 1-5\n"))
lang()
run_program = True

while run_program:
    # Principal list
    print(f'{language_os}:\n')
    time.sleep(1.5)
    print(f'1. {language_o1}.')
    print(f'2. {language_o2}.')
    print(f'3. {language_o3}.\n')
    time.sleep(2)
    c0 = input(f'{language_i1}:\n')
    while int(c0) not in range(1, 3):
        print(f'{language_i2}.\n')
        time.sleep(1)
        c0 = input(f'{language_i1}:\n')
    if int(c0) == 1:
        scene_data()
        # Making the Orbit: "While" iterations
        o = 0  # Angle variable definition and initial condition.
        d = 0.01  # Angle step size.
        # graph(scroll=True, fast=False, xmin=0, xmax=10)
        # g = gcurve()
        o_f = 1000000
        while o < o_f:
            if run and stopp:
                rate(500)  # Number of iterations per second.
                r = ro / (1 + E * cos(o * (1 - prec)))  # Ellipse equation (polar coordinates, focus in the origin).
                # Prec: From slider
                pos = vector(r * cos(o), r * sin(o),
                             0)  # Definition of Mercury's position vector. Angle "o" from iterations
                mercury.pos = r * pos.hat  # New Mercury's position, replaces object's position.
                # g.plot(o, r)
                o = o + d  # Iteration process.
        # Return to menu or exit
        print(f'{language_f1}\n')
        time.sleep(1)
        o1 = input(f'{language_f2}:\n')
        if o1 == 'y':
            run_program = True
        else:
            run_program = False
            print(f'{language_bye}')
            time.sleep(4)
            sys.exit()
    # plotting the orbits
    if int(c0) == 2:
        o_i = float(input(f'{language_io}:\n'))
        o_f = float(input(f'{language_if}:\n'))
        scene_data()
        # Making the Orbit: "While" iterations
        o = o_i  # Angle variable definition and initial condition.
        d = 0.01  # Angle step size.
        while o < o_f:
            if run:
                rate(500)  # Number of iterations per second.
                r = ro / (1 + E * cos(o * (1 - prec)))  # Ellipse equation (polar coordinates, focus in the origin).
                # Prec: From slider
                pos = vector(r * cos(o), r * sin(o), 0)  # Definition of Mercury's position vector. Angle "o" from
                # iterations
                mercury.pos = r * pos.hat  # New Mercury's position, replaces object's position.
                o = o + d  # Iteration process.
        # Return to menu or exit
        print(f'{language_f1}\n')
        time.sleep(1)
        o1 = input(f'{language_f2}:\n')
        if o1 == 'y':
            run_program = True
        else:
            run_program = False
            print(f'{language_bye}')
            time.sleep(4)
            sys.exit()
    elif int(c0) == 4:
        print(f'{language_bye}.')
        sys.exit()
