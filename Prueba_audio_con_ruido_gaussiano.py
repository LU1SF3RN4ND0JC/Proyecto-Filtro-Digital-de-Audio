import sounddevice as sd
from scipy.io.wavfile import write
from matplotlib import pyplot as plt
from playsound import playsound
import numpy as np
# Sampling frequency
freq = 44100
# Recording duration: 4 segundos
duration = 4
# Start recorder with the given values of
# duration and sample frequency
print('Iniciando grabacion')
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
ruido_gaussiano = np.random.normal(0, 0.00001, recording.shape)
recording_gaussiano = recording+ruido_gaussiano
# Record audio for the given number of seconds
sd.wait()
print('fin')
print(recording)

fig, ax = plt.subplots(2, 1, figsize=(10, 8))

ax[0].plot(recording)
ax[0].set_title('graf Recording')

ax[1].plot(recording_gaussiano)
ax[1].set_title('graf Gaussiano')

ax[0].set_xlabel('Eje X')
ax[0].set_ylabel('Eje Y')
ax[1].set_xlabel('Eje X')
ax[1].set_ylabel('Eje Y')
plt.tight_layout()
plt.show()
# This will convert the NumPy array to an audio
# file with the given sampling frequency
write("recording1.wav", freq, recording)
sd.default.samplerate = freq
print("Playing audio")
sd.play(recording_gaussiano)
sd.wait()
