import matplotlib.pyplot as plt
import numpy as np
import sqlite3


x = np.linspace(-10,10,100)

plt.plot(x,np.sin(x),'r-')
plt.plot(x,np.cos(x),'g-')
plt.title('Plot of Sin(x) and Cos(x) functions')
plt.xlabel('Values in radian')
plt.ylabel('values of functions')
plt.show()

