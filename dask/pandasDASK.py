#%%  Vanaf:  https://www.youtube.com/watch?v=EybGGLbLipI
# Volledige DASK tutoriaal


from time import sleep
from dask import delayed
from dask import compute
import pandas as pd


# %% Sekwensiele pandas
%%time 
verkope = pd.read_csv("kardata.csv")
verkope.head()
# %%
%%time 
verkope.groupby("Brand").mean()

#%% DASK pandas
%%time 
verkope = delayed(pd.read_csv)("kardata.csv")

#%%
verkope.head()
# %%
%%time 
gemiddeld = verkope.groupby("Brand").mean()
# %%
%%time 
compute(gemiddeld)
# %%
gemiddeld.visualize()
# %%
