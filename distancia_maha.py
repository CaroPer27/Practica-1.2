import numpy as np

def mahalanobis(x,data):
    media = np.mean(data, axis = 0)
    covarianza = np.cov(data, rowvar = False)
    diff = x - media
    cov_inversa = np.linalg.inv(covarianza)
    distancia = np.sqrt(np.dot(np.dot(diff, cov_inversa),diff.T))
    
    return distancia