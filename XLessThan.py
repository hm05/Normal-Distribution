import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Define parameters
mu = float(input("Enter mu :: "))
sigma = float(input("Enter sigma :: "))
n = float(input("Enter n :: "))
sample_mean = float(input("Enter X-bar :: "))

# Calculate standard error
se = sigma / np.sqrt(n)

# Calculate Z-score
z_score = (sample_mean - mu) / se

# Define the range of values for the standard normal distribution
x = np.linspace(-4, 4, 1000)

# Plot the standard normal distribution curve
plt.plot(x, norm.pdf(x), 'b-', label='Standard Normal Distribution')

# Shade the area representing P(Z < z_score)
x_shade = np.linspace(-4, z_score, 100)
plt.fill_between(x_shade, norm.pdf(x_shade), color='orange', alpha=0.5, label='P(X̄ < 960)')

# Add labels and legend
plt.xlabel('Z')
plt.ylabel('Probability Density')
plt.title('Standard Normal Distribution')
plt.legend()

# Show plot
plt.grid(True)
plt.show()
