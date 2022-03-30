import sys
import csv


with open('lesson6_task_6_bakery.csv', 'a', encoding ='utf-8') as file:
	price = csv.writer(file, lineterminator='\r')
	price.writerow(sys.argv[1])


		