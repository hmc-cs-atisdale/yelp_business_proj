import csv


idFile = 'reveiwBussinessID.csv'
idList = []

#Get the order of the bussinesses
with open(idFile, 'rb') as f1:
  idList = csv.reader(f1).next()

resultMatrix = []
for i in range(len(idList)):
  resultMatrix.append([])



#Get the features and the bussiness correlated 
filename1 = 'businessLatentFt_ids.csv'#'businessRatings_ids.csv'#'businessLatentFt_ids.csv'
filename2 = 'businessLatentFt_data.csv'#'businessRatings_data.csv' #'businessLatentFt_data.csv'
with open(filename1, 'rb') as f1, open(filename2, 'rb') as f2:
  
  idReader = csv.reader(f1)
  dataReader = csv.reader(f2)

  #For all of the id in the reader
  for bID in idReader: 
    #get the data at that row
    data = dataReader.next()

    #See if this Id is in the dataset
    for i in range(len(idList)):

      #If so add the data to the matrix at the correct row
      if bID[0] == idList[i]:
        resultMatrix[i] = data
        break


outputFile = open('correctLatentFeatures.csv','w+')
csv_writer = csv.writer(outputFile)

for i in range(len(resultMatrix)):
  csv_writer.writerow(resultMatrix[i])

outputFile.close()


