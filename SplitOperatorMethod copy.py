import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft,ifft
from matplotlib import animation

N = 3000
t = np.linspace(0,0.6,N)
x = np.linspace(-10,10,N)
p = np.linspace(-10,10,N)
dx = x[1] -x[0]
dt = t[1] -t[0]
b = 1
p_0 = 40
m = 1

def psi(x):
    return np.array(np.sqrt(2*b)/np.sqrt(np.sqrt(2*np.pi)) * np.exp(1j*p_0*x)* np.exp(-(x)**2 *b**2),'complex')


def V(x):
    vvals = []
    for i in x:
        if i ==3:
            vvals.append(6000)
        else:
            vvals.append(0)
    return np.array(vvals)

psimatrix = np.zeros((3000,3000),'complex')
psimatrix[0,:] = psi(x)

for i in np.arange(0,2999):


    step1 = np.exp(-1j*V(x)*dt) * (dt/2) * psimatrix[i,:]
    step2 = fft(step1)
    step3 = ((p**2)/(2*m))*step2*dt
    step4 = ifft(step3)
    Finalstep = np.exp(-1j*V(x)*dt) * (dt/2) * step4

    psimatrix[i+1,:] = Finalstep


print(psimatrix)


