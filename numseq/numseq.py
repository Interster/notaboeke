#%%
import numpy as np

sequence = np.array([0, 8, 3, -1, 5, 6, 7, 8, 1, 2, 0])
sequencediff = np.diff(sequence)

#%%
vind = False
langeinde = 0
eindetemp = 0
lengtetemp = 0
langstery = 0

posisie = np.where(sequencediff == 1)
posisiediff = np.diff(posisie[0][:])

for plek in posisiediff:
    
    if plek == 1:
       lengtetemp += 1
       eindetemp += 1

    if lengtetemp > langstery:
       langstery = lengtetemp
       langeinde = eindetemp

    if plek != 1:
       lengtetemp = 0
       eindetemp = 0
       
print('Die langste reeks is ' + str(langstery + 2) + ' syfers lank')

indeksvanlangreeks = posisie[0][langeinde - langstery : langeinde + 1]
indeksvanlangreeks = np.append(indeksvanlangreeks, [indeksvanlangreeks[-1] + 1])
print ('Die reeks is: ' + str(sequence[indeksvanlangreeks]))

#%%
# Ontfoutingsdata
print(sequence)
print(sequencediff)
print(posisie[0][:])
print(posisiediff)

# %%
