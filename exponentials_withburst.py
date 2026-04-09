import numpy as np
import matplotlib.pyplot as plt

def exponential_decay(x, e_folding):
    return np.exp(-x / e_folding)

# Input values for the x-axis
x_values = np.arange(0, 3000, step=1)  # You can adjust the range based on your preference

old_e_folding = 1000
# E-folding values for the exponential decay
burst_fracs = [0.1]
burst_ages = [100, 500, 1000]
burst_taus = [20000]

# Plotting the curves for each e-folding value
for frac in burst_fracs:
    for age in burst_ages:
        for tau in burst_taus:
            
            y_values = exponential_decay(x_values, old_e_folding)
            
            x_dummy = np.arange(0, age, step=1)
            y_dummy = exponential_decay(x_dummy, tau)
            
            k = frac / (1. - frac)
            k = k * np.sum(y_values) / np.sum(y_dummy)
            
            y_values[3000-age:3000] += (k * y_dummy)
            y_values /= np.sum(y_values)
            
            plt.plot(x_values, y_values, label=r'$\tau$ = {}'.format(tau))

# Adding labels and legend
plt.xlabel('Age of Universe [Myr]', fontsize=12)
plt.ylabel('Log Normalized SFR', fontsize=12)
#plt.title('Exponential Declining Function with Different E-folding Values', fontsize=24)
#plt.legend(fontsize=12)

# Adding major and minor ticks on each axis
plt.tick_params(axis='both', which='major', labelsize=12, length=8, direction='in')
plt.tick_params(axis='both', which='minor', labelsize=12, length=4, direction='in')
plt.minorticks_on()

# Set minor tick frequency to half the major tick frequency
#plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(base=(x_values[-1] - x_values[0]) / 20))
#plt.gca().yaxis.set_minor_locator(plt.MultipleLocator(base=0.1))

# Display the plot
plt.grid(True)
plt.savefig('single_tau_SFHs_withbursts_example.pdf', dpi=500, format='pdf', bbox_inches='tight')