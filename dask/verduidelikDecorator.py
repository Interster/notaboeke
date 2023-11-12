#%%  Vanaf:  https://www.youtube.com/watch?v=EybGGLbLipI
# Volledige DASK tutoriaal


from time import sleep
from dask import delayed

#%%
@delayed
def inc(x):
    sleep(1)
    return x + 1

@delayed
def add(x, y):
    sleep(1)
    return x + y

#%%
%%time 

# Sekwensiele operasie:
x = inc(1)
y = inc(2)
z = add(x, y)


#%%
%%time
# Nou voer dit uit met compute:
 
# voer uit
z.compute()

#%%
z
z.visualize()

# %%
