# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 11:11:32 2017

@author: lindseykitchell
"""

import pandas as pd
import numpy as np
from scipy.stats.stats import pearsonr
import matplotlib.pylab as plt
import glob
import os

pwd = os.getcwd()

df_dict = {}
subj_list = []
for file in glob.glob(pwd + "/*spectrum.json"):
    subj_name = os.path.basename(file)[0:6]
    subj_list.append(subj_name)
    df_dict[os.path.basename(file)[0:6]] = pd.read_json(file)
 
all_tracts = list(df_dict[subj_list[0]])[:-1] 
 
    
    
fig = plt.figure(figsize=(18,18))
all_corrs = []
fig_num = 1
for tract in all_tracts:
    corr = np.zeros([len(subj_list), len(subj_list)])
    for num in range(len(subj_list)):
        for num2 in range(len(subj_list)):
            corrval, pval = pearsonr(df_dict[subj_list[num]][tract], df_dict[subj_list[num2]][tract])
            corr[num, num2] = corrval
    all_corrs.append(corr)
    ax = fig.add_subplot(5,4,fig_num)
    ax.set_aspect('equal')
    ax.set_title(tract)
    im = ax.imshow(corr, interpolation='nearest', vmin=0, vmax=1, cmap=plt.cm.viridis, aspect='equal')
    #ocean hot     
    fig_num += 1
cax = fig.add_axes([0.9, 0.1, 0.03, 0.8])
plt.colorbar(im, cax)
plt.savefig('alltractcorrelations.png', bbox_inches='tight')
plt.show()