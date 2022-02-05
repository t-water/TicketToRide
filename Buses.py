import csv

buses = {}

with open('TransportationCards.csv', newline='') as csv_file:
    bus_reader = csv.reader(csv_file, delimiter=' ', quotechar='|')
    for row in bus_reader:
        entries = row[0].split(',')
        buses[entries[0]] = int(entries[1])

print(buses)