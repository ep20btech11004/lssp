import matplotlib.pyplot as plt

n = [1, 2, 3, 4, 5]
Rx2 = [0.0016, 0.0036, 0.0066, 0.0094, 0.01277]
  
plt.plot(n, Rx2)

plt.xlabel('Order of the Rings')
plt.ylabel('Diametre^2')
  
plt.title('300gm longitudinal') 
  
plt.show()
