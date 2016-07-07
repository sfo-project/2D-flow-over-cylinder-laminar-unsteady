import numpy as np
import matplotlib.pyplot as plt

data_Re100 = np.genfromtxt('data/forceCoeffs_Re100.txt', delimiter='\t')

# print(Re_100)
# print(Re_100.shape)
# print(Re_100[35000:, [2]])
# print(Re_100[71000:, [2]].mean(axis=0))

#Calculat & plot Drag Coefficient

def cal_plot_coeffs(coeff_column):
    print(data_Re100[30000:, [coeff_column]].mean(axis=0))

    plt.ylim(-2, 2)
    plt.plot(data_Re100[:, [0]], data_Re100[:, [coeff_column]])
    plt.show()

cal_plot_coeffs(2)
cal_plot_coeffs(3)

# t_cl = Re_100[:, [3]]
# print(t_cl)

# rfft2 = np.fft.rfft2(t_cl)
# print(rfft2.max(axis=0))

# plt.plot(rfft2)
# plt.ylim(-100, 100)
# plt.show()

# Plot Cd vs time
# Find Cd mean
# Plot Cl vs time
# Find Cl mean
