import math
import scipy
import sympy as sym
from sympy import *
# from sympy.solvers import solve
import scipy.constants as constant
import numpy as np
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
alpha_orbital = (r_a * (1 - E**2))  # alpha is half latus rectum  5.546e+10
# D perturbation parameter from precession observed value
D_perturbation_observed = omega_rad_rev / (2 * math.pi)  # 7.999e-08
# T_D the period for each new precession
T_phi = (2 * math.pi) / (1 - D_perturbation_observed)   # T_phi = T_phi_0 + omega
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
r_a_calculated = r_perihelion/(1-E)
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
print(f'El error relativo en omega Vulcan es: {Error_omega_Vulcan }, aproximando: '
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
print(f'Vulcan :{floor_revolution_Vulcan}, Approximated: {floor_revolution_approximated}, Observed: {floor_revolution_observed}')
print('Los ángulos phi_pi_4 son:')
print(f'Vulcan :{phi_pi4_Vulcan}, Approximated: {phi_pi_4_relativistic_approximated}, Observed: {phi_pi_4_observed}')
print(f' La cercanía entre omega_vulcan - omega_approximated ={omega_vulcan-omega_approximated} porque son iguales XD')

# This is the formula used, but for the calculation I have to be careful!
TT = 2 * math.pi * math.sqrt(r_a**3/(G * M))  # 7.6003e+06
TT_d = TT / (3600 * 24 * 365.25)
print('{:.10g}'.format(TT_d))  # 0.2408394979 (con G dada),  0.2408404 con G scipy
print('{:.5g}'.format(TT))  # 7.6003e+06

a_finite = 0
u_a_finite = 1 / r_perihelion
b_finite = T_phi
u_b_finite = 1 / r_perihelion

N_finite = int(input('Por favor ingrese el número de pasos N\n'))

Delta = (b_finite - a_finite) / N_finite
# A = N((2 - Delta ** 2), 4)
# B = N(((3 * G * M * Delta ** 2) / c ** 2), 4)
# C = N((1 / alpha_bulk) * Delta ** 2, 4)
A = - 3 * G * M / (c ** 2)
B = Delta ** 2 - 2
C = 1
D = N((-G * M * Delta / h ** 2), 4)
print(A, B, C)
# A_prime = N(math.sqrt(A), 4)
# B_prime = 1
# C_prime = N(math.sqrt(A) * (C - (B ** 2)/(4 * A)), 4)
x = sym.Symbol('x')
x_prime = sym.Symbol('x')
# U = [None] * N_finite
# U.append(N(u_a_finite, 4))
# U.append(x_prime)
# U.append(N(A_prime * x_prime ** 2 + u_a_finite + C_prime, 4))
# u = [u_a_finite, x_prime, A_prime * x_prime + u_a_finite + C_prime]
# # u[0] = u_a_finite
u_x = x_prime
A_prime = 2
C_prime = 1
theta_finite_1 = N(a_finite + Delta, 4)
r_finite_1 = N(alpha_bulk / (1 + E * math.cos(theta_finite_1)), 4)
print(theta_finite_1, r_finite_1)
print(U)
# This creates the equation to be soled numerically, comes from the Finite difference, but nonlinear
# for i in range(3, N_finite + 1):
#     x_prime = N(A_prime * x_prime ** 2 + u_a_finite + C_prime, 4)
#     theta_finite = N(a_finite + i * Delta, 4)
#     U.append(sym.expand(x_prime))
    # u[i] = A_prime * u[i - 1] + u[i - 2] + C_prime
    # print(i, theta_finite, x_prime, U[i])
    # print(i, u[i])
# U[N_finite] =  u_b_finite
# For Newton method to find the root:

# Derivative_prime = N(diff(U[10], x), 4)
# N(Derivative_prime.evalf(subs={x: theta_finite_1}), 4)
# print(f'\n\n{N(Derivative_prime.evalf(subs={x: theta_finite_1}), 4)}')
# print(f'\n\n{N(Derivative_prime.evalf(theta_finite_1), 4)}')
# print(f'\n\n\n{(U[3]).evalf(subs={x:5})}')
# equation_to_solve = U[7]-1
# solution = solve(equation_to_solve, x)
# print(solution)
# subs={a:6, b:5, c:2}
theta_finite = N(a_finite, 4)
r_finite = N(alpha_bulk / (1 + E * math.cos(theta_finite)), 4)
diff_r_finite = N(diff(r_finite, x), 4)
u_zero = sym.Symbol('u')
g_zero = N((2 * A * u_zero + B / 2), 4)
# CREATING J MATRIX
J = np.zeros((N_finite + 1, N_finite + 1))
U_finite = np.zeros(N_finite + 1)
F_finite = np.zeros((0, N_finite + 1))
u_finite_zero_vector = np.zeros(N_finite + 1)
phi_finite_vector = np.zeros(N_finite + 1)
#U_zeros
for i in range(N_finite + 1):
    phi_finite = i * Delta
    phi_finite_vector[i] = phi_finite
    u_finite_zero = (1 + E * np.cos(phi_finite))
    u_finite_zero_vector[i] = u_finite_zero
print(phi_finite_vector, u_finite_zero_vector)
print(U_finite)
# Construction F(x)
F_finite[0][0] = u_finite_zero_vector[0]
F_finite[0][N_finite] = u_finite_zero_vector[N_finite+1]
for i in range(1, N_finite):
    F_finite[0][i] = u_finite_zero_vector[i+1] + A * (u_finite_zero_vector[i] + B / (2 * A)) ** 2 + \
                     u_finite_zero_vector[i-1] + D - (B ** 2) / (4 * A)
print(F_finite)
for j in range(N_finite + 1):
    J[0][0] = 1
    J[N_finite][N_finite] = 1
    for i in range(1, N_finite):
        if i == j+1 or i == j-1:
            J[i][j] = 1
        elif i == j:
            J[i][j] = (2 * A) * u_finite_zero_vector[i] + B / 2
print(J)
# for i in range(N_iterations):
#     theta_finite = theta_finite + i * Delta -
#u_zero.evalf(subs={u: 0.1})
# def function(varible):
#     f_variable = (1 + E * math.cos(variable)) / alpha_bulk
# u.append(A * u[i] + B * u[i] ** 2 + C - u[i - 1])
# u = []
# u.append(u_a_finite)
# # u[0] = u_a_finite
# u.append(A * u[1] + B * u[1] ** 2 + C - u[0])
# for i in range(1, N_finite):
#     print(i)
#     # u.append(A * u[i] + B * u[i] ** 2 + C - u[i-1])
# u.append(u_b_finite)
# print(u)
