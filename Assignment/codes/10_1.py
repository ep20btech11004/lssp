import matplotlib.pyplot as plt

n = [1, 2, 3, 4, 5]
Rx1 = [0.0009, 0.0032, 0.0064, 0.0090, 0.0121]
  
plt.plot(n, Rx1)

plt.xlabel('Order of the Rings')
plt.ylabel('Diametre^2')
  
plt.title('250gm longitudinal') 
  
plt.show()
