#%%
# Meet die geraas op 'n paneel agter in 'n Suzuki Ertiga
# wat begin vibreer by 80kph, maar die ergste vibreer by
# 90kph.
# Die opwekking is van die pad deur die bande, want as dit op growwe teer
# loop teen hierdie spoed vibreer die paneel, maar op baie
# gladde teer is die paneel stil.
# Die motor het 'n R185/65R15 band.  Hierdie band het 'n 
# naaf diameter van 15 duim en 'n band diameter van 24.47 duim.
# Hierdie diameter is 'n band omtrek van 
# 24.47 duim = 621mm -> pi*d = 3.141*621mm = 1950mm
# Indien die ergste opwekking by 90kph is, bereken die
# rotasie frekwensie as volg:
# 90kph = 90000m/3600s = 25m/s
# Rotasie frekwensie is dus:  25m/s/1.95m = 12.8Hz
# Daar is 'n eerste piek by 10 maal hierdie frekwensie
# maar die hoogste piek is by 160Hz.
# Daar kan aangeneem word dat die bande 'n wye geraasvloer
# opwek en dat die paneel se natuurlike frekwensie naby aan
# 160Hz is.
# Indien die motor oor 'n ongelykheid of 'n impak ry,
# dan word die hele spektrum opgewek nes 'n impakhamer.
# Dus werk die padgeraas meer soos 'n wye spektrum opwekking.
# Dit is duidelik dat die opwekking van die enjin geen
# invloed op die paneel het nie.  Dit is net as gevolg van
# pad geruis dat die paneel vibreer.


#%%  Load an oggopus file
# https://pyogg.readthedocs.io/en/latest/examples.html
import pyogg
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Note:  Had to install the PyOgg from the git repository:
# https://github.com/TeamPyOgg/PyOgg/discussions/67
#
# git clone https://github.com/TeamPyOgg/PyOgg.git
# pip install -e PyOgg



#%%

# Specify the filename to read
filename = "ErtigaGeraasPaneel20241216.opus"

# Read the file using OpusFile
print("Reading Ogg Opus file...")
opus_file = pyogg.OpusFile(filename)

# Display summary information about the audio
print("\nRead Ogg Opus file")
print("Channels:\n  ", opus_file.channels)
print("Frequency (samples per second):\n  ",opus_file.frequency)
print("Buffer Length (bytes):\n  ", len(opus_file.buffer))

# Get the data as a NumPy array
buf = opus_file.as_array()

# The shape of the array can be read as
# "(number of samples per channel, number of channels)".
print(
    "Shape of numpy array (number of samples per channel, "+
    "number of channels):\n  ",
    buf.shape
)


#%% Plot die kanaal
# Die opus leer se frekwensie is 48000Hz of 48kHz.
# Maak nou 'n tydvektor daarvoor

sein = buf[0:-1,0]
seinlengte = len(sein)
frekwensie = opus_file.frequency
tydvektor = np.linspace(0, seinlengte/frekwensie, seinlengte)

plt.plot(tydvektor, sein)
plt.ylabel('Klansein in 16bis heelgetalle')
plt.xlabel('Tyd [s]')
plt.show()

# %%
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.periodogram.html

# Create periodogram
fs = frekwensie # [Hz]
f, Pxx_den = signal.periodogram(sein, fs)
plt.semilogy(f, Pxx_den)

plt.ylim([1e-1, 1e7])
plt.xlim([1e-7, 1000])

plt.xlabel('frequency [Hz]')

plt.ylabel('PSD [(deg/s)**2/Hz]')

plt.show()
# %%
# Vergroot rondom 160Hz om piek duidelik te wys
plt.semilogy(f, Pxx_den)

plt.ylim([1e-1, 1e7])
plt.xlim([1e-7, 180])

plt.xlabel('frequency [Hz]')

plt.ylabel('PSD [(deg/s)**2/Hz]')

plt.show()
# %%
