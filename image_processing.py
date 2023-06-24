import numpy as np
import cv2
from DCT import custom_dct2, custom_idct2


def process_image(image_path, F, d):
    # suddividere l’immagine in blocchi quadrati f di pixel di dimensioni F×F partendo in alto a sinistra, scartando gli avanzi;
    image = cv2.imread(image_path, 0)
    height, width = image.shape
    bw = width // F  # block width
    bh = height // F  # block height
    image = image[:bh*F, :bw*F]

    blocks = np.split(image, bh, axis=0)
    blocks = [np.split(block, bw, axis=1) for block in blocks]
    blocks = np.array(blocks)

    # Applica il processo a ciascun blocco
    for i in range(bh):
        for j in range(bw):
            block = blocks[i, j]

            # Applica la DCT2
            # c = custom_dct2(np.float32(block))
            c = cv2.dct(np.float32(block))

            # Taglia le frequenze
            c = threshold_cutoff(c, d)

            # Applica l'inversa della DCT2
            # ff = custom_idct2(c)
            ff = cv2.idct(c)

            # Arrotonda e normalizza i valori
            ff = np.round(ff)
            ff = np.clip(ff, 0, 255)

            # Aggiorna il blocco ricostruito
            blocks[i, j] = ff

    # Ricompone l'immagine a partire dai blocchi
    reconstructed_image = np.block(
        [[block for block in row] for row in blocks])

    # Converte l'immagine in formato byte
    reconstructed_image = reconstructed_image.astype(np.uint8)
    return reconstructed_image


def threshold_cutoff(coefficients, threshold):
    size = coefficients.shape[0]
    for i in range(size):
        for j in range(size):
            if i + j >= threshold:
                coefficients[i, j] = 0
    return coefficients
