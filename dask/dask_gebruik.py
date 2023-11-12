#%%  Vanaf:  https://www.youtube.com/watch?v=EybGGLbLipI
# Volledige DASK tutoriaal

%%time 
from time import sleep
from dask import delayed

#%%

def inc(x):
    sleep(1)
    return x + 1

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

# Parallel met DASK:
x = delayed(inc)(1)
y = delayed(inc)(2)
z = delayed(add)(x, y)

#%%
%%time
# Nou voer dit uit met compute:
 
# voer uit
z.compute()

#%%
z
z.visualize()
# %%
data = [1, 2, 3, 4, 5, 6, 7, 8]

#%% Sekwensieel (stadig sonder DASK)
%%time 

results = []

for x in data:
    y = inc(x)
    results.append(y)

total = sum(results)
print('Resultaat stadig', total)

# %%

#%% with DASK
%%time 

results = []

for x in data:
    y = delayed(inc)(x)
    results.append(y)

total = delayed(sum)(results)
print('voor computing', total)
result = total.compute()
print("Na computing : ", result)

total.visualize()

# %%
