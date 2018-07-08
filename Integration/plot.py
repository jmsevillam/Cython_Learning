import numpy as np
import matplotlib.pylab as plt

data1=np.genfromtxt('int.dat')
data2=np.genfromtxt('test.dat')

x1=data1[:,0]
y1=data1[:,1]
x2=data2[:,0]
y2=data2[:,1]

fig=plt.figure(figsize=(5,3))
plt.subplots_adjust(right=.98,top=0.93,left=0.11,bottom=0.15)
ax=fig.add_subplot(111)
ax.set_xlabel('Intervals [#]')
ax.set_ylabel('Time [s]')
ax.plot(x1,y1,'.-',label='Python')
ax.plot(x2,y2,'.-',label='Cython')
ax.legend()
plt.savefig('time.pdf')
plt.close()
