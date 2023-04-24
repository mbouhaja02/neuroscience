# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 10:52:34 2022

@author: Amelie_Aussel
"""

import matplotlib.pyplot as plt
import scipy.io
import numpy as np
from mpl_toolkits import mplot3d


def plot_connection_matrix_3d(matrix,positions):
    rows, cols = np.where(matrix > 0)
    print("Nombre d'aretes : "+str(len(rows.tolist())))
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    for k in range(len(rows.tolist())) :
        x,y=rows[k],cols[k]
        ax.plot3D([positions[x,0],positions[y,0]],[positions[x,1],positions[y,1]],[positions[x,2],positions[y,2]],'k', zorder=1,lw=matrix[x,y])
    ax.scatter3D(positions[:,0],positions[:,1],positions[:,2], s=40, zorder=2)

def plot_connection_matrix_2d(matrix,positions):
    rows, cols = np.where(matrix > 0)
    print("Nombre d'aretes : "+str(len(rows.tolist())))
    plt.figure()
    for k in range(len(rows.tolist())) :
        x,y=rows[k],cols[k]
        plt.plot([positions[x,0],positions[y,0]],[positions[x,1],positions[y,1]],'k', zorder=1,lw=matrix[x,y])
    plt.scatter(positions[:,0],positions[:,1], s=40, zorder=2)


mat = scipy.io.loadmat('Coactivation_matrix.mat')
Coactivation_matrix=mat['Coactivation_matrix']
Coordinates=mat['Coord']
mat = scipy.io.loadmat('GroupAverage_rsfMRI_matrix.mat')
Coactivation_matrix=mat['GroupAverage_rsfMRI']
Coordinates=mat['Coord']
print('Nombre de sommets total : '+str(Coactivation_matrix.shape[0]))

Nmax=4
Nmax=min(Nmax,Coactivation_matrix.shape[0])
print('Nombre de sommets conserves: '+str(Nmax))
Coactivation_matrix=Coactivation_matrix[:Nmax,:Nmax]
Coordinates=Coordinates[:Nmax,:]
plt.close('all')
plot_connection_matrix_3d(Coactivation_matrix,Coordinates)
plot_connection_matrix_2d(Coactivation_matrix,Coordinates)
print(Coactivation_matrix)
print(len(Coactivation_matrix))
#plt.show()