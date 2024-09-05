import matplotlib.pyplot as plt
import numpy as np
x=np.array(['walking','cycle','bus','car','train'])
y=np.array([10,23,40,12,8])
plt.bar(x,y,width=1)
plt.xlabel("mode of transportation")
plt.ylabel("Students number")
plt.show()
