def find_alpha(window:tuple,image:tuple):
    if image[0]>=image[1]:
        i = 0
    else:
        i = 1
    return (window[i]*0.3)/image[i]

def is_pos_int(str:str):
    str = str.strip()

    if str == "":
        return False

    # Gestione del segno positivo
    if str[0] == '+':
        str = str[1:]
    #Controllo eventuali decimali
    if str.count('.') == 0:
        return str.isdigit()
    elif str.count('.') == 1:
        strs = str.split('.')
        return strs[0].isdigit() and (strs[1].count('0') == len(strs[1]))

    return False