import math
import numpy as np


def custom_dct(image):
    dim = len(image)
    dct_image = np.zeros(dim)

    for k in range(dim):
        dct_image[k] = np.sqrt(2/dim) * np.sum(image *
                                               np.cos((np.pi/dim) * k * (np.arange(dim) + 0.5)))

    dct_image[0] *= 1/np.sqrt(2)
    return dct_image


def custom_dct2(matrix):
    # Avremo in input un'immagine che dovremo convertire in un numpy array

    # Applica la DCT alle colonne
    dct_cols = np.zeros_like(matrix, dtype=float)
    for i in range(matrix.shape[1]):
        dct_cols[:, i] = custom_dct(matrix[:, i])

    # Applica la DCT alle righe così da ottenere il risultato completo
    dct_full = np.zeros_like(matrix, dtype=float)
    for i in range(matrix.shape[0]):
        dct_full[i, :] = custom_dct(dct_cols[i, :])

    return dct_full


def custom_idct2(dct_image):
   # Ottieni le dimensioni del blocco
    M, N = dct_image.shape

    # Inizializza l'array per il blocco di output (matrice con i valori originali ricostruiti)
    f = np.zeros((M, N), dtype=np.float64)

    # Calcola la DCT2 inversa per ogni punto del blocco
    for i in range(M):
        for j in range(N):
            # Calcola il valore del punto (i, j) del blocco di output
            value = 0.0
            for x in range(M):
                for y in range(N):
                    # Calcola il coefficiente di coseno
                    coef = np.cos((np.pi / M) * (i + 0.5) * x) * \
                        np.cos((np.pi / N) * (j + 0.5) * y)

                    # Aggiungi il termine alla somma delle componenti del segnale originale 
                    value += coef * dct_image[x, y]

            # Moltiplica il valore per il fattore di normalizzazione
            value *= (2 / M) * (2 / N)

            # Assegna il valore al punto (i, j) del blocco di output
            f[i, j] = value

    return f
