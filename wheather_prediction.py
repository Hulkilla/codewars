import numpy as np
days = 4

weather_today = 2

weather_final = 0

Prediction = [[0.1, 0.1, 0.8], 
              [0.2, 0.7, 0.1],
              [0.4, 0.2, 0.4]]

## Este ejercicio se basa en las cadenas de Markov

'''
Esto sirve para cuando los días son 2 porque sino lo que hay que hacer es elevar al potencia de predicciones al número de días

k=len(Prediction[0])

suma = 0

for i in range(k):
    suma += Prediction[weather_today][i] * Prediction[i][weather_final]
    print(i)
    print(round(suma,3))

print(suma)

'''

## Solucion chachipistachi

'''
en este caso de estudio, como tenemos 4 días en el que pueden pasar cosas, la probabilidad condicionada de 1 solo día,
hay que elevarla a la 4 (si fueran 5 días, serían a la 5)

como nuestro estado inicial es 2 y el final es 0, basta con sacar por pantalla, la posición [2,0] de la matriz elevada
'''
P_4 = np.linalg.matrix_power(Prediction, 4)
prob_4_days = P_4[2, 0]

print(P_4)
print(prob_4_days)