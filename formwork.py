import numpy as np
from matplotlib import pyplot as plt

# rho = concrete density (kg/m3)
# C1 = size and shape coefficient
# R = vertical pour rate (m/hr)
# C2 = concrete constituent
# T = temperature when concrete discharges (celcius)
# h = height of formwork (m)
# h_disch = discharge height above top of form (m)
# H = discharge height (m)
# K = temperature coefficient
# h2 = max pressure height (m)

def  calculate_pressure(rho, C1, R, C2, T, h, h_disch):
    H = h_disch + h                 # m
    P_max_hydro = rho * h / 100     # kPa
    K = (36 / (T + 16)) ** 2

    # Check if H > sqrt(R)  * C1, this is the case where P_max is not reached
    if (H > np.sqrt(R) * C1):
        P_max = rho/100 * (C1 * np.sqrt(R) + C2 *K * np.sqrt(H - C1 * np.sqrt(R)))  # kPa
    else:
        P_max = P_max_hydro  # kPa
        
    h2 = P_max / P_max_hydro * h  # m

    plt.plot ([0, P_max, P_max], [h, h - h2, 0])
    plt.xlabel ("Pressure (kPa)")
    plt.ylabel("Height of Form (m)")
    plt.title("Lateral Concrete Pressure On Form")
    plt.xlim(xmin = 0)
    plt.ylim(ymin = 0)
    plt.show()

calculate_pressure(2600, 1, 0.4, 0.3, 16, 1.7, 0.2)