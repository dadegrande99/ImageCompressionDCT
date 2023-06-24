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


def printTime(time):
    tmp = []
    tmp.append(time)  # microsecondi - tmp[0]
    tmp.append((int)(tmp[0]/1000))  # millisecondi - tmp[1]
    tmp.append((int)(tmp[1]/1000))  # secondi - tmp[2]
    tmp.append((int)(tmp[2]/60))  # minuti - tmp[3]

    tmp[0] = tmp[0] - (tmp[1] * 1000)
    tmp[1] = tmp[1] - (tmp[2] * 1000)
    tmp[2] = tmp[2] - (tmp[3] * 60)

    mu = "\u03BC"

    if tmp[3] != 0:
        res = str(tmp[3]) + "m " + str(tmp[2]) + "s"
    elif tmp[2] != 0:
        res = str(tmp[2]) + "." + str(round(tmp[1]/100)) + "s"
    elif tmp[1] != 0:
        res = str(tmp[1]) + "." + str(round(tmp[0]/100)) + "ms"
    else:
        res = str(tmp[0]) + "\u03BCs"

    # print(str(tmp[3]) + " : " + str(tmp[2]) + " : " + str(tmp[1]) + " : " + str(tmp[0]))
    # print(res)
    return (res)


def reFormat(x: np.array, sig: int):
    for i in range(len(x)):
        if type(x[i]) is np.array:
            x[i] = reFormat(x[i], sig)
        elif not (np.isnan(x[i])):
            x[i] = reFormatNumber(x[i], sig)
    return x


def reFormatNumber(x: np.generic, sig: int):
    string = str(x)
    fon = sig  # quantità di numeri significativi che voglio tenere
    if '-' in string[:fon]:
        fon += 1
    if '.' in string[:fon]:
        fon += 1
    return float(string[:fon])
