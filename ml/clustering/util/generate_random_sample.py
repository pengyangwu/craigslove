import os
import csv
import numpy as np

"""
get random sample of n posts from each city
"""

def write_sample(in_path, out_path, n):
	# count num rows
	row_count = 0
	with open(in_path,'r') as in_file:
		file_reader = csv.reader(in_file) 
		row_count = sum(1 for row in file_reader)

	with open(in_path,'r') as in_file, open(out_path, 'w') as out_file:
		file_reader = csv.reader(in_file) 
		file_writer = csv.writer(out_file)
		rows_to_sample = np.random.choice(np.arange(1,row_count), n, replace=False)
		rows_to_sample = rows_to_sample.tolist()
		i = 0
		for row in file_reader:
			if i in rows_to_sample:
				file_writer.writerow(row)
			i += 1
		print in_path + ' has ' + str(i) + ' rows. Sampled ' + str(n)

def main():

	n = 5000

	### generate random samples per city
	for city in os.listdir('../data/city'):
		f = os.path.join('../data/city', city)
		if f.endswith('.csv'): 
			new_sample_file = '../data/city/sample/' + city
			write_sample(f, new_sample_file, n)

if __name__ == '__main__':
	main()