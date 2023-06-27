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


def custom_idct(vector):
    # Calcola l'IDCT-II per un vettore unidimensionale

    N = len(vector)
    idct_vector = np.zeros(N)

    for n in range(N):
        sum_val = (1 / np.sqrt(2)) * vector[0]
        for k in range(1, N):
            sum_val += vector[k] * np.cos((np.pi / N) * (n + 0.5) * k)
        idct_vector[n] = sum_val * np.sqrt(2 / N)

    return idct_vector


def custom_idct2(matrix):
    # Calcola l'IDCT-II per una matrice bidimensionale

    # Applica l'IDCT alle righe
    idct_rows = np.zeros_like(matrix, dtype=float)
    for i in range(matrix.shape[0]):
        idct_rows[i, :] = custom_idct(matrix[i, :])

    # Applica l'IDCT alle colonne così da ottenere il risultato completo
    idct_full = np.zeros_like(matrix, dtype=float)
    for i in range(matrix.shape[1]):
        idct_full[:, i] = custom_idct(idct_rows[:, i])

    return idct_full
