#%%
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
%%time 

results = []

for x in data:
    y = delayed.(inc)(x)
    results.append(y)

total = delayed(sum)(results)
print('Before computing', total)
result = total.compute()
print("After computing : ", result)