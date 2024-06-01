import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)  # Secuencia lineal de 0 a 10 con 100 puntos

ruido_gaussiano = np.random.normal(1, 0.5, x.shape)

# Aplicar el ruido gaussiano a la secuencia
secuencia_con_ruido = x + ruido_gaussiano

# Visualizar las secuencias
plt.figure(figsize=(10, 5))
plt.plot(x, label='Secuencia Original')
plt.plot(secuencia_con_ruido, label='Secuencia con Ruido Gaussiano')
plt.legend()
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.title('Secuencia Original vs Secuencia con Ruido Gaussiano')
plt.show()
