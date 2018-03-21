import datetime
import os
import time
import logging
import numpy as np

from src.main.ConfigManager import ConfigManager
from src.main.CsvRetriever import CsvRetriever


class CsvReader:

    # -----------------------------------------------------------
    # Initializing:
    #   configManager: read all the props from queryCreator.ini
    #   timestamp : timestamp
    #   humanTimestamp : timestamp in a human readable format
    #   delimitator: log formatting element
    #   sourcePath : path of the source file
    #   insertStatement: first INSERT's query statement
    #   outputDirectoryPath: path of the output file
    #   fileName : name of the output file
    # ------------------------------------------------------------
    def __init__(self):
        self.timestamp = str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S'))
        self.humanTimestamp = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
        self.delimitator = ' =========================== '
        self.insertStatement = ''
        self.sourcePath = ''
        self.fileName = ''
        self.outputFilePath = ''
        self.csvRetriever = CsvRetriever()
        logging.basicConfig(filename='queryCreator.log', level=logging.DEBUG)
        logging.info(self.delimitator + 'Process started in ' + str(self.humanTimestamp) + self.delimitator)

        logging.info("\n --- Initialization ---")
        self.configManager = ConfigManager()

    def initialize(self):
        logging.info("\n --- Loading configs from .ini file --- \n")

        # self.configManager.setRelativePath('..\..')
        self.configManager.extractProperties()

        self.sourcePath = os.path.join(os.path.join(
            self.configManager.relative_path,
            self.configManager.resourceFolder),
            self.configManager.filename
        )

        self.insertStatement = "INSERT INTO " + self.configManager.nameTable + self.configManager.firstInsertCmd

        outputPath = os.path.join(self.configManager.relative_path, self.configManager.outputFolder)
        self.fileName = 'Inserts' + self.timestamp + '.txt'
        self.outputFilePath = os.path.join(outputPath, self.fileName)

        logging.info('Selected output directory:' + self.outputFilePath)
        logging.info('Path of the written file path:' + self.outputFilePath)

    # -------------------------------------------------------------------------------
    # input: string matrix 'data'
    #
    # Creation of a batch of inserts, looping between each row of the 'data' matrix
    # writing it on a file
    # -------------------------------------------------------------------------------
    def queryCreation(self, data):
        outputFile = open(self.outputFilePath, 'w', encoding='utf-8')
        outputFile.write(self.insertStatement + self.configManager.VALUES + '\n')
        i = 0
        # Should be better to compose the string first.
        for i in range(0, data.shape[0]):
            outputFile.write(
                self.configManager.START_BRACKET + data[i, 1] + "," + self.configManager.loca_id + "," +
                self.configManager.APEX + data[i, 6] + self.configManager.APEX + "," +
                self.configManager.APEX + data[i, 3] + self.configManager.APEX +
                self.configManager.END_BRACKET + '\n'
            )

        logging.info(self.delimitator + str(i + 1) + ' row written. Process ended.' + self.delimitator)
        print('query writings ended')

    # -----------------------------------------------------
    # output: A string's matrix created from the csv file
    # -----------------------------------------------------
    def openCsv(self):
        self.initialize()
        csvMatrix = self.csvRetriever.csvFromTextAcquisition(self.sourcePath)
        logging.info('The matrix produced from the CSV has shape ' + str(np.shape(csvMatrix)))
        return csvMatrix

    # ------------------------------------------------------
    # run the query writing
    # ------------------------------------------------------
    def run(self):
        csvData = self.openCsv()
        self.queryCreation(csvData)

    def setInsertStatement(self, newInsertStatement):
        self.insertStatement = newInsertStatement
