import numpy as np

a = np.array([ 

	[-0.55, 0.45, 0.1],
	[0.45, -0.9,0.1],
	[1,1,1]

	])

b = np.array(
	[0,0,1]
	)

x = np.linalg.solve(a,b)
print(x)
