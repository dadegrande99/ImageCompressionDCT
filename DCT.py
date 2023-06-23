import math
import numpy as np

#sarà da inizializzare a random sulla base delle "dimensioni" fornite dall'Array N che dovrà avere ampi valori
matrix = [[255, 255, 255, 255, 255, 255, 255, 255],
          [255, 255, 255, 255, 255, 255, 255, 255],
          [255, 255, 255, 255, 255, 255, 255, 255],
          [255, 255, 255, 255, 255, 255, 255, 255],
          [255, 255, 255, 255, 255, 255, 255, 255],
          [255, 255, 255, 255, 255, 255, 255, 255],
          [255, 255, 255, 255, 255, 255, 255, 255],
          [255, 255, 255, 255, 255, 255, 255, 255]]

pi = math.pi
block_dimension = 8 #dovrà essere uguale a quello passato credo

#bisognerà passare un'immagine e prenderne le sue dimensioni
def dct():
    image = np.random.randint(0, 256, size=((80, 80)))
    image_height, image_width = image.shape
    dct_matrix = np.zeros((image_height, image_width))
    for y in range(0,  image_height, block_dimension):
        for x in range(0, image_width, block_dimension):
            block = image[y:y+block_dimension, x:x+block_dimension]
            dct_block = calculate_dct(block)
            dct_matrix[y:y+block_dimension, x:x+block_dimension] = dct_block
    
    return dct_matrix

def calculate_dct(block):
    for i in range(block_dimension):
        for j in range(block_dimension):
            sum = 0
            for u in range(block_dimension):
                for v in range(block_dimension):
                    pixel_value = block[i, j]
                    cosine_u = cosine(u, i, block_dimension)
                    cosine_v = cosine(v, j, block_dimension)
                    sum += pixel_value * cosine_u * cosine_v
            dct_coeff = sum * coefficient_normalization(u, block_dimension) * coefficient_normalization(v, block_dimension)
            block[u, v] = dct_coeff
    return block

def cosine(k, n, block_dim):
    return math.cos((k * (pi/block_dim)) * n)

def coefficient_normalization(coeff, block_dim, dct2 = False):
    if(dct2 == False):
        if (coeff == 0):
            return math.sqrt(1/block_dim)
        else:
            return math.sqrt(2/block_dim)
    else:
        if (coeff == 0):
            return math.sqrt(1/2)
        else:
            return math.sqrt(2)

#mtx = dct()
#for i, row in enumerate(mtx):
#   print(row)

def dct2(matrix):
    rows, cols = matrix.shape
    dct_matrix = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            sum = 0
            for u in range(rows):
                for v in range(cols):
                    pixel_value = matrix[i, j]
                    cosine_u = cosine(u, i, block_dimension)
                    cosine_v = cosine(v, j, block_dimension)
                    sum += pixel_value * cosine_u * cosine_v
            dct_coeff = sum * coefficient_normalization(u, block_dimension, True) * coefficient_normalization(v, block_dimension, True)
            dct_matrix[u, v] = dct_coeff
    return dct_matrix

mtx = dct2(np.random.randint(0, 256, size=((80, 80))))
for i, row in enumerate(mtx):
    print(row)