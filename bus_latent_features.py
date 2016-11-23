import json
from scipy import sparse, io
import numpy as np

business_clean = open('test_clean.json', 'w+')
business_dict = {}
attributes = []

for line in open('test.json'):
	business_json = json.loads(line)
	if 'attributes' in business_json:
		buss_attr = business_json["attributes"]
		attr_list = []
		for attr in buss_attr.keys():
			if buss_attr[attr] == True or buss_attr[attr] == False:
				if attr not in attributes:
					attributes.append(attr)
				attr_list.append((attr, buss_attr[attr]))
		business_dict[business_json["business_id"]] = attr_list

print(business_dict)
print(attributes)
modif_attr = [0]
modif_attr.extend(attributes)
big_array = np.array(modif_attr)

print(big_array)
for bus in business_dict:
	arr = [0]*len(modif_attr)
	print(arr)
	arr[0] = bus
	for elem, truth in business_dict[bus]:
		arr[modif_attr.index(elem)] = int(truth)


shape = (len(business_dict.keys()), len(attributes))
matrix = sparse.coo_matrix(shape)
print(matrix.shape)


io.savemat('business_attr.mat', dict(matrix = matrix))

