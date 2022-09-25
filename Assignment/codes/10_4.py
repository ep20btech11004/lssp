import matplotlib.pyplot as plt

n = [1, 2, 3, 4, 5]
Ry2 = [0.0016, 0.0058, 0.01, 0.0137, 0.0179]
  
plt.plot(n, Ry2)

plt.xlabel('Order of the Rings')
plt.ylabel('Diametre^2')
  
plt.title('300gm transverse') 
  
plt.show()
