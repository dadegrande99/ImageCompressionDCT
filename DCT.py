import math
import numpy as np

pi = math.pi
block_dimension = 8 #dovrà essere uguale a quello passato credo

def dct(image):
    dim = len(image)
    dct_image = np.zeros(dim)

    for k in range(dim):
        dct_image[k] = np.sqrt(2/dim) * np.sum(image * np.cos((np.pi/dim) * k * (np.arange(dim) + 0.5)))

        if k == 0:
            dct_image[k] *= 1/np.sqrt(2)
    return dct_image

mtx = dct(np.array([231, 32, 233, 161, 24, 71, 140, 245], dtype=float))
print("--------DCT--------")
for i, row in enumerate(mtx):
   print(row)

def dct2(matrix):
    #avremo in input un'immagine che dovremo convertire in un numpy array
    rows, cols = matrix.shape
    dct_matrix = np.zeros_like(matrix, dtype=float)

    for i in range(rows):
        for j in range(cols):
            sum = 0.0
            coeff_u = 1 if i == 0 else np.sqrt(2)
            coeff_v = 1 if j == 0 else np.sqrt(2)
            for u in range(rows):
                for v in range(cols):
                    pixel_value = matrix[u, v]
                    cosine_u = np.cos((2 * u + 1) * i * pi / (2*rows))
                    cosine_v = np.cos((2 * v + 1) * j * pi / (2*cols))
                    sum += pixel_value * cosine_u * cosine_v
            dct_matrix[i, j] = sum * coeff_u * coeff_v / np.sqrt(rows*cols)
    return dct_matrix

mtx = dct2( np.array([
    [231, 32, 233, 161, 24, 71, 140, 245],
    [247, 40, 248, 245, 124, 204, 36, 107],
    [234, 202, 245, 167, 9, 217, 239, 173],
    [193, 190, 100, 167, 43, 180, 8, 70],
    [11, 24, 210, 177, 81, 243, 8, 112],
    [97, 195, 203, 47, 125, 114, 165, 181],
    [193, 70, 174, 167, 41, 30, 127, 245],
    [87, 149, 57, 192, 65, 129, 178, 228]
], dtype=np.float32))
print("--------DCT2--------")
for row in mtx:
    print(row)