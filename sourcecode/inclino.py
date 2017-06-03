
'''
	Inclino v0.5
	Written by Luca Naterop
	Zürich, 2017
	Questions, suggestions and comments to luca@naterop.net
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

print('Inclino version 0.5 started. ')

readAnotherFile = True
while readAnotherFile:

	# ask for csv file
	file = input("enter name of csv file: ")

	# get Neigung
	M = np.genfromtxt(file, delimiter=',')
	Tiefe = M[:,0]
	Neigung = M[:,1]

	# Parameters
	W = input("W in mm (default: 21) =  ")
	if(W==''):
		W = 21
	else:
		W = float(W)

	D = input("D in mm (default: 60) = ")
	if(D==''):
		D = 60
	else:
		D = float(D)

	def computeBothSidedA(T_Neigung, Neigung):
		Neigung = Neigung*10
		amount = len(T_Neigung)
		L = (T_Neigung[1]-T_Neigung[0])

		# compute t_a (= Tiefe zu jedem Wert der Auslenkung, siehe Evernote-Notiz inclino)
		t_a = np.zeros(amount+1)
		for i in range(1,amount+1):
			t_a[i] = L/2 + (i-1)*L

		# compute a (= Auslenkung zu jeder Tiefe, siehe Evernote Notiz)
		a = np.zeros(amount+1)
		a[1] = L/2*Neigung[0]
		for i in range(2,amount+1):
			a[i] = a[i-1] + L/2*(Neigung[i-2] + Neigung[i-1])

		# cubic spline interpolation
		spline = CubicSpline(t_a,a)
		x_large1 = np.linspace(0,T_Neigung[-1],100)
		x_large2 = np.linspace(L/2,T_Neigung[-1]-L/2,100)

		def A(x):
			return W+spline(x)-(spline(x-L/2) + spline(x+L/2))/2

		fig = plt.figure()
		

		ax = plt.subplot(121)
		ax.plot(a, -t_a, 'o',label='Deviation')
		ax.plot(spline(x_large1),-x_large1, label='Deviation (interpolated)')
		plt.ylabel('depth (m)')
		plt.xlabel('mm')
		plt.title('Deviation from vertial line')
		box = ax.get_position()
		ax.set_position([box.x0, box.y0, box.width * 0.9, box.height])
		# ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), prop={'size':8})
		plt.grid()

		ax = plt.subplot(122)
		ax.plot(A(x_large2), -x_large2, label='A(t) first side')
		ax.plot(D-A(x_large2), -x_large2, label='A(t) second side')
		plt.ylabel('depth (m)')
		plt.xlabel('mm')
		plt.title('Distance A(t)')
		axes = plt.gca()
		axes.set_xlim([0,60])
		box = ax.get_position()
		ax.set_position([box.x0, box.y0, box.width * 0.9, box.height])
		# ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), prop={'size':8})
		plt.grid()

		plotname = file[:-4]+'.pdf'
		print('saving ' + plotname)
		plt.show()
		fig.savefig(plotname)
		print('done.')

	print('computing and writing plots...')

	computeBothSidedA(Tiefe, Neigung)

	readAnotherFile = input('Read another csv file? (Yes/No): ').lower() == 'yes'

print('Exiting.')

