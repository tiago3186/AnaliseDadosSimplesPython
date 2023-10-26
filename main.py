import numpy as np
import matplotlib.pyplot as plt

# Dados de altura e peso de 5 indivíduos
altura = [170, 175, 180, 165, 160]  # Altura em centímetros
peso = [70, 75, 85, 60, 55]  # Peso em quilogramas

# Calculando a média da altura e do peso
media_altura = np.mean(altura)
media_peso = np.mean(peso)

# Calculando a correlação entre altura e peso
correlacao = np.corrcoef(altura, peso)[0, 1]

# Plotando os dados
plt.scatter(altura, peso, label="Dados")
plt.xlabel("Altura (cm)")
plt.ylabel("Peso (kg)")

# Linha de regressão linear
a, b = np.polyfit(altura, peso, 1)
plt.plot(altura, a * np.array(altura) + b, color='red', label="Regressão Linear")

plt.legend()
plt.title(f"Correlação entre altura e peso: {correlacao:.2f}\nMédia de altura: {media_altura:.2f} cm\nMédia de peso: {media_peso:.2f} kg")
plt.show()
