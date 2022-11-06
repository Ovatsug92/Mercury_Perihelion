import math
import scipy
import sympy as sym
from sympy import *
# from sympy.solvers import solve
import scipy.constants as constant
import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
from numpy import linalg

U = []


def relative_error(variable, real_value):
    error_relative = abs((variable - real_value) / variable)
    error_relative_significant = float('%.4g' % error_relative)
    return error_relative_significant


def relative_error_no_significant(variable, real_value):
    error_relative = abs((variable - real_value) / variable)
    return error_relative


# Main quantities
# Constants (is G a natural or physical constant?)
# Because the least significant figures is 4 for eccentricity, that is used
G = scipy.constants.G  # 6.6743e-11 está mejor
c = scipy.constants.c
print(G, c)
# G = 6.67435 * (10 ** (-11))  # m**3 kg−1 s**−2 with a relative uncertainty of 19 ppm.
# c = 299792458  # m/s
# Data Sun
M = 1988500 * (10 ** 24)  # kg 6 significant figures
# Data Mercury Bulk
m = 0.330103 * (10 ** 24)  # kg 4 significant figures
uncertainty_m = 0.000021 * (10 ** 24)
# Data Mercury Orbital
Td = 87.969  # days 5 significant figures Sidereal orbit period
r_a = 57.909 * (10 ** 9)  # meters  semi-major axis  5 significant figures
# E = 0.20563069  # Eccentricity
E = 0.2056  # Eccentricity 4 significant figures
omega_sec_century = 43  # Precession arc-sec/century
r_perihelion = 46.000 * (10 ** 9)  # meters perihelion 5 significant figures
# Auxiliary quantities
# Data Sun bulk
R_vol_M = 695700 * 10 ** 3  # Volumetric mean radius (km)	695,700.    0.006*10**10
# Data Mercury bulk
R_vol_m = 2439.4 * 10 ** 3  # Volumetric mean radius (km)	2439.7      0.00024*10**10
uncertainty_R_vol_m = 0.1 * 10 ** 3
# Data Mercury orbital
r_aphelion = 69.818 * (10 ** 9)  # meters (10**6 km) aphelion

# Calculated quantities
# Main calculated quantities
T = Td * 24 * 3600  # seconds 7600521.6  760.052 10**4 7.601e+06 s
omega_rad_rev = omega_sec_century * ((88 * 2 * math.pi) / (3600 * 360 * 100 * 365))  # 5.026e-07 rad/rev
alpha_orbital = (r_a * (1 - E ** 2))  # alpha is half latus rectum  5.546e+10
# D perturbation parameter from precession observed value
D_perturbation_observed = omega_rad_rev / (2 * math.pi)  # 7.999e-08
# T_D the period for each new precession
T_phi = (2 * math.pi) / (1 - D_perturbation_observed)  # T_phi = T_phi_0 + omega
# T_phi_0 = 2 * math.pi

# Auxiliary calculated quantities
# For alpha
rb = r_a * (1 - E ** 2) ** (1 / 2)  # semiminor
A = math.pi * (r_a * rb)  # Area
h = (2 * A) / T  # angular momemtum per unit mass
alpha_bulk = (h ** 2 / (G * M))  # 5.546e+10 All previous was used for calculate this
Error_alpha = relative_error(alpha_bulk, alpha_orbital)

# D the perturbation parameter from Binet equation
D_perturbation_equation = (3 * G ** 2 * M ** 2) / (h ** 2 * c ** 2)  # 7.988e-08
Error_D = relative_error(D_perturbation_equation, D_perturbation_observed)
omega_approximated = (24 * math.pi ** 3 * r_a ** 2) / (c ** 2 * T ** 2 * (1 - E ** 2))
omega = (2 * math.pi) * (1 / (1 - D_perturbation_equation) - 1)
omega_vulcan = (6 * math.pi * G * M) / (r_a * c ** 2 * (1 - E ** 2))  # 5.018896261130917e-07
Error_omega_approximated = relative_error(omega_approximated, omega_rad_rev)
Error_omega = relative_error(omega, omega_rad_rev)
Omega_comparison = relative_error(omega, omega_approximated)
Error_omega_Vulcan = relative_error(omega_vulcan, omega_rad_rev)
# D the perturbation parameter from Vulcan
D_perturbation_vulcan = omega_vulcan / (2 * math.pi)
Error_D_vulcan = relative_error(D_perturbation_vulcan, D_perturbation_observed)
T_D_Vulcan = 2 * math.pi / (1 - D_perturbation_vulcan)
Error_T_D_Vulcan = relative_error(T_D_Vulcan, T_phi)

# Radii
r_a_calculated = r_perihelion / (1 - E)
r_aphelion_calculated = r_a * (1 + E)
Error_r_a = relative_error(r_a_calculated, r_a)
Error_aphelion = relative_error(r_aphelion_calculated, r_aphelion)

# x = float('%.4g' % Error_D)
# print('{:.3e}'.format(x))
# Print
# Just "Aproximando and porcentual are of interest"
print(f'El error relativo en delta (D) es: {Error_D}, aproximando: ' '{:.3e}'.format(Error_D),
      'porcentual: {:.4g}%'.format(Error_D * 100, '.4g'))
print(f'El error relativo en delta (D) vulcam  es: {Error_D_vulcan}, aproximando: '
      '{:.3e}'.format(Error_D_vulcan), 'porcentual: {:.3e}%'.format(Error_D_vulcan * 100))
print(f'El error relativo en omega app  es: {Error_omega_approximated}, aproximando: '
      '{:.3e}'.format(Error_omega_approximated), 'porcentual: {:.3e}%'.format(Error_omega_approximated * 100))
print(f'El error relativo en omega  es: {Error_omega}, aproximando: '
      '{:.3e}'.format(Error_omega), 'porcentual: {:.3e}%'.format(Error_omega * 100))
print(f'El error relativo en omega Vulcan es: {Error_omega_Vulcan}, aproximando: '
      '{:.3e}'.format(Error_omega_Vulcan), 'porcentual: {:.3e}%'.format(Error_omega_Vulcan * 100))
print(f'La comparación entre omega y omega app  es: {Omega_comparison}, aproximando: '
      '{:.3e}'.format(Omega_comparison), 'porcentual: {:.3e}%'.format(Omega_comparison * 100))
print(f'El error relativo en el afelio  es: {Error_aphelion}, aproximando: '
      '{:.3e}'.format(Error_aphelion), 'porcentual: {:.3e}%'.format(Error_aphelion * 100))
print(f'El error relativo en r_a es: {Error_r_a}, aproximando: '
      '{:.3e}'.format(Error_r_a), 'porcentual: {:.3e}%'.format(Error_r_a * 100))
print(f'El error relativo en la mitad del lado recto  es: {Error_alpha}, aproximando: '
      '{:.3e}'.format(Error_alpha), 'porcentual: {:.3e}%'.format(Error_alpha * 100))
print(f'La comparación entre los periodos angulares de Vulcan y relativista  es: {Error_T_D_Vulcan}, '
      f'aproximando: '
      '{:.3e}'.format(Error_T_D_Vulcan), 'porcentual: {:.3e}%'.format(Error_T_D_Vulcan * 100))

# For the pi_4 angles
revolution_Vulcan = (2 * math.pi) / omega_vulcan
floor_revolution_Vulcan = math.floor((2 * math.pi) / omega_vulcan)
phi_pi4_Vulcan = (math.pi / 4) * floor_revolution_Vulcan
revolution_observed = 2 * math.pi / omega_rad_rev
floor_revolution_observed = math.floor(2 * math.pi / omega_rad_rev)
phi_pi_4_observed = (math.pi / 4) * floor_revolution_observed
revolution_approximated = 2 * math.pi / omega_approximated
floor_revolution_approximated = math.floor(2 * math.pi / omega_approximated)
phi_pi_4_relativistic_approximated = (math.pi / 4) * floor_revolution_approximated

print('Las revoluciones son:')
print(f'Vulcan :{revolution_Vulcan}, Approximated: {revolution_approximated}, Observed: {revolution_observed}')
print('Los auxiliares son:')
print(
    f'Vulcan :{floor_revolution_Vulcan}, Approximated: {floor_revolution_approximated}, Observed: {floor_revolution_observed}')
print('Los ángulos phi_pi_4 son:')
print(f'Vulcan :{phi_pi4_Vulcan}, Approximated: {phi_pi_4_relativistic_approximated}, Observed: {phi_pi_4_observed}')
print(
    f' La cercanía entre omega_vulcan - omega_approximated ={omega_vulcan - omega_approximated} porque son iguales XD')

# This is the formula used, but for the calculation I have to be careful!
TT = 2 * math.pi * math.sqrt(r_a ** 3 / (G * M))  # 7.6003e+06
TT_d = TT / (3600 * 24 * 365.25)
print('{:.10g}'.format(TT_d))  # 0.2408394979 (con G dada),  0.2408404 con G scipy
print('{:.5g}'.format(TT))  # 7.6003e+06
print(phi_pi_4_relativistic_approximated / T_phi)
# Boundary conditions
a_finite = phi_pi_4_observed
u_a_finite = 1 / r_perihelion
b_finite = phi_pi_4_observed + T_phi
u_b_finite = 1 / r_perihelion
# Asks for the number of steps
N_finite = int(input('Por favor ingrese el número de pasos N\n'))
# Asks for number of iterations
N_iterations = int(input('Por favor ingrese el número de iteraciones i\n'))
# Asks for tolerance
Tolerance = float(input('Por favor ingrese la tolerancia en decimales i\n'))
Delta = (b_finite - a_finite) / (N_finite + 1)  # Step size
A = (- 3 * G * M * Delta ** 2) / (c ** 2)
B = (Delta ** 2 - 2)
C = 1
D = (-G * M * Delta ** 2) / (h ** 2)
print('\nLas constantes de las funciones f_i son:')
print(f'A = {A}')
print(f'B = {B}')
print(f'C = {C}')
print(f'D = {D}')
# Creating vector for solution u
U_finite = np.zeros(N_finite + 1)
# Creating phi_i vector
phi_finite_vector = np.zeros(N_finite + 1)
# Creating initial solution u_zero
u_finite_zero_vector = np.zeros(N_finite + 1)
for i in range(N_finite + 1):
    phi_finite = a_finite + i * Delta
    phi_finite_vector[i] = phi_finite
    u_finite_zero = (1 + E * np.cos(phi_finite * (1 - D_perturbation_observed))) / alpha_bulk
    # u_finite_zero = (1 + E * np.cos(phi_finite)) / alpha_bulk
    u_finite_zero_vector[i] = u_finite_zero
    U_finite[i] = u_finite_zero_vector[i]
# for i in range(N_finite + 1):
    # print(i, N(phi_finite_vector[i], 4), N(u_finite_zero_vector[i], 4))
# CREATING J MATRIX
J = np.zeros((N_finite + 1, N_finite + 1))
# for j in range(N_finite + 1):
#     J[0][0] = 1
#     J[N_finite][N_finite] = 1
#     for i in range(1, N_finite):
#         if i == j + 1 or i == j - 1:
#             J[i][j] = 1
#         elif i == j:
#             J[i][j] = (2 * A) * u_finite_zero_vector[i] + B / 2
# print(J)
# Creating F column
F_finite = np.zeros(N_finite + 1)
# Construction F(x)
F_finite[0] = U_finite[0]
F_finite[N_finite] = U_finite[N_finite]
for i in range(1, N_finite-1):
    F_finite[i] = u_finite_zero_vector[i + 1] + A * (u_finite_zero_vector[i] + B / (2 * A)) ** 2 + \
                  u_finite_zero_vector[i - 1] + D - (B ** 2) / (4 * A)
#  F_finite_T_list = []
# for i in range(N_finite + 1):
#     F_finite_T_list.append([F_finite[i]])
# F_finite_T = np.array(F_finite_T_list)
# print(F_finite)
# print(F_finite_T)
# y = inv(J).dot(F_finite_T)
# y_T = inv(J).dot(F_finite_T)
# y_matmul = np.matmul(inv(J), F_finite)
# print(f'La primera solución es: y = {y}')
# print(f'La primera solución es: y_T = {y_T}')
# print(f'La primera solución es: y_T = {y_matmul}')
# phi_finite = 0
k = 1
while k <= N_iterations:
    for j in range(N_finite + 1):
        J[0][0] = 1
        J[N_finite][N_finite] = 1
        for i in range(1, N_finite):
            if i == j + 1 or i == j - 1:
                J[i][j] = 1
            elif i == j:
                J[i][j] = (2 * A) * U_finite[i] + B
    y = -np.matmul(inv(J), F_finite)
    F_finite[0] = U_finite[0]
    F_finite[N_finite] = U_finite[N_finite]
    for i in range(1, N_finite-1):
        F_finite[i] = U_finite[i + 1] + A * (U_finite[i] + B / (2 * A)) ** 2 + \
                  U_finite[i - 1] + D - (B ** 2) / (4 * A)
    if linalg.norm(y) < Tolerance:
        print('El proceso fue exitoso.')
        break
    else:
        k += 1
        U_finite += y
r_iteration_solution = np.zeros(N_finite + 1)
print(f'\nLa norma del vector solución y es {linalg.norm(y)}\n')
for i in range(N_finite + 1):
    r_iteration_solution[i] = 1 / U_finite[i]
# print(r_iteration_solution)
fig, ax = plt.subplots(figsize=(6, 5))
ax.grid(True)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.ylabel(r"$r$(m)", fontsize=12)
plt.xlabel(r"$\varphi$(rad)", fontsize=12)
ax.set_yticks([4 * (10 ** 10), 4.5 * (10 ** 10), 5 * (10 ** 10), 7 * (10 ** 10)])  # Less radial ticks
ax.plot(phi_finite_vector, r_iteration_solution, 'g.', markersize=4)
# phi_newtonian = np.arange(0, T_phi, 0.1)
r_newtonian = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(phi_finite_vector)))
ax.plot(phi_finite_vector, r_newtonian, 'r.', markersize=3)
# phi_relativistic = np.arange(0, T_phi, 0.1)
r_relativistic = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(phi_finite_vector * (1 - D_perturbation_observed))))
ax.plot(phi_finite_vector, r_relativistic, 'b.', markersize=1)
plt.show()
error_vector = np.zeros(N_finite + 1)
r_relativistic_vector_2 = np.zeros(N_finite + 1)
phi_finite_vector_2 = np.zeros(N_finite + 1)
r_iteration_solution_2 = np.zeros(N_finite + 1)
phi_finite_vector_3 = np.zeros(N_finite + 1 - 90 * math.floor(N_finite/100))
r_relativistic_vector_3 = np.zeros(N_finite + 1 - 90 * math.floor(N_finite/100))
r_iteration_solution_3 = np.zeros(N_finite + 1 - 90 * math.floor(N_finite/100))
plt.close()
for i in range(90 * math.floor(N_finite / 100), N_finite + 1):
    phi_finite_vector_2[i] = a_finite + i * Delta
    r_relativistic_vector_2[i] = (h ** 2 / (G * M)) * \
                                 (1 / (1 + E * np.cos(phi_finite_vector_2[i] * (1 - D_perturbation_observed))))
    #error_vector[i] = abs(r_iteration_solution_2[i]-r_relativistic_vector_2[i]) / r_iteration_solution_2[i]
    print('{} {:.9g} {:.7g} {:.7g}'.format(i, phi_finite_vector_2[i], r_iteration_solution_2[i],
                                              r_relativistic_vector_2[i]))  # , error_vector[i]))
error_vector_3 = np.zeros(N_finite + 1 - 90 * math.floor(N_finite/100))
for i in range(len(phi_finite_vector_3)):
    phi_finite_vector_3[i] = phi_finite_vector_2[i + 90 * math.floor(N_finite / 100)]
    r_relativistic_vector_3[i] = r_relativistic_vector_2[i + 90 * math.floor(N_finite / 100)]
    r_iteration_solution_3[i] = r_iteration_solution[i + 90 * math.floor(N_finite / 100)]
    error_vector_3[i] = abs(r_relativistic_vector_3[i] - r_iteration_solution_3[i]) / r_iteration_solution_3[i]
print(phi_finite_vector_3)
print(r_relativistic_vector_3)
print(r_iteration_solution_3)
fig, ax = plt.subplots(figsize=(6, 5))
ax.grid(True)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.ylabel(r"$r$(m)", fontsize=12)
plt.xlabel(r"$\varphi$(rad)", fontsize=12)
ax.set_yticks([4 * (10 ** 10), 4.5 * (10 ** 10), 5 * (10 ** 10), 7 * (10 ** 10)])  # Less radial ticks
ax.plot(phi_finite_vector_3, r_iteration_solution_3, 'g.', markersize=4)
# phi_newtonian = np.arange(0, T_phi, 0.1)
r_newtonian = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(phi_finite_vector_3)))
# ax.plot(phi_finite_vector_3, r_newtonian, 'r.', markersize=3)
# phi_relativistic = np.arange(0, T_phi, 0.1)
r_relativistic = (h ** 2 / (G * M)) * (1 / (1 + E * np.cos(phi_finite_vector_3 * (1 - D_perturbation_observed))))
ax.plot(phi_finite_vector_3, r_relativistic_vector_3, 'b.', markersize=1)
plt.show()
KKKK = int(input('Escriba 1'))
plt.close()
if KKKK == 1:
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.grid(True)
    plt.xticks(fontsize=11)
    plt.yticks(fontsize=11)
    plt.ylabel(r"$r$(m)", fontsize=12)
    plt.xlabel(r"$\varphi$(rad)", fontsize=12)
    ax.plot(phi_finite_vector_3, error_vector_3, 'b.', markersize=1)
    plt.show()