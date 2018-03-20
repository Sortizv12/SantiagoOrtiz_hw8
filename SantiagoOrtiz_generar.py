import numpy as np
#Funcion ue genera y retorna N numeros aleatorios
#de lista dada
def sample_1(N):
	probabilidades=np.array([0.1,0.4,0.2,0.3])
	elementos=np.array([-10,-5,3,9])
	numeros=np.random.choice(a=elementos,size=N,p=probabilidades)
	return numeros
#Funcion que genera y retorna numeros aleatorios
#de distribucion exponencial
def sample_2(N):
	numeros=np.random.exponential(0.5, N)
#Funcion que halla M numero de promedios
def get_mean(sampling_fun,N,M):
	means=[]
	for i in range(M):
		means.append(np.mean(sampling_fun(N)))
	return np.array(means)
Ns=[10,100,1000]

for i in range(len(Ns)):
	np.savetxt("sample_1_"+str(Ns[i])+".txt",get_mean(sample_1,Ns[i],10000))
	np.savetxt("sample_2_"+str(Ns[i])+".txt",get_mean(sample_1,Ns[i],10000))




