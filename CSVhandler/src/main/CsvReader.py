import datetime
import os
import time
import logging
import numpy as np

from src.main.ConfigManager import ConfigManager
from src.main.CsvRetriever import csvFromTextAcquisition


class CsvReader:

    def __init__(self):
        self.configManager = ConfigManager()
        self.timestamp = str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S'))
        self.humanTimestamp = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
        self.delimitator = ' =========================== '

        logging.basicConfig(filename='queryCreator.log', level=logging.DEBUG)
        logging.info(self.delimitator + 'Process started in ' + str(self.humanTimestamp) + self.delimitator)
        logging.info("\n --- Initialization ---")
        logging.info("\n --- Loading configs from .ini file --- \n")

        self.sourcePath = os.path.join(os.path.join(
                         self.configManager.RELATIVE_PATH,
                         self.configManager.resourceFolder),
                                self.configManager.filename)

        self.insertStatement = "INSERT INTO " + self.configManager.nameTable + self.configManager.firstInsertCmd

        dirName = os.path.join('..', self.configManager.outputFolder)
        logging.info('Selected output directory:' + dirName)
        fileName = 'Inserts' + self.timestamp + '.txt'
        path = os.path.join(dirName, fileName)
        logging.info('Path of the written file path:' + path)

        self.fileInserts = open(path, 'w', encoding='utf-8')

    def queryCreation(self, data):
        for i in range(0, data.shape[0]):
            self.fileInserts.write(
                self.configManager.START_BRACKET + data[i, 1] + "," + self.configManager.loca_id + "," +
                self.configManager.APEX + data[i, 6] + self.configManager.APEX + "," +
                self.configManager.APEX + data[i, 3] + self.configManager.APEX +
                self.configManager.END_BRACKET + '\n'
            )

        logging.info(self.delimitator + str(i + 1) + ' rows processed. Process ended.' + self.delimitator)
        print('query writings ended')

    def openCsv(self):
        X = csvFromTextAcquisition(self.sourcePath, int(self.configManager.cols));
        xShape = np.shape(X)
        logging.info('The matrix produced from the CSV has shape ' + str(xShape))  #

        self.fileInserts.write(self.configManager.firstInsertCmd + self.configManager.VALUES + '\n')
        return X


reader = CsvReader()
csvData = reader.openCsv()
reader.queryCreation(csvData)
