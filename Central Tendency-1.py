import numpy as np
from scipy import stats 

# speed = [45,35,78,65,45,24,22,35,78,69,79,67,69]

# New = np.mean(speed)
# print(New)

# speed = [45,35,78,65,45,24,22,35,78,69,79,67,69]

# New  = np.median(speed)
# print(New)

# speed = [45,35,78,65,45,24,22,35,78,69,79,67,69]

# New  = stats.mode(speed)
# print(New)

speed = [32,111,56,76,78,87,65,35,56,46,35,34,24,65]

Varience = np.var(speed)
Deviation = np.std(speed)

print('\nThe Varience of Speed is :{0}'.format(Varience))
print('\nThe Standard Deviation of Speed is :{0}'.format(Deviation))

