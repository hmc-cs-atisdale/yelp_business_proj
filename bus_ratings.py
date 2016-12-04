import json
from scipy import sparse, io
import numpy as np
import csv

#business_clean = open('test_clean.json', 'w+')
business_dict = {}
attributes = []

outputFile = open('businessRatings_ids.csv','w+', newline='')
outputFile2 = open('businessRatings_data.csv','w+', newline='')

csv_writer = csv.writer(outputFile)
csv_writer2 = csv.writer(outputFile2)

for line in open('yelp_academic_dataset_business.json'):
	business_json = json.loads(line)
	
	if 'stars' in business_json:
		# buss_attr = business_json["attributes"]
		# attr_list = []
		# for attr in buss_attr.keys():
		# 	if buss_attr[attr] == True or buss_attr[attr] == False:
		# 		if attr not in attributes:
		# 			attributes.append(attr)
		# 		attr_list.append((attr, buss_attr[attr]))
		business_dict[business_json["business_id"]] = business_json["stars"]
		csv_writer.writerow([business_json["business_id"]])
		csv_writer2.writerow([business_json["stars"]])
print(business_dict)

# print(business_dict)
# print(attributes)
# modif_attr = ['Business ID']
# modif_attr.extend(attributes)
# big_array = np.array(modif_attr)

# # print(big_array)
# for bus in business_dict:
# 	arr = [-1]*len(modif_attr)
# 	# print(arr)
# 	arr[0] = bus
# 	for elem, truth in business_dict[bus]:
# 		# print(truth)
# 		arr[modif_attr.index(elem)] = int(truth)
# 	big_array = np.vstack((big_array, arr))
# # print(big_array)

# rowNum, colNum = big_array.shape

# outputFile = open('businessLatentFt_data.csv','w+', newline='')
# outputFile1 = open('businessLatentFt_headers.csv','w+', newline='')
# outputFile2 = open('businessLatentFt_ids.csv','w+', newline='')
# csv_writer = csv.writer(outputFile)
# csv_writer1 = csv.writer(outputFile1)
# csv_writer2 = csv.writer(outputFile2)
# csv_writer1.writerow(big_array[0][1:])


# for i in range(1, rowNum):
# 	csv_writer.writerow(big_array[i][1:])
# 	csv_writer2.writerow([big_array[i][0]])

outputFile.close()
# outputFile1.close()
outputFile2.close()



