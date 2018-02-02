import datetime
import os
import time
import logging
import numpy as np

from main.ConfigManager import ConfigManager
from main.CsvRetriever import csvFromTextAcquisition


timestamp = str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S'))
logging.basicConfig(filename='queryCreator.log',level=logging.DEBUG)

logging.info("\n --- Creating config manager --- \n")
configManager = ConfigManager()
logging.info("\n --- Loading configs from .ini file --- \n")
configManager.loadConfigs()
sourcePath = os.path.join(os.path.join(configManager.RELATIVE_PATH, configManager.resourceFolder), configManager.filename)

insertStatement = 'INSERT INTO translation_competitors(sport,loca_id,long_name,english_name)'
VALUES = 'Values'
END_BRACKET = ")"
LOCA_ID = configManager.loca_id
START_BRACKET = "("
APEX = '\''
COLS = 7

dirName = os.path.join('..', configManager.outputFolder)
logging.info('Selected output directory:' + dirName)
fileName = 'Inserts' + timestamp + '.txt'
path = os.path.join(dirName, fileName)
logging.info('Path of the written file path:' + path)
#print('Path of the written file path', path)
fileInserts = open(path, 'w', encoding='utf-8')

X = csvFromTextAcquisition(sourcePath, COLS);

xShape = np.shape(X)
print('The matrix produced from the CSV has shape ' + str(xShape))  #

# --------Initial insert-------------
fileInserts.write(
    insertStatement
    + VALUES+ '\n')
# -----------------------------------

for i in range(0, X.shape[0]):
    if i % 10 == 0:
        print('row from ' + str(i - 10 + 1) + ' until ' + str(i) + ' has been processed')

    fileInserts.write(
        START_BRACKET + X[i, 1] + "," + LOCA_ID + "," + APEX + X[i, 6] + APEX + ","
        + APEX + X[i, 3] + APEX + END_BRACKET + '\n')

print('\n' + str(i) + ' rows processed')

