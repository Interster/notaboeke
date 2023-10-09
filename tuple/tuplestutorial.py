#%%
# https://realpython.com/python-tuple/

#%%
# Voorbeeld van kleur wat as tuple gestoor word:
red = (255, 0, 0)

#%%
record = ("John", 35, "Python Developer")

print(record[0])
print(record[2])
# %%
jane = ("Jane Doe", 25, 1.75, "Canada")
point = (2, 7)
pen = (2, "Solid", True)

days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)
# %%
# Leë tuple
empty = ()
empty


type(empty)