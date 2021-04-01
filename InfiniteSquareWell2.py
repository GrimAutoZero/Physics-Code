import numpy as np
import math as m 
import matplotlib.pyplot as plt
from scipy.sparse import diags

'''
Defines some constants
'''

hbar = 1.05E-34
mass = 9.11E-31
L = 1

'''
Sets up grid as well as defines constants
'''

numpoints = 10
spacegrid = np.linspace(0,L,numpoints+1)
dx = spacegrid[1] - spacegrid[0]
const = -((hbar)**2)/(2*mass*dx**2)

'''
Potential function
'''
def U(x):
    return 0
'''
Sets up hamiltonian
'''
listofones = [np.ones(numpoints).tolist()]
listoftwos =[(-2*np.ones(numpoints+1)).tolist()]

H1 = diags(listofones, [1]).toarray()
H2 = diags(listofones, [-1]).toarray()
H3 = diags(listoftwos, [0]).toarray()
H = H1+H2+H3

for i in [0,numpoints]:
    H[:,i] = 0

w,v = np.linalg.eigh(H)
print(w)
plt.plot(spacegrid,(v[:,0])/np.sqrt(dx))
plt.show()

plt.plot(spacegrid,(v[:,0]/np.sqrt(dx)**2))
plt.show()