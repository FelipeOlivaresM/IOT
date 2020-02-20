import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import pdb
import matplotlib.gridspec as gs
import math

file='Datos.xlsx'
excel=pd.read_excel(file,sheet_name=0)
excel2=pd.read_excel(file,sheet_name=0)


#Grafico de barras
ins=excel['Instrumento']
pia=ins[ins.str.match('Piano')].count()
gui=ins[ins.str.match('Guitarra')].count()
bat=ins[ins.str.match('Bateria')].count()

x=['Piano','Guitarra','Bateria']
y=[pia,gui,bat]
plt.figure(figsize=(13,7))
plt.bar(x,y,color='darkcyan')
plt.title('Clases',fontsize=18)
plt.xlabel('Estudiantes',fontsize='16')
plt.ylabel('Instrumento',fontsize='16')
plt.grid()
plt.savefig('Barras.jpg')


#Grafico circular
colors=['darkcyan','salmon','sandybrown']
plt.figure(figsize=(13,7))
plt.pie(y,labels=x,colors=colors,autopct='%1.0f%%')
plt.title('Clases',fontsize=18)
plt.savefig('Pie.jpg')


#Histrograma
nota=excel['Nota Final']
plt.figure(figsize=(13,7))
plt.grid()
plt.hist(nota,5,edgecolor='grey',color='sandybrown')
plt.title('Notas Finales',fontsize=18)
plt.xlabel('Nota Final',fontsize=16)
plt.ylabel('#Estudiantes',fontsize=16)
plt.savefig('Histrograma.jpg')


#Lineas
c1=excel['Nota primer corte']
c2=excel['Nota segundo corte']
c3=excel['Nota tercer corte']
#--promedios---Primer semestre
ac1=c1.mean()
ac2=c2.mean()
ac3=c3.mean()

x2=['Primero','Segundo','Tercero']
y2=[ac1,ac2,ac3]
plt.figure(figsize=(13,7))
plt.plot(x2,y2,color='darkcyan',linewidth=2,linestyle='-.')
plt.title('Comportamiento notas',fontsize=18)
plt.xlabel('Promedio del curso',fontsize='16')
plt.ylabel('Corte',fontsize='16')
plt.ylim(0,5)
plt.grid()
plt.savefig('Linea.jpg')


#Areas
plt.figure(figsize=(13,7))
plt.fill_between(x2,y2,color='darkcyan')
plt.title('Comportamiento notas',fontsize=18)
plt.xlabel('Promedio del curso',fontsize='16')
plt.ylabel('Corte',fontsize='16')
plt.ylim(0,5)
plt.grid()
plt.savefig('Areas.jpg')


#Matriz de graficas
gs1=gs.GridSpec(nrows=1,ncols=2)
gs1.update(hspace=0.1)
plt.figure(figsize=(13,7))
ax1=plt.subplot(gs1[0,0])
ax1.plot(x2,y2,color='darkcyan',linewidth=2,linestyle='-.')
ax2=plt.subplot(gs1[0,1])
ax2.fill_between(x2,y2,color='darkcyan')
plt.suptitle('Comportamiento notas',fontsize=18)
plt.savefig('GridSpec.jpg')
plt.show()

#Funciones

def f1(x):
	return x

def f2(x):
	return(x**2)
x=np.arange(-5,5,0.1)
plt.plot(x,[f1(i) for i in x])
plt.plot(x,[f2(i) for i in x])
plt.grid()
plt.show()

