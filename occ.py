import csv
occupations_dict = {}

#with open('occupations.csv') as csvfile:
#	reader = csv.DictReader(csvfile)
#	for row in reader:
#		print(row)

reader = csv.DictReader(open('occupations.csv'))
for row in reader:
	k, v = row['Job Class'], float(row['Percentage'])
	occupations_dict[k] = v
	
print occupations_dict