
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
	N_all = np.genfromtxt(file, delimiter=',')
	print(str(N_all.shape[1]) + ' data series found in the csv file. ')

	# Parameters
	dt = input("dt in m (default: 0.5) =  ")
	if(dt==''):
		dt = 0.5
	else:
		dt = float(dt)

	W = input("W in mm (default: 21) =  ")
	if(W==''):
		W = 21
	else:
		W = float(W)

	L = input("L in m (default: 1) = ")
	if(L==''):
		L = 1
	else:
		L = float(L)

	S = input("S in mm (default: 20) = ")
	if(S==''):
		S = 20
	else:
		S = float(S)

	D = input("D in mm (default: 60) = ")
	if(D==''):
		D = 60
	else:
		D = float(D)

	def computeBothSidedA(N):
		amount = len(N)
		# compute Tiefe
		T = np.linspace(0,amount*dt,amount+1)

		# compute Auslenkung
		Auslenkung = np.zeros(amount+1)
		for i in range(amount):
			Auslenkung[i+1] = Auslenkung[i] + dt*N[i]

		# cubic spline interpolation
		spline = CubicSpline(T,Auslenkung)
		x_large = np.linspace(-0,10,100)
		ay = spline(x_large)

		def beule(x):
			spline(x)-(spline(x))

		def B(x):
			return W-spline(x)+(spline(x-L/2) + spline(x+L/2))/2

		def A(x):
			return B(x)-S/2

		fig = plt.figure()
		


		ax = plt.subplot(211)
		ax.plot(T,Auslenkung,'o',label='Deviation')
		ax.plot(x_large,ay, label='Deviation (interpolated)')
		plt.xlabel('depth (m)')
		plt.ylabel('mm')
		# plt.title('Deviation from vertial line')
		box = ax.get_position()
		ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
		ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), prop={'size':8})
		plt.grid()

		ax = plt.subplot(212)
		ax.plot(x_large,A(x_large), label='A(t) first side')
		ax.plot(x_large,D-A(x_large), label='A(t) second side')
		plt.xlabel('depth (m)')
		plt.ylabel('mm')
		# plt.title('Distance A(t)')
		box = ax.get_position()
		ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
		ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), prop={'size':8})
		plt.grid()

		plotname = file[:-4]+str(counter)+'.pdf'
		print('saving ' + plotname)
		plt.show()
		fig.savefig(plotname)
		print('done.')

	print('computing and writing plots...')
	counter = 1
	for i in range(0,N_all.shape[1]):
		computeBothSidedA(N_all[:,i])
		counter = counter+1

	readAnotherFile = input('Read another csv file? (Yes/No): ').lower() == 'yes'

print('Exiting.')

