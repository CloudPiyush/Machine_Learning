'''Base- Examample of Hierarchical Clustering Using Dendogram.'''

# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.cluster.hierarchy import dendrogram,linkage

# X = [4,5,10,4,3,11,14,6,10,12]
# Y = [21,19,24,17,16,25,24,22,21,21]

# Data = list(zip(X,Y))
# linkage_Data = linkage(Data,method='ward',metric='euclidean')
# dendrogram(linkage_Data)
# plt.show()

'''Hierarchical_Clustering using Skleran'''

# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.cluster import AgglomerativeClustering

# X = np.array([4,5,10,4,3,11,14,6,10,12])
# Y = np.array([21,19,24,17,16,25,24,22,21,21])

# Data = list(zip(X,Y))

# Hierarchical_Cluster = AgglomerativeClustering(n_clusters=2,affinity='euclidean',linkage='ward')
# Labels = Hierarchical_Cluster.fit_predict(Data)

# plt.scatter(X,Y,c=Labels)
# plt.show()

'''-------------'''

import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram,linkage
import numpy as np
from sklearn.cluster import AgglomerativeClustering
X = np.array([4,5,10,4,3,11,14,6,10,12])
Y = np.array([21,19,24,17,16,25,24,22,21,21])

Data = list(zip(X,Y))

Model = AgglomerativeClustering(n_clusters=2,linkage='ward',affinity='euclidean')
label = Model.fit_predict(Data)

plt.scatter(X,Y,c=label)
# linkage_Data = linkage(Data,method='ward',metric='euclidean')
# dendrogram(linkage_Data)
plt.show()