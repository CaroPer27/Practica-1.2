import math

def distancia_minkowski(x, y, p):
    if len(x) != len(y):
        raise ValueError("Los vectores deben tener la misma longitud")
    
    suma = 0
    for i in range(len(x)):
        suma += abs(x[i] - y[i]) ** p
    
    distancia = suma ** (1/p)
    return distancia

vector1 = [0, 2, 3, 4, 6, 8]
vector2 = [2, 4, 3, 7, 9, 2]
p = 3  

dist = distancia_minkowski(vector1, vector2, p)
print(f"Distancia de Minkowski con p={p}: {dist}")