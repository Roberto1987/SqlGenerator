# ----FIXED CONSTANT
import configparser
import os

import logging


class ConfigManager:
    RELATIVE_PATH = '..'
    SETTINGS_FOLDER = 'settings'
    PROPERTIES_FILE_NAME = 'queryCreator.ini'
    START_BRACKET = "("
    APEX = '\''
    VALUES = 'Values'
    END_BRACKET = ")"

    query = ''
    firstInsertCmd = ''
    outputFolder = 'UNSETTED'
    resourceFolder = 'UNSETTED'
    loca_id = 'UNSETTED'
    nameTable = "GenericTable"
    cols = 0
    filename = ''

    def __init__(self):
        # ----loading props parser
        config = configparser.ConfigParser()
        # ----building props path
        configPath = os.path.join(os.path.join(self.RELATIVE_PATH, self.SETTINGS_FOLDER), self.PROPERTIES_FILE_NAME)
        logging.info('Configuration path: ' + configPath)

        # ----reading props
        config.read(configPath)

        # ----extracting the properties
        self.query = config['QuerySettings']['query.insert']
        self.nameTable = config['QuerySettings']['query.nameTable']
        self.firstInsertCmd = config['QuerySettings']['query.insert.firstInsert']
        self.outputFolder = config['GeneralSettings']['qc.outputFolder']
        self.loca_id = config['TranslationSettings']['translation.localisation_id']
        self.resourceFolder = config['CsvSettings']['csv.sourceFolder']
        self.cols = config['CsvSettings']['csv.columns']
        self.filename = config['CsvSettings']['csv.filename']

        logging.info(" ---------- Exported properties ---------- ")
        logging.info("\t Query type: " + self.query)
        logging.info("\t Table name: " + self.nameTable)
        logging.info("\t First Insert code: " + self.firstInsertCmd)
        logging.info("\t Localization code: " + self.loca_id)
        logging.info("\t Output folder: " + self.outputFolder)
        logging.info("\t Source folder: " + self.resourceFolder)
        logging.info("\t CSV number of columns: " + self.cols)
        logging.info("\t filename: " + self.filename)
        logging.info("------------------------------------------ ")
