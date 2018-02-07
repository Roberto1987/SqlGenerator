import numpy as np
import logging


#  Input:
#       path: path of the csv file to import
#       cols: number of column of the csv need to be taken
#  Csv import as text in a matrix form
import sys


def csvFromTextAcquisition(path, cols):
    try:
        X = np.genfromtxt(
            path, delimiter=",", encoding='utf-8',
            skip_header=True, autostrip=True, dtype=None,
            usecols=np.arange(0, cols))
    except IOError:
        logging.error("File " + path + " not found")
        print("File " + path + " not found")
        sys.exit()

    return X
