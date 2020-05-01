#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
from IPython.display import display
import scipy as sp
from datetime import datetime 
from scipy.optimize import minimize
from datetime import date
from scipy.signal import savgol_filter


# In[2]:


import wget
import os
from pathlib import Path


# In[3]:


def read_dataset():
    file="d:/1/corona/corona2.csv"
    file_path=Path(file)
    if not file_path.is_file():
        wget.download("https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv", 
              file)
    ds = pd.read_csv('D:/1/corona/corona2.csv',sep=",")
    return ds


# In[4]:


def resLogistic1(coefficents, DAYS, F):
    A0 = coefficents[0]
    A1 = coefficents[1]
    A2 = coefficents[2]

    T = A0 / (1 + np.exp(A1 * (DAYS - A2)))
    
    return np.sum((T - F) ** 2)


# In[5]:


def resLogistic2(coefficents, DAYS, F):
    A0 = coefficents[0]
    A1 = coefficents[1]
    A2 = coefficents[2]

    B0 = coefficents[3]
    B1 = coefficents[4]
    B2 = coefficents[5]

    A = A0 / (1 + np.exp(A1 * (DAYS - A2)))
    B = B0 / (1 + np.exp(B1 * (DAYS - B2)))
    T = A + B
    
    return np.sum((T - F) ** 2)


# In[6]:


def resLogistic3(coefficents, DAYS, F):
    A0 = coefficents[0]
    A1 = coefficents[1]
    A2 = coefficents[2]

    B0 = coefficents[3]
    B1 = coefficents[4]
    B2 = coefficents[5]

    C0 = coefficents[6]
    C1 = coefficents[7]
    C2 = coefficents[8]

    A = A0 / (1 + np.exp(A1 * (DAYS - A2)))
    B = B0 / (1 + np.exp(B1 * (DAYS - B2)))
    C = C0 / (1 + np.exp(C1 * (DAYS - C2)))
    T = A + B + C
    
    return np.sum((T - F) ** 2)


# In[7]:


def filter(ds, region, province):
    if ''!=province:
        series=ds.loc[(region == ds["Country/Region"]) & (province == ds["Province/State"])]
    else:
        series=ds.loc[(region == ds["Country/Region"]) & (ds["Province/State"].isnull())]
    return series


# In[8]:


def process(ds, region, province, humps=1, method="Powell"):
    series=filter(ds, region, province)
    D=series["Date"]
    F=series["Deaths"].values
    C=series["Confirmed"].values
    dF = F[1:] - F[:-1]
    dFmax=max(dF)
    dFmed=np.median(dF)
    dC = C[1:] - C[:-1]
    dCmax=max(dC)
    dCmed=np.median(dC)
    
    dFsmooth = savgol_filter(dF, 7, 1) # window size polynomial order
    series["Deaths"]
    
    scale=round(dCmax/dFmax, 2)
    dCscaled=dC/scale
    D1=pd.to_datetime(D).values
    DAYS=(D1-np.datetime64("2020-01-01"))/np.timedelta64(1, 'D')
    X_long = np.arange(20, 200)
    time_long = pd.date_range('2020-01-20', periods=180)
    
    opt = {'maxiter': 100000, 'disp': True}
    
    bnds1 = ((0.0, None), (0.0, None), (0.0, None))
    bnds2 = ((0.0, None), (None, 0.0), (0.0, None), (0.0, None), (None, 0.0), (0.0, None))
    bnds3 = ((0.0, 1.0e+4), (-1.0e+4, 0.0), (0.0, 1.0e+4), (0.0, 1.0e+4), (-1.0e+4, 0.0), (0.0, 1.0e+4), (0.0, 1.0e+4), (-1.0e+4, 0.0), (0.0, 1.0e+4))
    
    ## default:
    #method="Powell"
    
    #method="TNC"
    #method="TNC"
    #method="Nelder-Mead"
    #method="BFGS"
    #method="trust-constr"
    A0=np.max(F)
    print(A0)
    guess1=[A0, -.1, 90]
    guess2=[A0, -.1, 90, A0, -.1, 90]
    guess3=[A0, -.1, 90, A0, -.1, 90, A0, -.1, 90]
    if 1==humps:
        minim=minimize(resLogistic1, guess1, args = (DAYS, F), bounds=bnds1, method = method, options=opt)
    elif 2==humps:
        minim=minimize(resLogistic2, guess2, args = (DAYS, F), bounds=bnds2, method = method, options=opt)
    elif 3==humps:
        minim=minimize(resLogistic3, guess3, args = (DAYS, F), bounds=bnds3, method = method, options=opt)
    else:
        raise ValueError("Wrong number of humps")
    #print(minim)
    if not minim.success:
        raise ValueError("Logit failed")
    
    if 1==humps:
        TT = minim.x[0] / (1 + np.exp(minim.x[1] * (X_long - minim.x[2])))
    elif 2==humps:
        T2_1=minim.x[0] / (1 + np.exp(minim.x[1] * (X_long - minim.x[2]))) 
        T2_2=minim.x[3] / (1 + np.exp(minim.x[4] * (X_long - minim.x[5])))
        TT = T2_1 + T2_2
    elif 3==humps:
        T3_1 = minim.x[0] / (1 + np.exp(minim.x[1] * (X_long - minim.x[2]))) 
        T3_2 = minim.x[3] / (1 + np.exp(minim.x[4] * (X_long - minim.x[5]))) 
        T3_3 = minim.x[6] / (1 + np.exp(minim.x[7] * (X_long - minim.x[8])))
        TT = T3_1 +  T3_2 +  T3_3
    else:
        raise ValueError("Wrong number of humps")

    plt.figure(figsize = (10,5))
    plt.grid()
    plt.title('Number of daily deaths in: ' + region + " " + province, Size=20);
    plt.plot(DAYS[1:], dF, 'r', Marker='o', label='Daily deaths')
    #plt.plot(DAYS[1:], dCscaled, 'y', Marker='o', label="Daily Infected; scale factor:" + str(scale))
    plt.plot(DAYS[1:], dFsmooth, 'k', label="Daily deaths smooth")
    plt.xticks(X_long[1:120][::3], time_long.date[1:120][::3], rotation='90');
    if 2==humps:
        plt.plot(X_long[1:120], T2_1[1:120] - T2_1[:119], 'c', label='Forecast Hump 1')
        plt.plot(X_long[1:120], T2_2[1:120] - T2_2[:119], 'm', label='Forecast Hump 2')
    elif 3==humps:
        plt.plot(X_long[1:120], T3_1[1:120] - T3_1[:119], 'c', label='Forecast Hump 1')
        plt.plot(X_long[1:120], T3_2[1:120] - T3_2[:119], 'm', label='Forecast Hump 2')
        plt.plot(X_long[1:120], T3_3[1:120] - T3_3[:119], 'g', label='Forecast Hump 3')
    plt.plot(X_long[1:120], TT[1:120] - TT[:119], 'b', label='Forecast')
    plt.legend()
    
    dFCST=TT[1:120] - TT[:119]
    
    plt.figure(figsize = (10,2))
    plt.grid()
    plt.title("Residuals", Size=20);
    plt.plot(DAYS[1:], dF-dFCST[0:len(dF)], 'r', Marker='o')
    plt.legend()


# In[9]:


dataset_file="d:/1/corona/corona2.csv"

ds = read_dataset()
#ds["Country/Region"].unique()


# In[10]:


process(ds, "Canada", "Ontario")


# In[11]:


process(ds, "Canada", "Quebec", 1)


# In[12]:


process(ds, "Italy", "", 2, "trust-constr")


# In[13]:


process(ds, "Italy", "")


# In[14]:


process(ds, "Spain", "", 2, "trust-constr")


# In[15]:


process(ds, "Spain", "")


# In[16]:


process(ds, "Portugal", "", 2, "trust-constr")


# In[17]:


process(ds, "Austria", "", 3, "trust-constr")


# In[18]:


process(ds, "Sweden", "", 2, "trust-constr")


# In[19]:


process(ds, "Norway", "", 1)


# In[20]:


process(ds, "Denmark", "", 2, "trust-constr")


# In[21]:


process(ds, "France", "", 2, "trust-constr")


# In[22]:


process(ds, "Germany", "", 1)


# In[44]:


process(ds, "Israel", "", 2, "trust-constr")


# In[41]:


#process(ds, "United Kingdom", "", 2, "trust-constr")
process(ds, "United Kingdom", "")


# In[25]:


process(ds, "Switzerland", "", 2, "trust-constr")


# In[26]:


process(ds, "Netherlands", "", 2, "trust-constr")


# In[46]:


process(ds, "Belgium", "", 2, "trust-constr")


# In[28]:


#process(ds, "Iran", "", 3, "trust-constr")
process(ds, "Iran", "")


# In[29]:


process(ds, "Iran", "", 2, "trust-constr")


# In[30]:


process(ds, "Iran", "")


# In[31]:


process(ds, "Ireland", "", 1)


# In[47]:


process(ds, "Turkey", "", 2, "trust-constr")


# In[33]:


process(ds, "Brazil", "", 1)


# In[34]:


process(ds, "Russia", "")


# In[35]:


process(ds, "India", "", 1)


# In[36]:


process(ds, "Taiwan*", "")


# In[37]:


process(ds, "Korea, South", "", 2)


# In[38]:


process(ds, "Japan", "", 1)


# In[39]:


process(ds, "New Zealand", "")


# In[ ]:




