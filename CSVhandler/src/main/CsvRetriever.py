import numpy as np
import logging

import sys


# noinspection PyMethodMayBeStatic
class CsvRetriever:

    def __init__(self):
        print('')

    # --------------------------------------------------------------
    # Determinate the number of columns of the csv from the header
    # --------------------------------------------------------------
    def checkCsvHeader(self, path):
        logging.info("Checking CSV header")
        csvFile = open(path, 'r', encoding='UTF-8-sig')
        header = csvFile.readline()
        csvFile.close()
        fields = header.split(',')
        if '' in fields:
            fields[fields.index('')] = 'EMPTY'
        header = ' - '.join(fields)

        logging.info("Header size: " + str(len(fields)))
        logging.info("Header: " + header)
        return len(fields)

    # ---------------------------------------------------------
    #  Input:   path: path of the csv file to import
    #  Csv import as text in a matrix form
    # ---------------------------------------------------------
    def csvFromTextAcquisition(self, path):
        cols = self.checkCsvHeader(path)
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

    def getHeaderValues(self,path):
        logging.info("Extracting CSV header")
        csvFile = open(path, 'r', encoding='UTF-8-sig')
        header = csvFile.readline()
        csvFile.close()
        fields = header.split(',')

        if '' in fields:
            fields[fields.index('')] = 'EMPTY'
        for s in fields:
            s = s.strip()
        return fields


