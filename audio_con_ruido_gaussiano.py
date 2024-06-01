import sounddevice as sd
from scipy.io.wavfile import write
from matplotlib import pyplot as plt
from playsound import playsound
import numpy as np
# Sampling frequency
freq = 44100
# Recording duration: 4 segundos
duration = 10
# Start recorder with the given values of
# duration and sample frequency
print('Iniciando grabacion')
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
# Record audio for the given number of seconds
sd.wait()
print('fin')
print(recording)
# Normalizar para rango (-1,1)
recording = recording / np.max(np.abs(recording))
nvlr = 0.01  # Nivel de ruido
ruido_gaussiano = np.random.normal(0, nvlr, recording.shape)
recording_gaussiano = recording+ruido_gaussiano
recording_gaussiano = recording / \
    np.max(np.abs(recording_gaussiano))  # Normalizar para rango (-1,1)

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
write("recording.wav", freq, recording)
sd.default.samplerate = freq
write("recordingg.wav", freq, recording_gaussiano)
sd.default.samplerate = freq
print("Playing audio")
sd.play(recording)
sd.wait()
print("Playing audio+gauss")
sd.play(recording_gaussiano)
sd.wait()
