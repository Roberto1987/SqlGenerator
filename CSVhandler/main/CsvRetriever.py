import numpy as np
import logging


def csvFromTextAcquisition(path, cols):
    try:
        X = np.genfromtxt(
            path, delimiter=",", encoding='utf-8',
            skip_header=True, autostrip=True, dtype=None,
            usecols=np.arange(0, cols))
    except:
        logging.warning("File " + path + " not found")

    return X
