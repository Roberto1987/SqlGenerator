import datetime
import os
import time
import logging
import numpy as np

from src.main.ConfigManager import ConfigManager
from src.main.CsvRetriever import csvFromTextAcquisition

# ----String constant
print("Query writing process started")
delimitator = ' =========================== '
timestamp = str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S'))
humanTime = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
logging.basicConfig(filename='queryCreator.log', level=logging.DEBUG)
logging.info(delimitator+'Process started in '+ str(humanTime) + delimitator)

logging.info("\n --- Creating config manager --- \n")
configManager = ConfigManager()
logging.info("\n --- Loading configs from .ini file --- \n")
configManager.loadConfigs()
sourcePath = os.path.join(os.path.join(configManager.RELATIVE_PATH, configManager.resourceFolder),
                          configManager.filename)

insertStatement = "INSERT INTO " + configManager.nameTable + configManager.firstInsertCmd

dirName = os.path.join('..', configManager.outputFolder)
logging.info('Selected output directory:' + dirName)
fileName = 'Inserts' + timestamp + '.txt'
path = os.path.join(dirName, fileName)
logging.info('Path of the written file path:' + path)
# print('Path of the written file path', path)
fileInserts = open(path, 'w', encoding='utf-8')

X = csvFromTextAcquisition(sourcePath, int(configManager.cols));

xShape = np.shape(X)
logging.info('The matrix produced from the CSV has shape ' + str(xShape))  #

# --------Initial insert-------------
fileInserts.write(configManager.firstInsertCmd + configManager.VALUES + '\n')
# -----------------------------------

for i in range(0, X.shape[0]):
    fileInserts.write(
        configManager.START_BRACKET +
        X[i, 1] + "," + configManager.loca_id + "," +
        configManager.APEX + X[i, 6] + configManager.APEX + "," +
        configManager.APEX + X[i, 3] + configManager.APEX +
        configManager.END_BRACKET + '\n'
    )


logging.info(delimitator+  str(i+1) + ' rows processed. Process ended.' +delimitator)
print('query writings ended')
