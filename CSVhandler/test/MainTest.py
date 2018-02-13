from src.main.CsvReader import CsvReader


def main():
    reader = CsvReader()
    reader.configManager.setRelativePath('..')
    reader.run()


main()
