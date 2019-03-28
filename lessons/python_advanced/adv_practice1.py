import csv
import re

def count_degrees(csv_file_name):
	open_degrees = open(csv_file_name)
	read_degrees = csv.reader(open_degrees)
	degrees_table = list(read_degrees)
	degrees_header = degrees_table[0]
	degrees_table = degrees_table[1:]
	
	print(degrees_table[0])

	degrees = {}

	for row in degrees_table:
		for item in row[1].upper().replace('.', '').split(' '):
			if item in degrees:
				degrees[item] += 1
			else:
				degrees[item] = 1

	del degrees['']
	return degrees

def count_titles(csv_file_name):
	open_degrees = open(csv_file_name)
	read_degrees = csv.reader(open_degrees)
	degrees_table = list(read_degrees)
	degrees_header = degrees_table[0]
	degrees_table = degrees_table[1:]

	titles = {}

	for row in degrees_table:
		if row[2].split(' ')[0] in titles:
			titles[row[2].split(' ')[0]] += 1
		else:
			titles[row[2].split(' ')[0]] = 1

	return titles


def get_emails(csv_file_name):
	open_degrees = open(csv_file_name)
	read_degrees = csv.reader(open_degrees)
	degrees_table = list(read_degrees)
	degrees_header = degrees_table[0]
	degrees_table = degrees_table[1:]

	emails = []

	for row in degrees_table:
		emails.append(row[3])

	return emails


def write_to_csv(list_of_emails):
    with open('emails.csv', 'w') as emails_csv:
        writer = csv.writer(emails_csv)
        writer.writerow(['list_of_emails'])
        for email in list_of_emails:
        	writer.writerow([email])

# def get_dict(csv_file_name):
# 	open_degrees = open(csv_file_name)
# 	read_degrees = csv.reader(open_degrees)
# 	degrees_table = list(read_degrees)
# 	degrees_header = degrees_table[0]
# 	degrees_table = degrees_table[1:]

# 	faculty = {}

# 	for row in degrees_table:
# 		if row[0].split(' ')[-1] in faculty:
# 			faculty[row[0].split(' ')[-1]].append(row[1:])
# 		else:
# 			faculty[row[0].split(' ')[-1]] = [row[1:]]

# 	return faculty

def get_dict(csv_file_name):
	open_degrees = open(csv_file_name)
	read_degrees = csv.reader(open_degrees)
	degrees_table = list(read_degrees)
	degrees_header = degrees_table[0]
	degrees_table = degrees_table[1:]

	faculty = {}

	for row in degrees_table:
		tup = tuple(row[0].split(' '))
		faculty[tup] = row[1:]

	return faculty


get_dict('faculty.csv')