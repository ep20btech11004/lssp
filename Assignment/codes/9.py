import matplotlib.pyplot as plt
x = [0.00, 0.05, 0.10, 0.15, 0.20, 0.25]
y = [0.000, 0.006, 0.011, 0.018, 0.025, 0.039]
  
plt.plot(x, y)

plt.xlabel('Load, m(kg)')
plt.ylabel('Corresponding Elevation, l(cm)')
  
plt.title('Uniform Bending')
  
plt.show()