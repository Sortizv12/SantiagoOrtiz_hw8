import numpy as np
import matplotlib.pyplot as plt




def normal_dist(x,mean,sigma):
	x=(x-np.mean(x))+mean
	x=(x/np.std(x))*sigma
	return x

def get_fit(filename):
	datos=np.loadtxt(filename)
	freq,bins=np.histogram(datos, normed=True)
	y=freq
	x=0.5*(bins[:-1]+bins[1:])
	plt.hist(datos)
	plt.savefig(filename[:-4]+".pdf")
	plt.close()

lista_nombres=["sample_1_10.txt","sample_1_100.txt","sample_1_1000.txt","sample_2_10.txt","sample_2_10.txt","sample_2_10.txt"]

for i in range(len(lista_nombres)):
	get_fit(lista_nombres[i])
