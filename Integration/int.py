import sys

def f(x):
	return x ** 2 - x
def integrate_f(a,b,N):
	s=0
	dx=(b-a)/N
	for i in range(N):
		s += f(a + i * dx)
	return s * dx

xini=float(sys.argv[1])
xfin=float(sys.argv[2])
Ni=int(sys.argv[3])
integrate_f(xini,xfin,Ni)
