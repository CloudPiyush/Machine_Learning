# import numpy as np
# import matplotlib.pyplot as plt

# x = np.random.uniform(10,20,150)
# print(x)

# font1 = {'family':'century','size':20,'color':'red'}
# font2 = {'family':'impact','size':20,'color':'red'}
# plt.hist(x,color='yellow')
# plt.xlabel('X-Axis',fontdict=font1)
# plt.ylabel('Y-Axis',fontdict=font2)
# plt.title('Data Distribution',size=23,family='Algerian')
# plt.show()

"""Normal Data Distribution using Histogram"""

import numpy as np
import matplotlib.pyplot as plt

X = np.random.normal(5.0,1.0,1000)

font1 = {'family':'corbel','size':15,'color':'green'}
font2 = {'family':'gadugi','size':12,'color':'blue'}

plt.hist(X,100,color='hotpink',histtype='stepfilled')
plt.xlabel('Values',fontdict=font1)
plt.ylabel('Specified Value',fontdict=font2)
plt.title('Normal Data Distribution.',family='impact',size=28,color='red')
plt.show()

"""Normal Data Distribution using Scatter plot"""

# import numpy as np
# import matplotlib.pyplot as plt

# x = np.random.normal(5,3,120)
# y = np.random.normal(4,5,120)
# color = np.random.randint(1,100,120)
# size = 5 * np.random.randint(1,20,120)

# font1 = {'family':'corbel','size':15,'color':'green'}
# font2 = {'family':'gadugi','size':12,'color':'blue'}

# plt.scatter(x,y,c=color,cmap='flag',alpha=0.6,s=size)
# plt.xlabel('Standard Deviation',fontdict=font1)
# plt.ylabel('Mean Value',fontdict=font2)
# plt.title('Normal Data Distribution using Scatter',family='Algerian',color='red',size=20)
# plt.show()