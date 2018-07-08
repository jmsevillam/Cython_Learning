from integration import integrate_f
import sys

xini=float(sys.argv[1])
xfin=float(sys.argv[2])
Ni=int(sys.argv[3])
integrate_f(xini,xfin,Ni)
