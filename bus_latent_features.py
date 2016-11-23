import json
from pprint import pprint

import json

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

