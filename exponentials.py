import numpy as np
import matplotlib.pyplot as plt

def exponential_decay(x, e_folding):
    return np.exp(-x / e_folding)

# Input values for the x-axis
x_values = np.linspace(0, 3000, 1000)  # You can adjust the range based on your preference

# E-folding values for the exponential decay
e_folding_values = [200, 500, 1000, 5000, 20000]

# Plotting the curves for each e-folding value
for e_folding in e_folding_values:
    y_values = exponential_decay(x_values, e_folding)
    y_values /= np.max(y_values)
    plt.plot(x_values, y_values, label=r'$\tau$ = {}'.format(e_folding))

# Adding labels and legend
plt.xlabel('Age of Universe [Myr]', fontsize=12)
plt.ylabel('Log Normalized SFR', fontsize=12)
#plt.title('Exponential Declining Function with Different E-folding Values', fontsize=24)
plt.legend(fontsize=12)

# Adding major and minor ticks on each axis
plt.tick_params(axis='both', which='major', labelsize=12, length=8, direction='in')
plt.tick_params(axis='both', which='minor', labelsize=12, length=4, direction='in')
plt.minorticks_on()

# Set minor tick frequency to half the major tick frequency
#plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(base=(x_values[-1] - x_values[0]) / 20))
#plt.gca().yaxis.set_minor_locator(plt.MultipleLocator(base=0.1))

# Display the plot
plt.grid(True)
plt.savefig('single_tau_SFHs_example.pdf', dpi=500, format='pdf')