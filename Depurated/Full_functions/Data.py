import math
import scipy
import scipy.constants as constant
import numpy as np
# Constants (is G a natural or physical constant?)
G = scipy.constants.G
c = scipy.constants.c
# Data Sun
M = 1988500 * (10 ** 24)
R_vol_M = 695700 * 10 ** 3  # Volumetric mean radius (km)	695,700.    0.006*10**10
# Data Mercury
# Bulk
m = 0.330 * (10 ** 24)  # 10**24 kg
R_vol_m = 2439.7 * 10 ** 3  # Volumetric mean radius (km)	2439.7      0.00024*10**10
# Orbital
Td = 87.969  # days
T = Td * 24 * 3600  # seconds 7600521.6  760.052 10**4 7.601e+06 s
r_a = 57.909 * (10 ** 9)  # meters (10**6 km) semi-major axis
E = 0.20563069  # Eccentricity

# Precession
omega_sec_century = 43
# w_rad_century = w_sec_century / (3600 * 360)  # 3.318e-05 rad/century
omega_rad_rev = omega_sec_century * ((88 * 2 * math.pi) / (3600 * 360 * 100 * 365))  # 5.026e-07 rad/rev
#  phi for next pi/4 precession of perihelion
phi_pi4_precession = (2 * math.pi)*(2 * math.pi)/(8 * omega_rad_rev)
revolutions = (2 * math.pi) / omega_rad_rev  # revolutions

# Calculated quantities
alpha_orbital = (r_a * (1 - E**2))  # alpha is latus rectus?  5.546e+10

# Used in VPython, not in Python
rs_M = 2 * M * G / (c ** 2)  # Schwarzschild radius Sun 2953.4060640748576  0.0000002953406*10**10

# Is this used?
rb = r_a * (1 - E ** 2) ** (1 / 2)  # semiminor
A = math.pi * (r_a * rb)  # Area
h = (2 * A) / T  # angular momemtum per unit mass
alpha_bulk = (h ** 2 / (G * M))  # 5.546e+10

# D = 7.987821488244173e-08  # Is this right?
r_perihelion = 46.000 * (10 ** 9)  # meters (10**6 km) perihelion
r_aphelion = 69.818 * (10 ** 9)

# D the perturbation parameter from Binet equation
D_perturbation_equation = (3 * G ** 2 * M ** 2) / (h ** 2 * c ** 2)  # 7.988e-08
# D perturbation parameter from precession observed value
D_perturbation_observed = omega_rad_rev / (2 * math.pi)  # 7.999e-08
# T_D the period for each new precession
T_phi = (2 * math.pi) / (1 - D_perturbation_observed)
omega_approximated = (24 * math.pi ** 3 * r_a ** 2) / (c ** 2 * T ** 2 * (1 - E ** 2))
omega = (2 * math.pi) * (1 / (1 - D_perturbation_equation) - 1)
# D the perturbation parameter error
D_perturbation_error = abs(D_perturbation_equation - D_perturbation_observed) / D_perturbation_observed  # 1.391e-03
# When d = 0
r_a_calculated = r_perihelion/(1-E)
r_aphelion_calculated = r_a * (1 + E)
print(Td, T, '{:.3e}'.format(T), '{:.3e}'.format(r_a))
print('{:.3e}'.format(alpha_bulk), '{:.3e}'.format(alpha_orbital))
print('{:.3e}'.format(np.arccos((1 / E) * ((alpha_bulk / r_perihelion) - 1))))  # 1.601e-02
error_a = (r_a_calculated-r_a)/r_a
print(r_a, r_a_calculated, '{:.3e}'.format(error_a))
# 57909000000.0 57907574500.83262
error_aphelion = (r_aphelion_calculated-r_aphelion)/r_aphelion
print(r_aphelion, r_aphelion_calculated, '{:.3e}'.format(error_aphelion))
# 69818000000.0 69816867627.21
print('{:.3e}'.format(omega_sec_century), '{:.3e}'.format(omega_rad_rev))
print('D from Binet eq: {:.3e}'.format(D_perturbation_equation))
print('D from observation: {:.3e}'.format(D_perturbation_observed))
print('{:.3e}'.format(D_perturbation_error))
omega_vulcan = (6 * math.pi * G * M) / (r_a * c ** 2 * (1 - E ** 2))  # 5.018896261130917e-07
# rad/rev this is the precession of 43"/C
D_perturbation_vulcan = omega_vulcan / (2 * math.pi)
T_D_Vulcan = 2 * math.pi / (1 - D_perturbation_vulcan)  # For new perihelion
phi_pi4_Vulcan = (math.pi / 4) * (math.floor((2 * math.pi) / omega_vulcan))
print('Phi por each pi/4 precession {:.3e}'.format(phi_pi4_precession))  # 9.818e+06
print(f'Phi por each pi/4 precession: {phi_pi4_precession}')  # 9818307.273084803
# phi_pi4_precession_right = math.floor(phi_pi4_precession / math.pi)
# print(f'Phi por each pi/4 precession: {phi_pi4_precession_right * math.pi}')
revolution_auxiliary = math.floor(2 * math.pi / omega_approximated)
phi_pi_4_observed = (math.pi / 4) * math.floor(2 * math.pi / omega_rad_rev)
phi_pi_4_relativistic_approximated = (math.pi / 4) * math.floor(2 * math.pi / omega_approximated)
print('Relativistic phi_pi_4 {:.3e}'.format(phi_pi_4_relativistic_approximated))  # 9.833e+06
print('Vulcan phi_pi_4 {:.3e}'.format(phi_pi4_Vulcan))  # 9.832e+06
print('Observed phi_pi_4 {:.3e}'.format(phi_pi_4_observed))  # 9.818e+06
www = (6 * math.pi * G * M)/(T * (1 - E ** 2) * r_a * c ** 2)
print('{:3e}'.format(www))
print('Precesión de Vulcan {:3e}'.format(omega_vulcan))  # 5.018896e-07
print('Precesión Relativista aproximada {:3e}'.format(omega_approximated))  # 5.018663e-07
print('Precesión Relativista {:3e}'.format(omega))  # 5.018663e-07
print('Precesión Observada {:3e}'.format(omega_rad_rev))  # 5.018663e-07
Precession_error_Vulcan = abs(omega_vulcan - omega_rad_rev) / omega_rad_rev
Precession_error_Relativistic = abs(omega_approximated - omega_rad_rev) / omega_rad_rev
Precession_comparison = abs(omega_vulcan - omega_approximated) / omega_approximated
print('Error relativo de Vulcan {:3e}'.format(Precession_error_Vulcan))  # 5.018663e-07
print('Error relativo relativista {:3e}'.format(Precession_error_Relativistic))  # 5.018663e-07
print('Comparación relativa entre precesiones {:3e}'.format(Precession_comparison))  # 5.018663e-07
