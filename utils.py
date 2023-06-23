import numpy as np


def find_alpha(window: tuple, image: tuple):
    # Calculation of the alpha coefficient for resizing the window in which the image is displayed
    if image[0] >= image[1]:
        i = 0
    else:
        i = 1
    return (window[i]*0.3)/image[i]


def is_pos_int(str: str):
    # Return true if the string contains a positive integer
    str = str.strip()

    if str == "":
        return False

    # Gestione del segno positivo
    if str[0] == '+':
        str = str[1:]
    # Controllo eventuali decimali
    if str.count('.') == 0:
        return str.isdigit()
    elif str.count('.') == 1:
        strs = str.split('.')
        return strs[0].isdigit() and (strs[1].count('0') == len(strs[1]))

    return False


def MtxArrCompare(x: np.array, y: np.array):
    # Return true if x and y are equals, False
    if x.shape != y.shape:
        return False
    return (np.sum(x == y)) == np.prod(x.shape)
