#%%

# https://towardsdatascience.com/create-stunning-radar-plots-with-matplotlib-6a8e05054ff9


#%%
import matplotlib.pyplot as plt
import numpy as np

#%%
lithologies = ['Shale', 'Sandstone', 
               'Limestone', 'Dolomite', 
               'Anhydrite', 'Coal', 'Tuff']

well1 = [47, 35, 10, 1, 0, 2, 5]

well2 = [7, 10, 51, 22, 10, 0, 0]

#%%

lithologies = [*lithologies, lithologies[0]]
well1 = [*well1, well1[0]]
well2 = [*well2, well2[0]]

#%%
well2

#%%
label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(lithologies))

#%%
fig, ax = plt.subplots(figsize=(10,10), subplot_kw=dict(polar=True))

ax.plot(label_loc, well1, lw=2)
ax.plot(label_loc, well2, lw=2)

lines, labels = plt.thetagrids(np.degrees(label_loc), labels=lithologies)

plt.show()

#%%
from matplotlib.patches import Patch

fig, ax = plt.subplots(figsize=(10,10), subplot_kw=dict(polar=True))

ax.plot(label_loc, well1, lw=2)
ax.plot(label_loc, well2, lw=2)

ax.fill(label_loc, well1, alpha=0.3)
ax.fill(label_loc, well2, alpha=0.3)

lines, labels = plt.thetagrids(np.degrees(label_loc), labels=lithologies)

# Create custom legend handles
well1_legend = Patch(facecolor='C0', alpha=0.5, label='Well 1')
well2_legend = Patch(facecolor='C1', alpha=0.5, label='Well 2')

# Add a legend with custom position and handles
ax.legend(handles=[well1_legend, well2_legend], 
          bbox_to_anchor=(1.3, 0.2), fontsize=20, 
          frameon=True)

plt.show()

#%%
fig, ax = plt.subplots(figsize=(10,10), subplot_kw=dict(polar=True))

ax.plot(label_loc, well1, lw=2)
ax.plot(label_loc, well2, lw=2)

ax.fill(label_loc, well1, alpha=0.3)
ax.fill(label_loc, well2, alpha=0.3)

lines, labels = plt.thetagrids(np.degrees(label_loc), labels=lithologies)

ax.tick_params(axis='both', which='major', pad=30, labelsize=15)

# Create custom legend handles
well1_legend = Patch(facecolor='C0', alpha=0.5, label='Well 1')
well2_legend = Patch(facecolor='C1', alpha=0.5, label='Well 2')

# Add a legend with custom position and handles
ax.legend(handles=[well1_legend, well2_legend], 
          bbox_to_anchor=(1.3, 0.2), fontsize=20, 
          frameon=True)


plt.show()
# %%
