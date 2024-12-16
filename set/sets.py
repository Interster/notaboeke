#%%
# https://realpython.com/python-set-comprehension/
# Set comprehension in Python

# Definieer die versameling
colors = {"blue", "red", "green", "orange", "green"}

print(colors)

# Add a color
colors.add("purple")
print(colors)
#%%

# You can also create a new set using the set() constructor and an iterable of objects:
numbers = [2, 2, 1, 4, 2, 3]
set(numbers)
# %%

# Leë versameling
print(set())
# %%
uniekewoorde = set()

teks = """
Vuurbees

Die buffel ken geen metafisika:
hy soek die soetgras
en die kuil,
hy sal die kalf karnuffel,
horings in sy vyand gra,
die koei besnuffel,
teen hael gaan skuil,
maar geen vrae oor môre vra - 
die buffel ken geen metafisika.

Alleen die mens
tref in sy swerwe
tussen hede, toekoms en verlede
die spleet tot grotte
van die rede:
hy maak 'n mes,
'n vuur,
skep gode,
dink aan sterf,
prewel gebede
en moet beswerend teen 'n muur
van sy spelonk die buffel verf:

die buffel van die metafisika:
die vuurbees in homself
volg, buig of bars,
enduit sy drif en drome na,
en prikkels van die brein
word piramides, Laaste Avondmaal,
wiel, chroom,
projektiele, produkte van atoom,
et cetera.

En voor sy besete blik
besef die enkeling
onsteld
hy sal ook nie terugskrik
vir die alles-uitwissende slagveld - 
stukkend lê alreeds
die Parthenon en Hirosjima
in die bose skoonheid van geweld.
Die buffel ken geen metafisika.""".lower()

for woord in teks.split():
    uniekewoorde.add(woord)

print(uniekewoorde)

#%%

matrix = [
    [9, 3, 8, 3],
    [4, 5, 2, 8],
    [6, 4, 3, 1],
    [1, 0, 4, 5],
    ]

{value**2 for row in matrix for value in row}
{64, 1, 0, 4, 36, 9, 16, 81, 25}
# %%
# Filter eposse

emails_set = {
    "alice@example.org",
    "bob@example.com",
    "johndoe@example.com",
    "charlie@example.com",
    "david@example.net",
}

{email for email in emails_set if email.endswith(".com")}

# %%
