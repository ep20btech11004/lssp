import matplotlib.pyplot as plt

n = [1, 2, 3, 4, 5]
Ry1 = [0.0013, 0.0049, 0.0088, 0.0128, 0.0166]
  
plt.plot(n, Ry1)

plt.xlabel('Order of the Rings')
plt.ylabel('Diametre^2')
  
plt.title('250gm transverse') 
  
plt.show()
