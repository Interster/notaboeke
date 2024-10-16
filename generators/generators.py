#%%
# https://realpython.com/lessons/understanding-generators/

import sys
import cProfile

#%%
def oneindige_reeks():
    num = 0
    while True:
        yield num
        num += 1

        yield "Volgende yield statement"

#%%
oneindig = oneindige_reeks()

#%%

next(oneindig)
# %%

def eindige_reeks():
    nums = [1, 2, 3]
    for num in nums:
        yield num

#%%        
eindig = eindige_reeks()

#%%
next(eindig)        
# %%
# Met 'n lys in generator sintaks

nommers_kwadraat_lys = [nom**2 for nom in range(5)]
nommers_kwadraat_generator = (nom**2 for nom in range(5))

#%%
next(nommers_kwadraat_generator)
# %%
# Spoed en grootte van skikking vs. generator
nom_kwad_lys = [nom**2 for nom in range(100000)]
nom_kwad_generator = (nom**2 for nom in range(100000))

sys.getsizeof(nom_kwad_lys)
sys.getsizeof(nom_kwad_generator)

cProfile.run('sum([i*2 for i in range(100000)])')
cProfile.run('sum((i*2 for i in range(100000)))')

# %%
