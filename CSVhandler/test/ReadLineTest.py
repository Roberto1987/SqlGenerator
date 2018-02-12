from src.main.CsvRetriever import CsvRetriever
sourcePath = '../res/CsvFile2.csv'
csvRetriever = CsvRetriever(path=sourcePath)

row = 5;
print("row "+str(row)+":"+ csvRetriever.getCsvRow(n=row))

print("header: "+str(csvRetriever.getHeaderValues()))