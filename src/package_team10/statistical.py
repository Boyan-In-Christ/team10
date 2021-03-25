#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn
import os

import constants

# reading of the data files
def read_in_df(filedir, filename):
    '''This reads in a file or dataframe in csv.format with pandas'''
    name = '{}{}'.format(filedir, filename)
    print('Reading from file {} - pandas'.format(name))
    data = pd.read_csv(name, r'\s+')
    return data

def read_in_np(filedir, filename):
    '''This reads in a file in text format with numpy'''
    name = '{}{}'.format(filedir,filename)
    print('Reading from file {} - numpy'.format(name))
    data = np.loadtxt(name,skiprows=1)
    data = data.T
    return data

def workfiles(filenames):
    '''Define filenumbers to be able to perform the pipeline for every file'''
    for fileindex in range(len(filenames)):
        print 'Current file:', filenames[fileindex];
        df_file = read_in_df(filedir,filenames[fileindex]);
        plot_data(df_file)
    return df_file.head()

# read and plot expec.t
def plot_data(df_file):
    sn.relplot(data=df_file, kind='line')
plt.show()

# give information on the data set expec.t
df_file.info()

# show statistical properties of the data set expec.t
df_file.describe()
return


# discard columns <x> and <y> and define as new file df_expec_new
df_expec_new = df_expec.drop(columns = ['<x>', '<y>'])
df_expec_new.head(10)

# eliminate columns based on the variance: if the variance of the values
# in a column is below a given threshold, that column is discarded

#column variance of the data set
df_expec_new.var(axis = 0)

# define variance filter
threshv = 1.0e-5

# apply variance filter on data
df_expec_sorted_var = df_expec_new.drop(df_expec_new.var()[df_expec_new.var() < threshv].index.values, axis=1)
print(df_expec_sorted_var)

# create plot for filtered data with z for y axis
plot_expec_sorted_var_z = sn.relplot(data=df_expec_sorted_var, kind='line', x='time', y='<z>')
plt.show()

# save plot as .pdf
plot_expec_sorted_var_z.savefig('/home/anja/team10/team10/data/plots/plot_expec_sorted_var_z.pdf')
