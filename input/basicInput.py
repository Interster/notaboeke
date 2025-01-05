#%% Basic input
# https://realpython.com/python-input-output/

naam = input('Sleutel jou naam in')

print(f"{'Jou naam is '}{naam}")

#%%

nommer = input('Sleutel asseblief ''n nommer in ')

print(f"{'Die nommer is '}{nommer}{' en die tipe is '}{type(nommer)}")

print(f"{'Verander dit nou na '}{type(int(nommer))}{' en tel 100 by om '}{str(int(nommer) + 100)}{' te kry'}")

#%%
