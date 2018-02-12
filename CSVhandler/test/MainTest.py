from src.main.CsvReader import CsvReader


def main():
    reader = CsvReader()
    reader.configManager.setRelativePath('..')
    csvData = reader.openCsv()
    reader.queryCreation(csvData)

main()
