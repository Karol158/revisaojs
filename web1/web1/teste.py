from sklearn.linear_model import LinearRegression # Importa o modelo de regressão linear
import matplotlib.pyplot as plt # A biblioteca de plotagem
import numpy as np

x = np.array([121, 125, 131, 141, 152, 161]).reshape(-1,1) # x denota a área da casa como um atributo.
y = np.array([300, 350, 425, 405,496,517]) # y denota o preço da casa.
plt.scatter(x,y)
plt.xlabel("area") # Eixo X indica a área.
plt.ylabel("price") # Eixo Y indica o preço.
plt.show()