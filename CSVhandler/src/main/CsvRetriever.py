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

        csvFile = self.openCsv(path)
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

    # ---------------------------------------------------------
    # Get the header of the CSV
    # ---------------------------------------------------------
    def getHeaderValues(self, path):
        logging.info("Extracting CSV header")

        header = self.getCsvRow(1,path)

        return header

    #-----------------------------------------------------
    # Get the n row of the csv
    #----------------------------------------------------
    def getCsvRow(self, n, path):
        logging.info("Extracting the row " + str(n))
        csvFile = self.openCsv(path)
        row=''
        for i in range(0, n):
            row = csvFile.readline()

        csvFile.close()
        fields = row.split(',')

        if '' in fields:
            fields[fields.index('')] = 'EMPTY'
        for i in range(0, len(fields)):
            fields[i] = fields[i].strip()
        print(fields)
        return row

    # ------------------------------------------------------
    # Managing the opening of the CSV file
    # ------------------------------------------------------
    def openCsv(self, path):
        try:
            csvFile = open(path, 'r', encoding='UTF-8-sig')
        except IOError:
            logging.error("File " + path + " not found")
            print("File " + path + " not found")
            sys.exit()

        return csvFile
