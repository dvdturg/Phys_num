import numpy as np

STEP = 2880.879435 # (nm) taille d'un pas d'échantillonnage le long de l'axe optique
ORDER = 8 # ordre de repliement spectral
STEP_NB = 593 # nombre de pas de l'interférogramme = dimension du spectre calculé
ZPD_INDEX = 215 # position de la ZPD
OVERSAMPLING_FACTOR = STEP_NB / (STEP_NB - ZPD_INDEX) # facteur de suréchantillonage

FILTER_MIN = 14600
FILTER_MAX = 15450

LIGHT_VEL_KMS = 299792.458 # vitesse de la lumière en km/s

# longueurs d'onde en nm des raies d'émission présentes dans le cube
HA = 656.28 # Hydrogène ionisé (Halpha)
NII_1 = 654.805 # Azote ionisé 
NII_2 = 658.345 # Azote ionisé
SII_1 = 671.6440 # Soufre ionisé
SII_2 = 673.0816 # Soufre ionisé


def axis_min(theta):
    """nombre d'onde (cm-1) minimum de l'axe spectral
    
    :param theta: Angle d'incidence
    """
    return ORDER /  ( 2 * STEP * np.cos(np.deg2rad(theta))) * 1e7

def axis_step(theta):
    """nombre d'onde (cm-1) d'un pas d'échantillonage de l'axe spectral
    
    :param theta: Angle d'incidence
    """
    return 1 / (2 * STEP * np.cos(np.deg2rad(theta)) * STEP_NB) * 1e7

def pix2cm1(pix, theta):
    """conversion d'une position en pixel à un nombre d'onde (cm-1)
    
    :param pix: position en pixel
    :param theta: Angle d'incidence
    """
    return axis_min(theta) + pix * axis_step(theta)

def cm12pix(cm1, theta):
    """conversion d'un nombre d'onde (cm-1) vers une position en pixel.
    
    :param cm1: nombre d'onde
    :param theta: Angle d'incidence
    """
    return (cm1 - axis_min(theta)) / axis_step(theta)

def get_cm1_axis(theta):
    """Retourne un axe spectral """
    return pix2cm1(np.arange(STEP_NB), theta)




